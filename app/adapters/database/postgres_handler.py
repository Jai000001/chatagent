import json
import asyncpg
from app.core.app_config import app_config
from app.core.logger import Logger

logger = Logger.get_logger(__name__)

class PostgresHandler:
    def __init__(self, db_url=None):
        self.db_url = db_url or app_config.POSTGRES_DATABASE_URL
        self.pool = None
        self._pool_size = app_config.POSTGRES_POOL_SIZE
        self._initialized = False

    async def init(self):
        """Initialize the connection pool and ensure tables exist."""
        if self._initialized:
            logger.info("PostgresHandler already initialized")
            return
        try:
            logger.info(f"Initializing PostgreSQL connection pool (size: {self._pool_size})")
            self.pool = await asyncpg.create_pool(
                dsn=self.db_url,
                min_size=1,
                max_size=self._pool_size,
                command_timeout=120
            )
            await self.ensure_tables_exist()
            self._initialized = True
            logger.info("PostgresHandler initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize PostgreSQL connection pool: {e}")
            if self.pool:
                await self.pool.close()
                self.pool = None
            raise

    async def ensure_tables_exist(self):
        """Create all required tables if they don't exist."""
        create_table_queries = [
            '''CREATE TABLE IF NOT EXISTS visited_urls (
                url TEXT,
                task_id TEXT,
                created_at TIMESTAMP DEFAULT NOW(),
                PRIMARY KEY (url, task_id)
            );''',
            '''CREATE TABLE IF NOT EXISTS scraped_docs (
                url TEXT,
                content TEXT,
                metadata JSONB,
                task_id TEXT,
                created_at TIMESTAMP DEFAULT NOW(),
                PRIMARY KEY (url, task_id)
            );''',
            '''CREATE TABLE IF NOT EXISTS scraped_status (
                task_id TEXT,
                url TEXT,
                status TEXT,
                error TEXT,
                reason TEXT,
                created_at TIMESTAMP DEFAULT NOW(),
                PRIMARY KEY (task_id, url)
            );''',
            '''CREATE TABLE IF NOT EXISTS website_pdf_files (
                task_id TEXT,
                url TEXT,
                filename TEXT,
                created_at TIMESTAMP DEFAULT NOW(),
                PRIMARY KEY (task_id, url)
            );''',
            '''CREATE TABLE IF NOT EXISTS external_links (
                task_id TEXT,
                parent_url TEXT,
                external_url TEXT,
                external_domain TEXT,
                created_at TIMESTAMP DEFAULT NOW(),
                PRIMARY KEY (task_id, parent_url, external_url)
            );''',
            '''CREATE TABLE IF NOT EXISTS website_pdf_status (
                task_id TEXT,
                url TEXT,
                status TEXT,
                error TEXT,
                pages INT,
                reason TEXT,
                created_at TIMESTAMP DEFAULT NOW(),
                PRIMARY KEY (task_id, url)
            );''',
            '''CREATE TABLE IF NOT EXISTS upload_files_docs (
                filename TEXT,
                content TEXT,
                metadata JSONB,
                task_id TEXT,
                created_at TIMESTAMP DEFAULT NOW(),
                PRIMARY KEY (filename, task_id)
            );'''
        ]
        
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                for query in create_table_queries:
                    await conn.execute(query)

                # Ensure indexes for fast deletes on created_at
                index_queries = [
                    """CREATE INDEX IF NOT EXISTS idx_visited_urls_created_at ON visited_urls (created_at);""",
                    """CREATE INDEX IF NOT EXISTS idx_scraped_docs_created_at ON scraped_docs (created_at);""",
                    """CREATE INDEX IF NOT EXISTS idx_external_links_created_at ON external_links (created_at);""",
                    """CREATE INDEX IF NOT EXISTS idx_website_pdf_status_created_at ON website_pdf_status (created_at);""",
                    """CREATE INDEX IF NOT EXISTS idx_upload_files_docs_created_at ON upload_files_docs (created_at);""",
                    """CREATE INDEX IF NOT EXISTS idx_scraped_status_created_at ON scraped_status (created_at);""",
                    """CREATE INDEX IF NOT EXISTS idx_website_pdf_files_created_at ON website_pdf_files (created_at);""",
                ]
                for idx_query in index_queries:
                    await conn.execute(idx_query)
                
        logger.info("All tables and indexes ensured to exist")

    async def close_db_pool(self):
        """Close the connection pool."""
        if self.pool:
            logger.info("Closing PostgreSQL connection pool")
            await self.pool.close()
            self.pool = None
            self._initialized = False

    async def is_visited(self, url, task_id):
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow("SELECT 1 FROM visited_urls WHERE url = $1 AND task_id = $2", url, task_id)
            return row is not None

    async def mark_visited(self, url, task_id):
        async with self.pool.acquire() as conn:
            await conn.execute(
                "INSERT INTO visited_urls (url, task_id) VALUES ($1, $2) ON CONFLICT DO NOTHING",
                url, task_id
            )

    async def store_website_links_document(self, doc):
        try:
            clean_content = doc.page_content.replace('\x00', '')
            async with self.pool.acquire() as conn:
                await conn.execute(
                    """
                    INSERT INTO scraped_docs (url, content, metadata, task_id)
                    VALUES ($1, $2, $3, $4)
                    ON CONFLICT (url, task_id) DO NOTHING
                    """,
                    doc.metadata['source'], clean_content, json.dumps(doc.metadata), doc.metadata['task_id']
                )
            return True
        except Exception as e:
            logger.error(f"Failed to store document in Postgres for {doc.metadata['source']} (task_id={doc.metadata['task_id']}): {e}")
            return False

    async def add_scraped_status(self, task_id, url, status, error=None, reason=None):
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO scraped_status (task_id, url, status, error, reason)
                VALUES ($1, $2, $3, $4, $5)
                ON CONFLICT (task_id, url) DO UPDATE SET status = EXCLUDED.status, error = EXCLUDED.error, reason = EXCLUDED.reason
                """,
                task_id, url, status, error, reason
            )

    async def add_website_pdf_file(self, task_id, url, filename):
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO website_pdf_files (task_id, url, filename)
                VALUES ($1, $2, $3)
                ON CONFLICT (task_id, url) DO NOTHING
                """,
                task_id, url, filename
            )

    async def add_external_link(self, task_id, parent_url, external_url, external_domain):
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO external_links (task_id, parent_url, external_url, external_domain)
                VALUES ($1, $2, $3, $4)
                ON CONFLICT (task_id, parent_url, external_url) DO NOTHING
                """,
                task_id, parent_url, external_url, external_domain
            )

    async def add_website_pdf_status(self, task_id, url, status, error=None, pages=0, reason=None):
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO website_pdf_status (task_id, url, status, error, pages, reason)
                VALUES ($1, $2, $3, $4, $5, $6)
                ON CONFLICT (task_id, url) DO UPDATE SET status = EXCLUDED.status, error = EXCLUDED.error, pages = EXCLUDED.pages, reason = EXCLUDED.reason
                """,
                task_id, url, status, error, pages, reason
            )

    async def get_scraped_status(self, task_id):
        async with self.pool.acquire() as conn:
            rows = await conn.fetch("SELECT url, status, error, reason FROM scraped_status WHERE task_id = $1", task_id)
            return [{"url": r["url"], "status": r["status"], "error": r["error"], "reason": r["reason"]} for r in rows]

    async def get_website_pdf_files(self, task_id):
        async with self.pool.acquire() as conn:
            rows = await conn.fetch("SELECT url, filename FROM website_pdf_files WHERE task_id = $1", task_id)
            return [{"url": r["url"], "filename": r["filename"]} for r in rows]

    async def get_external_links(self, task_id):
        async with self.pool.acquire() as conn:
            rows = await conn.fetch("SELECT parent_url, external_url, external_domain FROM external_links WHERE task_id = $1", task_id)
            return [{"parent_url": r["parent_url"], "external_url": r["external_url"], "external_domain": r["external_domain"]} for r in rows]

    async def get_website_pdf_status(self, task_id):
        async with self.pool.acquire() as conn:
            rows = await conn.fetch("SELECT url, status, error, pages, reason FROM website_pdf_status WHERE task_id = $1", task_id)
            return [
                {"url": r["url"], "status": r["status"], "error": r["error"], "pages": r["pages"], "reason": r["reason"]}
                for r in rows
            ]
    
    async def get_scraped_documents(self, task_id):
        """Retrieve all scraped documents for a task"""
        async with self.pool.acquire() as conn:
            rows = await conn.fetch("SELECT url, content, metadata FROM scraped_docs WHERE task_id = $1", task_id)
        
        documents = []
        for row in rows:
            url, content, metadata = row["url"], row["content"], row["metadata"]
            # metadata is likely already a dict, but parse if needed
            if isinstance(metadata, dict):
                metadata_dict = metadata
            else:
                try:
                    metadata_dict = json.loads(metadata)
                except Exception:
                    metadata_dict = {"source": url, "task_id": task_id}
            
            from langchain.docstore.document import Document
            doc = Document(page_content=content, metadata=metadata_dict)
            documents.append(doc)
        return documents
    
    async def store_upload_files_document(self, doc):
        try:
            clean_content = doc.page_content.replace('\x00', '')
            async with self.pool.acquire() as conn:
                await conn.execute(
                    """
                    INSERT INTO upload_files_docs (filename, content, metadata, task_id)
                    VALUES ($1, $2, $3, $4)
                    ON CONFLICT (filename, task_id) DO NOTHING
                    """,
                    doc.metadata['source'], clean_content, json.dumps(doc.metadata), doc.metadata['task_id']
                )
            return True
        except Exception as e:
            logger.error(f"Failed to store upload document in Postgres: {e}")
            return False

    async def get_uploaded_and_failed_counts(self, task_id):
        """
        Returns a dict with counts of status='uploaded' and status='failed' in the scraped_status table for a specific task_id.
        Example: {"uploaded": 10, "failed": 2}
        """
        async with self.pool.acquire() as conn:
            rows = await conn.fetch(
                """
                SELECT status, COUNT(*) as count
                FROM scraped_status
                WHERE status IN ('uploaded', 'failed') AND task_id = $1
                GROUP BY status
                """,
                task_id
            )
        result = {"uploaded": 0, "failed": 0}
        for row in rows:
            if row["status"] == "uploaded":
                result["uploaded"] = row["count"]
            elif row["status"] == "failed":
                result["failed"] = row["count"]
        return result

    async def delete_old_data(self, hours=8):
        """Delete data older than N hours from all tables with a created_at column."""
        tables = [
            'visited_urls',
            'scraped_docs',
            'external_links',
            'website_pdf_status',
            'upload_files_docs',
            'scraped_status',
            'website_pdf_files',
        ]
        
        # Process each table independently to avoid transaction issues
        for table in tables:
            try:
                async with self.pool.acquire() as conn:
                    # Each table gets its own transaction
                    async with conn.transaction():
                        result = await conn.execute(f"""
                            DELETE FROM {table}
                            WHERE created_at < NOW() - INTERVAL '{hours} hours'
                        """)
                        
                        # Extract the number of deleted rows from the result
                        deleted_count = int(result.split()[-1]) if result.split()[-1].isdigit() else 0
                        if deleted_count > 0:
                            logger.info(f"Deleted {deleted_count} old records from {table}")
                    
                    # VACUUM ANALYZE outside of transaction (it cannot run inside)
                    await conn.execute(f"VACUUM ANALYZE {table}")
                    logger.info(f"Vacuumed and analyzed {table}")
                    
            except Exception as e:
                logger.warning(f"Failed to cleanup table {table}: {e}")
                # Continue with next table even if this one failed
                continue
        
        logger.info(f"Completed cleanup of data older than {hours} hours")

# Singleton/global instance for non-ARQ contexts
postgres_handler = PostgresHandler()