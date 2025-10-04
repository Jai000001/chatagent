import hashlib
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

class FileManager:
    def __init__(self):
        pass

    @staticmethod
    async def compute_file_content_hash(content: str) -> str:
        """Async compute SHA-256 hash of normalized content."""
        # Split content into sentences for better duplicate detection
        sentences = content.split('.')
        normalized_sentences = [
            ' '.join(sentence.lower().split())
            for sentence in sentences if sentence.strip()
        ]
        normalized_sentences.sort()
        normalized_content = '.'.join(normalized_sentences)
        return hashlib.sha256(normalized_content.encode('utf-8')).hexdigest() 

    async def is_duplicate_file(self, doc, client_id: str, ttl: int = 8 * 3600) -> bool:
        """
        Async check if a document is a duplicate for a client using Redis set.
        Content hashes expire after the same duration as progress keys (default 8 hours).
        """
        try:
            from app.adapters.database.redisdb_handler import RedisDBHandler
            redis_handler = RedisDBHandler()
            content_hash = await self.compute_file_content_hash(doc.page_content)
            # Fast check in Redis set
            if await redis_handler.is_content_hash_duplicate(client_id, content_hash):
                logger.info(f"Duplicate detected for client_id={client_id}")
                return True
            # Not duplicate, add hash for future checks (with expiry)
            await redis_handler.add_content_hash(client_id, content_hash, ttl=ttl)
            return False
        except Exception as e:
            logger.error(f"Deduplication error: {e}")
            return False

    async def extract_text_from_pdf(self, pdf_content, source_url):
        """Async function to extract text from PDF urls using PyPDF2, offloaded to a thread."""
        import asyncio
        import os
        from io import BytesIO
        import PyPDF2
        from langchain_core.documents import Document
        def sync_extract():
            text = ""
            try:
                pdf_file = BytesIO(pdf_content)
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                num_pages = len(pdf_reader.pages)
                text = "".join(page.extract_text() for page in pdf_reader.pages)
                doc = Document(
                    page_content=text,
                    metadata={
                        "source": os.path.basename(source_url),
                        #"page_count": num_pages
                    }
                )
                return doc, num_pages
            except Exception as e:
                raise Exception(f"Error extracting text from PDF: {str(e)}")
        return await asyncio.to_thread(sync_extract)

    async def update_upload_file_progress(self, task_id, processed_pages, total_pages):
        """ Function to update progress for uploading files (PDF, DOCX, PPTX, TXT, DOC, PPT) """
        from app.adapters.database.redisdb_handler import RedisDBHandler
        redis_handler = RedisDBHandler()
        current_progress = await redis_handler.get_progress_from_store(task_id) or {}
        current_progress["progress"] = int((processed_pages / total_pages) * 70)
        current_progress["uploaded_files_details"] = []
        await redis_handler.set_progress_in_store(task_id, current_progress)
        logger.info(f"Progress for task {task_id}: {current_progress['progress']}%")