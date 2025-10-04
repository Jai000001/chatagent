import uuid
import asyncio
import tiktoken
import re
from typing import List
from urllib.parse import urlparse
import qdrant_client 
from qdrant_client.models import (
    Distance, VectorParams,
    PointStruct, Filter, FieldCondition, MatchValue, MatchAny,
    HnswConfigDiff, OptimizersConfigDiff
)
from app.adapters.database.redisdb_handler import RedisDBHandler
from app.adapters.database.qdrant_collection_sizing import QdrantCollectionSizing
from app.core.app_config import app_config
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

redis_handler = RedisDBHandler()

class QdrantDBHandler:
    def __init__(self):
        self.client = None
        self.collections = {}
        self.collection_lock = asyncio.Lock()
        self.collection_rlock = asyncio.Lock()
        self.reset_timestamps = {}
        self.sizing_manager = QdrantCollectionSizing()
        # Track active bulk operations per collection
        self.active_bulk_operations = {}  # collection_name -> count
        self.bulk_operations_lock = asyncio.Lock()
        
        # Client initialization management
        self._client_initialized = False
        self._initialization_lock = asyncio.Lock()
        self._initialization_task = None

    async def _ensure_client_initialized(self):
        """Ensure the client is initialized before use with proper race condition handling."""
        if self._client_initialized and self.client is not None:
            return
            
        async with self._initialization_lock:
            # Double-check pattern to avoid multiple initializations
            if self._client_initialized and self.client is not None:
                return
                
            try:
                self.client = qdrant_client.AsyncQdrantClient(
                    host=app_config.QDRANT_HOST,
                    port=app_config.QDRANT_PORT,
                    grpc_port=app_config.QDRANT_GRPC_PORT,
                    prefer_grpc=True,
                    timeout=app_config.QDRANT_GRPC_TIMEOUT
                )
                # Test the connection to ensure it's working
                await self.client.get_collections()
                self._client_initialized = True
                logger.info("AsyncQdrant client initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize AsyncQdrant client: {e}")
                self.client = None
                self._client_initialized = False  
                raise 

    async def initialize_client(self):
        """Public method to manually initialize the client."""
        await self._ensure_client_initialized()

    # Context manager support
    async def __aenter__(self):
        """Async context manager entry."""
        await self._ensure_client_initialized()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self.client:
            await self.client.close()
            self.client = None
            self._client_initialized = False    

    @property
    def embedding_function(self):
        """Lazy loading of embedding function"""
        from app.adapters.database.embedding_function import EmbeddingFunction
        if not hasattr(self, '_embedding_function'):
            self._embedding_function = EmbeddingFunction(embedding_model=app_config.EMBEDDING_MODEL)
        return self._embedding_function

    def get_collection_name(self, client_id):
        """Get the collection name for a client"""
        base_name = f"{app_config.QDRANT_COLLECTION_NAME}_client_{client_id}"
        if client_id in self.reset_timestamps:
            return f"{base_name}_{self.reset_timestamps[client_id]}"
        return base_name
    
    async def _start_bulk_operation(self, collection_name):
        """Start a bulk operation - disable indexing if first operation"""
        await self._ensure_client_initialized()
        
        async with self.bulk_operations_lock:
            if collection_name not in self.active_bulk_operations:
                self.active_bulk_operations[collection_name] = 0
            
            # If this is the first bulk operation, disable indexing
            if self.active_bulk_operations[collection_name] == 0:
                try:
                    logger.info(f"Disabling indexing for bulk operation: {collection_name}")
                    await self.client.update_collection(
                        collection_name=collection_name,
                        hnsw_config=HnswConfigDiff(m=0),  # Disable indexing
                        optimizers_config=OptimizersConfigDiff(indexing_threshold=0)
                    )
                except Exception as e:
                    logger.warning(f"Could not disable indexing for {collection_name}: {e}")
            
            # Increment operation count
            self.active_bulk_operations[collection_name] += 1
            current_count = self.active_bulk_operations[collection_name]
            logger.info(f"Started bulk operation for {collection_name}. Active operations: {current_count}")

    async def _end_bulk_operation(self, collection_name):
        """End a bulk operation - restore indexing if last operation"""
        await self._ensure_client_initialized()
        
        async with self.bulk_operations_lock:
            if collection_name not in self.active_bulk_operations:
                logger.warning(f"No active bulk operation found for {collection_name}")
                return
            
            # Decrement operation count
            self.active_bulk_operations[collection_name] -= 1
            current_count = self.active_bulk_operations[collection_name]
            
            # If this was the last bulk operation, restore indexing
            if current_count == 0:
                try:
                    logger.info(f"Restoring indexing after bulk operations: {collection_name}")
                    await self.client.update_collection(
                        collection_name=collection_name,
                        hnsw_config=HnswConfigDiff(
                            m=64,
                            ef_construct=600,
                            full_scan_threshold=10000,
                            max_indexing_threads=2,
                            on_disk=True
                        ),
                        optimizers_config=OptimizersConfigDiff(indexing_threshold=1000)
                    )
                    # Clean up the entry
                    del self.active_bulk_operations[collection_name]
                    logger.info(f"Indexing restored and cleaned up for: {collection_name}")
                except Exception as e:
                    logger.error(f"Failed to restore indexing for {collection_name}: {e}")
            else:
                logger.info(f"Bulk operation ended for {collection_name}. Remaining operations: {current_count}")
    
    async def _create_collection(self, collection_name):
        """Create a new collection with proper client initialization."""
        await self._ensure_client_initialized()
        
        try:
            await self.client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(
                    size=app_config.EMBEDDING_VECTOR_SIZE,
                    distance=Distance.COSINE,
                    on_disk=True
                ),
                hnsw_config=HnswConfigDiff(
                    m=64,
                    ef_construct=600,
                    full_scan_threshold=10000,
                    max_indexing_threads=2,
                    on_disk=True
                ),
                optimizers_config=OptimizersConfigDiff(
                    indexing_threshold=1000,
                    max_optimization_threads=2
                ),
                shard_number=4
            )
            logger.info(f"Created collection: {collection_name}")
        except Exception as e:
            logger.error(f"Failed to create collection {collection_name}: {e}")
            raise  

    async def _collection_exists(self, collection_name):
        """Check if collection exists (async)"""
        await self._ensure_client_initialized()
        
        try:
            collections = (await self.client.get_collections()).collections
            return any(col.name == collection_name for col in collections)
        except Exception as e:
            logger.error(f"Error checking if collection {collection_name} exists: {e}")
            return False     

    async def get_or_create_collection(self, client_id):
        """Get or create a collection for the client (async)"""
        await self._ensure_client_initialized()
        
        async with self.collection_lock:
            collection_name = self.get_collection_name(client_id)
            try:
                # Check if collection exists
                collection_exists = await self._collection_exists(collection_name)
                if collection_exists:
                    logger.info(f"Retrieved existing collection: {collection_name}")
                    return collection_name
                else:
                    await self._create_collection(collection_name)
                    self.collections[client_id] = collection_name
                    logger.info(f"Created new collection: {collection_name}")
                    return collection_name

            except Exception as e:
                logger.error(f"Error in get_or_create_collection for client {client_id}: {e}")
                raise

    def calculate_tokens(self, text: str) -> int:
        """Calculate the number of tokens in a text using tiktoken."""
        encoding = tiktoken.get_encoding("cl100k_base")
        return len(encoding.encode(text))

    def create_token_aware_batches(self, docs, metadatas, ids, max_tokens_per_batch=250000):
        """Create batches based on token count rather than document count"""
        batches = []
        current_batch_docs = []
        current_batch_metadatas = []
        current_batch_ids = []
        current_batch_tokens = 0
        
        for doc, metadata, doc_id in zip(docs, metadatas, ids):
            doc_tokens = self.calculate_tokens(doc)
            
            # If adding this doc would exceed the limit, start a new batch
            if current_batch_tokens + doc_tokens > max_tokens_per_batch and current_batch_docs:
                batches.append((current_batch_docs, current_batch_metadatas, current_batch_ids))
                current_batch_docs = []
                current_batch_metadatas = []
                current_batch_ids = []
                current_batch_tokens = 0
            
            # If single document exceeds limit, split it further
            if doc_tokens > max_tokens_per_batch:
                logger.warning(f"Document with {doc_tokens} tokens exceeds max batch size. Consider splitting further.")
                # You might want to split this document into smaller chunks
                continue
                
            current_batch_docs.append(doc)
            current_batch_metadatas.append(metadata)
            current_batch_ids.append(doc_id)
            current_batch_tokens += doc_tokens
        
        # Add the last batch if it has content
        if current_batch_docs:
            batches.append((current_batch_docs, current_batch_metadatas, current_batch_ids))
        
        return batches

    async def add_documents(self, docs, task_id, client_id, dept_id, url_uuid):
        """Optimized document addition for pre-chunked documents with 256-batch processing"""
        await self._ensure_client_initialized()
        
        collection_name = await self.get_or_create_collection(client_id)

        # Start bulk operation (disables indexing if first operation)
        await self._start_bulk_operation(collection_name)
        
        try:
            total_tokens = 0
            total_docs = len(docs)
            processed_count = 0
            cost_per_1k_tokens = app_config.EMBEDDING_MODEL_RATE_PER_1K_TOKENS

            # Use 256 batch size for optimal performance with pre-chunked documents
            batch_size = min(app_config.QDRANT_UPSERT_BATCH_SIZE, 256)
            logger.info(f"Processing {total_docs} pre-chunked documents with batch size {batch_size}")

            async def _embed_and_upsert_batch(batch_docs, batch_metadatas, batch_ids):
                nonlocal processed_count, total_tokens
                max_retries = 3
                attempt = 0
                cur_batch_docs = batch_docs
                cur_batch_metadatas = batch_metadatas
                cur_batch_ids = batch_ids
                
                while attempt < max_retries:
                    try:
                        # Filter out empty or whitespace-only documents
                        valid_inputs = [
                            (doc_id, doc.strip(), metadata)
                            for doc_id, doc, metadata in zip(cur_batch_ids, cur_batch_docs, cur_batch_metadatas)
                            if doc and doc.strip() and len(doc.strip()) > 10  # Minimum meaningful content
                        ]
                        
                        if not valid_inputs:
                            logger.warning(f"No valid documents to embed in current batch. Skipping.")
                            return
                        
                        cur_batch_ids, cur_batch_docs, cur_batch_metadatas = map(list, zip(*valid_inputs))
                        
                        if not isinstance(cur_batch_docs, list):
                            logger.error(f"batch_docs is not a list! Got type: {type(cur_batch_docs)}")
                            return

                        # Get the embedding function instance (no longer needs await)
                        embedding_func = self.embedding_function
                        
                        # For pre-chunked documents, token checking is more predictable
                        if hasattr(embedding_func, 'count_tokens'):
                            batch_tokens = sum(embedding_func.count_tokens(doc) for doc in cur_batch_docs)
                            logger.info(f"Batch {len(cur_batch_docs)} pre-chunked docs with {batch_tokens} tokens")
                            
                            # Only split if we significantly exceed the limit (rare with pre-chunking)
                            if batch_tokens > 280000:  # Higher threshold since docs are pre-chunked
                                logger.warning(f"Exceptionally large batch ({batch_tokens} tokens), splitting by count...")
                                # Calculate how many docs to keep based on average token size
                                avg_tokens_per_doc = batch_tokens / len(cur_batch_docs)
                                max_docs = int(250000 / avg_tokens_per_doc)
                                new_size = max(max_docs, 32)  # Keep at least 32 docs
                                
                                cur_batch_docs = cur_batch_docs[:new_size]
                                cur_batch_metadatas = cur_batch_metadatas[:new_size]
                                cur_batch_ids = cur_batch_ids[:new_size]
                                logger.info(f"Reduced batch to {new_size} documents")
                        
                        # Perform embedding - handle both async and sync embedding functions
                        try:
                            # First try the async version if available
                            if hasattr(embedding_func, 'aembed_documents'):
                                embeddings = await embedding_func.aembed_documents(cur_batch_docs)
                            # Then try the sync version
                            elif hasattr(embedding_func, 'embed_documents'):
                                loop = asyncio.get_event_loop()
                                embeddings = await loop.run_in_executor(
                                    None, 
                                    embedding_func.embed_documents, 
                                    cur_batch_docs
                                )
                            # If it's a callable, handle it appropriately
                            elif callable(embedding_func):
                                if asyncio.iscoroutinefunction(embedding_func):
                                    embeddings = await embedding_func(cur_batch_docs)
                                else:
                                    # For sync callables, run in executor
                                    loop = asyncio.get_event_loop()
                                    if asyncio.iscoroutinefunction(embedding_func.__call__):
                                        # If it's an instance with async __call__, await it directly
                                        embeddings = await embedding_func(cur_batch_docs)
                                    else:
                                        # For regular sync callables, use run_in_executor
                                        embeddings = await loop.run_in_executor(
                                            None, 
                                            embedding_func, 
                                            cur_batch_docs
                                        )
                            else:
                                raise ValueError("No valid embedding function found")
                        except Exception as e:
                            logger.error(f"Error in embedding function: {e}")
                            raise
                        
                        # Validate embeddings
                        if not embeddings:
                            logger.error("Embedding function returned no vectors. Check embedding function logs.")
                            if len(cur_batch_docs) > 64:  # Try smaller batch for pre-chunked docs
                                logger.info("Retrying with half batch size...")
                                mid = len(cur_batch_docs) // 2
                                cur_batch_docs = cur_batch_docs[:mid]
                                cur_batch_metadatas = cur_batch_metadatas[:mid]
                                cur_batch_ids = cur_batch_ids[:mid]
                                attempt += 1
                                continue
                            else:
                                logger.error("Batch failed embedding, skipping...")
                                return
                        
                        if len(embeddings) != len(cur_batch_docs):
                            logger.error(f"Embedding count mismatch: expected {len(cur_batch_docs)}, got {len(embeddings)}")
                            # Handle partial embeddings
                            if len(embeddings) > 0 and len(embeddings) < len(cur_batch_docs):
                                logger.warning(f"Using first {len(embeddings)} successfully embedded documents")
                                cur_batch_docs = cur_batch_docs[:len(embeddings)]
                                cur_batch_metadatas = cur_batch_metadatas[:len(embeddings)]
                                cur_batch_ids = cur_batch_ids[:len(embeddings)]
                            else:
                                logger.error("Cannot recover from embedding mismatch, skipping batch")
                                return
                        
                        # Create points for Qdrant
                        points = [
                            PointStruct(id=doc_id, vector=embedding,
                                        payload={"document": doc, **metadata})
                            for doc_id, doc, metadata, embedding in zip(cur_batch_ids, cur_batch_docs, cur_batch_metadatas, embeddings)
                        ]

                        # Upsert to Qdrant
                        try:
                            await self.client.upsert(
                                collection_name=collection_name,
                                points=points,
                                wait=False
                            )
                            
                            # Success: update counters and report progress
                            processed_count += len(cur_batch_docs)
                            batch_tokens = sum(
                                embedding_func.calculate_tokens(doc) if hasattr(embedding_func, 'calculate_tokens') 
                                else self.calculate_tokens(doc) 
                                for doc in cur_batch_docs
                            )
                            total_tokens += batch_tokens
                            
                            # Report progress more frequently for better UX
                            progress_percentage = min(100, int((processed_count / total_docs) * 100))
                            await self._report_progress(task_id, processed_count, total_docs, total_tokens, cost_per_1k_tokens, progress_percentage)
                            
                            logger.info(f"Successfully processed batch: {len(cur_batch_docs)} docs, {batch_tokens} tokens ({progress_percentage}% complete)")
                            return  # Exit after successful upsert
                            
                        except Exception as upsert_exc:
                            # Handle Qdrant-specific errors
                            err_str = str(upsert_exc)
                            if ("DEADLINE_EXCEEDED" in err_str or "timeout" in err_str.lower()):
                                if len(cur_batch_docs) > 32:  # Only split if batch is reasonably large
                                    logger.warning(f"Qdrant upsert timeout for batch of {len(cur_batch_docs)} docs (attempt {attempt+1}). Retrying with smaller batch.")
                                    await asyncio.sleep(min(2 ** attempt, 10))  # Max 10 sec backoff
                                    mid = len(cur_batch_docs) // 2
                                    cur_batch_docs = cur_batch_docs[:mid]
                                    cur_batch_metadatas = cur_batch_metadatas[:mid]
                                    cur_batch_ids = cur_batch_ids[:mid]
                                    attempt += 1
                                    continue
                                else:
                                    logger.error(f"Small batch still timing out, giving up: {upsert_exc}")
                                    return
                            else:
                                logger.error(f"Qdrant upsert failed for batch (attempt {attempt+1}): {upsert_exc}")
                                attempt += 1
                                if attempt == max_retries:
                                    logger.error(f"Giving up on batch after {max_retries} attempts.")
                                    return
                                await asyncio.sleep(min(attempt * 2, 10))  # Progressive backoff
                                continue
                                
                    except Exception as e:
                        logger.error(f"Batch processing failed (attempt {attempt+1}) for task {task_id}: {e}")
                        attempt += 1
                        if attempt == max_retries:
                            logger.error(f"Giving up on batch after {max_retries} attempts: {e}")
                            return
                        await asyncio.sleep(min(attempt, 5))

            # Pre-allocate document lists
            all_docs = []
            all_metadatas = []
            all_ids = []
            
            # Prepare all documents with content cleaning
            for doc in docs:
                doc.metadata['client_id'] = client_id
                doc.metadata['dept_id'] = dept_id
                doc.metadata['url_uuid'] = url_uuid

                # Clean content (documents are already chunked appropriately)
                clean_content = doc.page_content.replace('\x00', '').strip()
                
                # Skip documents that are too short (but be less strict since they're pre-chunked)
                if len(clean_content) < 5:
                    logger.debug("Skipping empty document chunk")
                    continue
                    
                all_docs.append(clean_content)
                all_metadatas.append(doc.metadata)
                all_ids.append(str(uuid.uuid4()))

            if not all_docs:
                logger.warning("No valid documents to process after filtering")
                await self._report_progress(task_id, 0, 0, 0, cost_per_1k_tokens, 100)
                return {"task_id": task_id, "message": "No valid documents found"}

            logger.info(f"Processing {len(all_docs)} pre-chunked documents in batches of up to {batch_size}")

            # Process in batches with optimized concurrency for 256-sized batches
            tasks = []
            max_concurrent_batches = 8  # Higher concurrency for pre-chunked documents
            
            for i in range(0, len(all_docs), batch_size):
                batch_docs = all_docs[i:i + batch_size]
                batch_metadatas = all_metadatas[i:i + batch_size]
                batch_ids = all_ids[i:i + batch_size]
                
                task = _embed_and_upsert_batch(batch_docs, batch_metadatas, batch_ids)
                tasks.append(task)
                
                # Process in groups to manage concurrency
                if len(tasks) >= max_concurrent_batches:
                    await asyncio.gather(*tasks, return_exceptions=True)  # Don't fail on single batch errors
                    tasks = []

            # Process remaining tasks
            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)

            # Update cache asynchronously after successful upload
            if processed_count > 0:
                await self.sizing_manager.update_collection_cache_async(
                    collection_name, 
                    self.client
                )

            # Final progress update
            final_progress = {
                "progress": 100,
                "total_tokens": total_tokens,
                "total_cost": self.calculate_total_cost(total_tokens, cost_per_1k_tokens),
                "processed_docs": processed_count,
                "total_docs": total_docs
            }
            
            await redis_handler.set_progress_in_store(task_id, final_progress)

            success_rate = (processed_count / total_docs * 100) if total_docs > 0 else 0
            success_message = f"Successfully added {processed_count}/{total_docs} documents ({success_rate:.1f}% success rate)"
            logger.info(f"{success_message} for task_id={task_id}")
            return {"task_id": task_id, "message": success_message}

        except Exception as e:
            logger.error(f"Failed during document upload for task_id={task_id}: {e}")
            error_progress = {
                "progress": 100,
                "total_tokens": total_tokens,
                "total_cost": self.calculate_total_cost(total_tokens, cost_per_1k_tokens),
                "error": str(e),
                "processed_docs": processed_count,
                "total_docs": total_docs
            }
            await redis_handler.set_progress_in_store(task_id, error_progress)
            return {"task_id": task_id, "message": f"Upload failed: {str(e)}"}
            
        finally:
            # Always end bulk operation (restores indexing if last operation)
            await self._end_bulk_operation(collection_name)

    def calculate_total_cost(self, total_tokens, cost_per_1k_tokens):
        cost = round((total_tokens / 1000) * cost_per_1k_tokens, 6)
        return f"{cost:.6f}"

    async def _report_progress(self, task_id, processed_count, total_docs, total_tokens, cost_per_1k_tokens, progress_percentage=None):
        """Enhanced progress reporting with better error handling"""
        try:
            from datetime import datetime
            from app.adapters.database.redisdb_handler import RedisDBHandler
            redis_handler = RedisDBHandler()
            
            # Calculate progress if not provided
            if progress_percentage is None:
                progress_percentage = min(100, int((processed_count / total_docs) * 100)) if total_docs > 0 else 0
            
            progress_data = {
                "progress": progress_percentage,
                "processed_docs": processed_count,
                "total_docs": total_docs,
                "total_tokens": total_tokens,
                "total_cost": round((total_tokens / 1000) * cost_per_1k_tokens, 6)
            }
            
            await redis_handler.set_progress_in_store(task_id, progress_data)
            
        except Exception as e:
            logger.error(f"Failed to report progress for task {task_id}: {e}")
            # Don't fail the entire operation due to progress reporting issues
                
    async def query_documents(self, query_text, client_id, dept_id):
        """Query documents from Qdrant collection with cached dynamic sizing (async)"""
        await self._ensure_client_initialized()
        
        collection_name = await self.get_or_create_collection(client_id)
        try:
            # Get cached collection info (very fast)
            sizing_info = await self.sizing_manager.get_cached_collection_info(collection_name, self.client)
            
            # Get the embedding function instance
            embedding_func = self.embedding_function
            
            # Generate query embedding
            if hasattr(embedding_func, 'aembed_documents'):
                # If it has an async embed method, use that
                query_embedding = (await embedding_func.aembed_documents([query_text]))[0]

            elif hasattr(embedding_func, 'embed_documents'):
                # If it has a sync embed method, run it in an executor
                loop = asyncio.get_event_loop()
                query_embedding = (await loop.run_in_executor(
                    None, 
                    embedding_func.embed_documents, 
                    [query_text]
                ))[0]
            elif callable(embedding_func):
                if asyncio.iscoroutinefunction(embedding_func.__call__):
                    query_embedding = (await embedding_func([query_text]))[0]
                else:
                    loop = asyncio.get_event_loop()
                    query_embedding = (await loop.run_in_executor(
                        None, 
                        embedding_func, 
                        [query_text]
                    ))[0]
            else:
                raise ValueError("No valid embedding function available")
            # Search in Qdrant with dynamic parameters
            search_result = await self.client.search(
                collection_name=collection_name,
                query_vector=query_embedding,
                limit=sizing_info['search_limit'],
                with_payload=True,
                score_threshold=sizing_info['score_threshold'],
                search_params={
                    "hnsw_ef": min(200, max(50, sizing_info.get('point_count', 10000) // 100))
                },
            )
            documents = []
            metadatas = []
            distances = []
            
            for point in search_result:
                documents.append(point.payload.get('document', ''))
                
                # Extract metadata (exclude the document field)
                metadata = {k: v for k, v in point.payload.items() if k != 'document'}
                metadatas.append(metadata)
                
                # Convert score to distance
                distances.append(1.0 - point.score)

            logger.info(f"Retrieved {len(documents)} documents with collection size: {sizing_info['category']}")

            return {
                'documents': documents,
                'metadatas': metadatas,
                'distances': distances,
                'collection_info': sizing_info
            }

        except Exception as e:
            logger.error(f"Exception while querying document: {e}")
            return {
                'documents': [], 
                'metadatas': [], 
                'distances': [], 
                'collection_info': {'context_window': 4096, 'category': 'small'}
            }

    async def reset_collection(self, client_id):
        """Reset collection by deleting and recreating it (async)"""
        await self._ensure_client_initialized()
        
        async with self.collection_lock:
            try:
                # Get all collections
                collections = (await self.client.get_collections()).collections
                
                # Find and delete collections for this client
                for collection in collections:
                    if collection.name.startswith(f"{app_config.QDRANT_COLLECTION_NAME}_client_{client_id}"):
                        try:
                            # Invalidate cache before reset
                            await self.sizing_manager.invalidate_cache(collection.name)
                            await self.client.delete_collection(collection.name)
                            logger.info(f"Deleted collection: {collection.name}")
                        except Exception as e:
                            logger.warning(f"Error deleting collection {collection.name}: {e}")

                # Create new collection
                new_collection_name = f"{app_config.QDRANT_COLLECTION_NAME}_client_{client_id}"
                for attempt in range(3):
                    try:
                        await self._create_collection(new_collection_name)
                        self.collections[client_id] = new_collection_name
                        logger.info(f"Created new collection: {new_collection_name}")
                        
                        # Remove reset timestamp
                        if client_id in self.reset_timestamps:
                            del self.reset_timestamps[client_id]
                        
                        # After successful reset, update cache asynchronously
                        await self.sizing_manager.update_collection_cache_async(new_collection_name, self.client)

                        return new_collection_name
                        
                    except Exception as e:
                        logger.error(f"Attempt {attempt + 1} - Failed to create collection: {e}")
                        if attempt == 2:
                            raise
                        await asyncio.sleep(1)

            except Exception as e:
                logger.error(f"Exception while resetting collection: {e}")
                raise

    async def get_collection_data(self, client_id, dept_id=None):
        """Get collection data using offset-based pagination (async)"""
        await self._ensure_client_initialized()
        
        try:
            collection_name = self.get_collection_name(client_id)

            # Check if collection exists
            if not await self._collection_exists(collection_name):
                logger.warning(f"Collection {collection_name} for client {client_id} does not exist")
                return None
            
            # Build filter conditions
            filter_conditions = [
                FieldCondition(key="client_id", match=MatchValue(value=client_id))
            ]
            
            # Add dept_id filter if provided
            if dept_id:
                filter_conditions.append(FieldCondition(key="dept_id", match=MatchValue(value=dept_id)))

            scroll_filter = Filter(must=filter_conditions)

            offset = None
            batch_size = 1000
            all_metadatas = []

            while True:
                points, next_page_offset = await self.client.scroll(
                    collection_name=collection_name,
                    limit=batch_size,
                    offset=offset,
                    scroll_filter=scroll_filter,
                    with_payload=True,
                    with_vectors=False
                )
                for point in points:
                    metadata = point.payload
                    all_metadatas.append(metadata)

                offset = next_page_offset  # Important: Update offset from Qdrant response
                if offset is None:
                    break

            result = {
                'metadatas': all_metadatas,
            }

            logger.info(f"Successfully fetched {len(all_metadatas)} points from collection: {collection_name}")
            return result

        except Exception as e:
            logger.error(f"Exception while fetching collection data for client {client_id}: {e}")
            return None

    async def stream_qdrant_collection_data(self, client_id, dept_id=None):
        """Async generator to stream Qdrant collection data in batches."""
        import json
        await self._ensure_client_initialized()
        try:
            collection_name = self.get_collection_name(client_id)

            if not await self._collection_exists(collection_name):
                logger.warning(f"Collection {collection_name} for client {client_id} does not exist")
                yield json.dumps({"error": "Collection does not exist"}) + "\n"
                return

            # Build filter
            filter_conditions = [
                FieldCondition(key="client_id", match=MatchValue(value=client_id))
            ]
            if dept_id:
                filter_conditions.append(FieldCondition(key="dept_id", match=MatchValue(value=dept_id)))

            scroll_filter = Filter(must=filter_conditions)

            offset = None
            batch_size=1000

            while True:
                points, next_page_offset = await self.client.scroll(
                    collection_name=collection_name,
                    limit=batch_size,
                    offset=offset,
                    scroll_filter=scroll_filter,
                    with_payload=True,
                    with_vectors=False
                )

                if not points:
                    break

                for point in points:
                    # Assuming document text is stored in payload as 'document' field
                    yield json.dumps({
                        "metadata": point.payload,
                        "document": point.payload.get("document")  # adjust key if different
                    }, ensure_ascii=False) + "\n"

                offset = next_page_offset
                if offset is None:
                    break

        except Exception as e:
            logger.error(f"Exception while streaming collection data for client {client_id}: {e}")
            yield json.dumps({"error": str(e)}) + "\n"

    async def delete_documents_by_source(self, source_names, client_id, dept_id):
        """Delete documents by source names (async)"""
        await self._ensure_client_initialized()
        
        collection_name = self.get_collection_name(client_id)
        temp_collection_name = f"{collection_name}_temp"
    
        try:
            # Handle batch deletion for large source lists
            BATCH_SIZE = 1000
            if isinstance(source_names, list) and len(source_names) > BATCH_SIZE:
                for i in range(0, len(source_names), BATCH_SIZE):
                    batch = source_names[i:i + BATCH_SIZE]
                    await self._delete_by_source_batch(collection_name, batch, client_id, dept_id)
                    await self.sizing_manager.invalidate_cache(collection_name)
                    await self.sizing_manager.update_collection_cache_async(collection_name, self.client) 
    
                    if await self._collection_exists(temp_collection_name) and await self._collection_has_data(temp_collection_name, source_names):
                        await self._delete_by_source_batch(temp_collection_name, batch, client_id, dept_id)
                        await self.sizing_manager.invalidate_cache(temp_collection_name)
                        await self.sizing_manager.update_collection_cache_async(temp_collection_name, self.client)
            else:
                await self._delete_by_source_batch(collection_name, source_names, client_id, dept_id)
                await self.sizing_manager.invalidate_cache(collection_name)
                await self.sizing_manager.update_collection_cache_async(collection_name, self.client) 
    
                if await self._collection_exists(temp_collection_name) and await self._collection_has_data(temp_collection_name, source_names):
                    await self._delete_by_source_batch(temp_collection_name, source_names, client_id, dept_id)
                    await self.sizing_manager.invalidate_cache(temp_collection_name)
                    await self.sizing_manager.update_collection_cache_async(temp_collection_name, self.client)
    
        except Exception as e:
            logger.error(f"An error occurred while deleting documents: {e}")
    
    async def _delete_by_source_batch(self, collection_name, source_names, client_id, dept_id):
        """Helper method to delete documents by source in batches (async)"""
        await self._ensure_client_initialized()
        
        filter_conditions = Filter(
            must=[
                FieldCondition(key="client_id", match=MatchValue(value=client_id)),
                FieldCondition(key="dept_id", match=MatchValue(value=dept_id)),
                FieldCondition(
                    key="source",
                    match=MatchAny(any=source_names) if isinstance(source_names, list) else MatchValue(value=source_names)
                )
            ]
        )
    
        await self.client.delete(
            collection_name=collection_name,
            points_selector=filter_conditions
        )

    async def delete_documents_by_url_pattern(self, source_name, url_pattern, client_id, dept_id, url_uuid=None):
        """Delete documents by URL pattern using offset-based pagination (async)"""
        await self._ensure_client_initialized()
        
        collection_name = self.get_collection_name(client_id)
        temp_collection_name = f"{collection_name}_temp"

        try:
            async def get_matching_document_ids_with_offset(collection_name, url_pattern, client_id, dept_id, url_uuid):
                matching_ids = []
                offset = None
                batch_size = 1000

                # Build filter conditions
                filter_conditions = [
                    FieldCondition(key="client_id", match=MatchValue(value=client_id)),
                    FieldCondition(key="dept_id", match=MatchValue(value=dept_id))
                ]
                
                if url_uuid is not None:
                    filter_conditions.append(
                        FieldCondition(key="url_uuid", match=MatchValue(value=url_uuid))
                    )

                scroll_filter = Filter(must=filter_conditions)

                while True:
                    points, next_page_offset = await self.client.scroll(
                        collection_name=collection_name,
                        limit=batch_size,
                        offset=offset,
                        with_payload=True,
                        scroll_filter=scroll_filter  # DATABASE-LEVEL FILTERING!
                    )
                    if not points:
                        break

                    # Now only filter by URL pattern (much smaller dataset)
                    for point in points:
                        payload = point.payload
                        if 'source' in payload and url_pattern.match(payload['source']):
                            matching_ids.append(str(point.id))

                    offset = next_page_offset  # Important: Update offset from Qdrant response
                    if offset is None:
                        break

                return matching_ids

            # Get documents to delete from main collection
            documents_to_delete = await get_matching_document_ids_with_offset(
                collection_name, url_pattern, client_id, dept_id, url_uuid
            )

            # Check and process temp collection
            temp_documents_to_delete = []
            if await self._collection_exists(temp_collection_name) and await self._collection_has_data(temp_collection_name, source_name):
                temp_documents_to_delete = await get_matching_document_ids_with_offset(
                    temp_collection_name, url_pattern, client_id, dept_id, url_uuid
                )

            # Perform batched deletions
            BATCH_SIZE = 1000

            for i in range(0, len(documents_to_delete), BATCH_SIZE):
                batch = documents_to_delete[i:i + BATCH_SIZE]
                await self.client.delete(
                    collection_name=collection_name,
                    points_selector=batch
                )

            # Invalidate cache after deletion
            await self.sizing_manager.invalidate_cache(collection_name)
        
            # Update cache asynchronously
            await self.sizing_manager.update_collection_cache_async(collection_name, self.client)    

            for i in range(0, len(temp_documents_to_delete), BATCH_SIZE):
                batch = temp_documents_to_delete[i:i + BATCH_SIZE]
                await self.client.delete(
                    collection_name=temp_collection_name,
                    points_selector=batch
                )

            if temp_documents_to_delete:
                # Invalidate cache after deletion
                await self.sizing_manager.invalidate_cache(temp_collection_name)
            
                # Update cache asynchronously
                await self.sizing_manager.update_collection_cache_async(temp_collection_name, self.client)      

            total_deleted = len(documents_to_delete) + len(temp_documents_to_delete)
            if total_deleted > 0:
                logger.info(f"Deleted {len(documents_to_delete)} documents from {collection_name} and {len(temp_documents_to_delete)} documents from {temp_collection_name}")
            else:
                logger.info("No documents matched the deletion criteria.")

        except Exception as e:
            logger.error(f"An error occurred while deleting documents: {e}")

    async def _collection_has_data(self, collection_name, source_name):
        """Check if collection has data for the given source_name (async)"""
        await self._ensure_client_initialized()
        
        try:
            if source_name.startswith(('http://', 'https://')):
                domain = urlparse(source_name).netloc
                # Use a filter with OR condition (should)
                scroll_filter = Filter(
                    should=[
                        FieldCondition(
                            key="source",
                            match=MatchValue(value=source_name)
                        ),
                        FieldCondition(
                            key="source",
                            match=MatchValue(value=domain)
                        )
                    ]
                )
            else:
                # For non-URL sources, just exact match
                scroll_filter = Filter(
                    must=[
                        FieldCondition(
                            key="source",
                            match=MatchValue(value=source_name)
                        )
                    ]
                )

            points, next_page_offset = await self.client.scroll(
                collection_name=collection_name,
                limit=1,
                with_payload=False,
                scroll_filter=scroll_filter
            )
            return len(points) > 0
        except Exception as e:
            logger.error(f"Error checking data for source '{source_name}' in collection '{collection_name}': {e}")
            return False

    async def get_collection_size_mb(self, source_name, client_id, dept_id):
        """Calculate collection size in MB for a specific source using offset-based pagination (async)"""
        await self._ensure_client_initialized()
        
        try:
            collection_name = self.get_collection_name(client_id)
    
            # Use scroll_filter for client_id and dept_id
            scroll_filter = Filter(must=[
                FieldCondition(key="client_id", match=MatchValue(value=client_id)),
                FieldCondition(key="dept_id", match=MatchValue(value=dept_id))
            ])
    
            offset = None
            batch_size = 1000
            total_size_bytes = 0
            matching_docs = []
    
            # If URL, compile regex
            if source_name.startswith(('http://', 'https://')):
                parsed_url = urlparse(source_name)
                main_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
                url_pattern = re.compile(f"^{re.escape(main_url)}(/.*)?$")
            else:
                url_pattern = None
    
            while True:
                points, next_page_offset = await self.client.scroll(
                    collection_name=collection_name,
                    limit=batch_size,
                    offset=offset,
                    with_payload=True,
                    scroll_filter=scroll_filter  # DATABASE-LEVEL FILTERING!
                )
                if not points:
                    break
    
                # Now only filter by source (much smaller dataset)
                for point in points:
                    payload = point.payload
                    source = payload.get('source')
                    if not source:
                        continue
    
                    if url_pattern:
                        if url_pattern.match(source):
                            matching_docs.append(payload.get('document', ''))
                    else:
                        if source == source_name:
                            matching_docs.append(payload.get('document', ''))
    
                offset = next_page_offset
                if offset is None:
                    break

            # Calculate size
            for doc in matching_docs:
                total_size_bytes += len(doc.encode('utf-8'))

            total_size_mb = total_size_bytes / (1024 * 1024)

            return round(total_size_mb, 6)

        except Exception as e:
            logger.error(f"Exception while calculating collection size for source {source_name}: {e}")
            return 0

    async def update_client_id(self, client_id, source_names, action, dept_id, url_uuid=None):
        """Update client ID for specific sources using offset-based pagination"""
        await self._ensure_client_initialized()
        
        try:
            BATCH_SIZE = 1000
            collection_name = self.get_collection_name(client_id)

            # Ensure source_names is a list
            if isinstance(source_names, str):
                source_names = [source_names]

            # Determine search and update parameters
            if action == 'inactive':
                search_client_id = client_id
                new_client_id = 'inactive'
            elif action == 'active':
                search_client_id = 'inactive'
                new_client_id = client_id
            else:
                raise ValueError(f"Invalid action: {action}")
            
            # Build base filter
            filter_conditions = [
                FieldCondition(key="client_id", match=MatchValue(value=search_client_id)),
                FieldCondition(key="dept_id", match=MatchValue(value=dept_id))
            ]
            
            if url_uuid:
                filter_conditions.append(
                    FieldCondition(key="url_uuid", match=MatchValue(value=url_uuid))
                )

            scroll_filter = Filter(must=filter_conditions)

            offset = None
            points_to_update = []

            while True:
                points, next_page_offset = await self.client.scroll(
                    collection_name=collection_name,
                    limit=BATCH_SIZE,
                    offset=offset,
                    with_payload=True,
                    with_vectors=True,
                    scroll_filter=scroll_filter  # DATABASE-LEVEL FILTERING!
                )
                if not points:
                    break

                # Now only filter by source (much smaller dataset)
                for source in source_names:
                    for point in points:
                        payload = point.payload
                        if 'source' not in payload:
                            continue

                        matches = False
                        if source.startswith(('http://', 'https://')):
                            parsed_url = urlparse(source)
                            main_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
                            url_pattern = re.compile(f"^{re.escape(main_url)}(/.*)?$")
                            matches = url_pattern.match(payload['source']) is not None
                        else:
                            matches = (payload['source'] == source)

                        if matches:
                            new_payload = payload.copy()
                            new_payload['client_id'] = new_client_id
                            points_to_update.append(PointStruct(
                                id=point.id,
                                vector=point.vector,
                                payload=new_payload
                            ))

                offset = next_page_offset
                if offset is None:
                    break

            # Perform batched updates
            total_updated = 0
            for i in range(0, len(points_to_update), BATCH_SIZE):
                batch = points_to_update[i:i + BATCH_SIZE]
                try:
                    await self.client.upsert(
                        collection_name=collection_name,
                        points=batch
                    )
                    total_updated += len(batch)
                except Exception as batch_error:
                    logger.error(f"Error updating batch {i//BATCH_SIZE + 1}: {batch_error}")
                    continue

            if total_updated > 0:
                # Invalidate cache after updates
                await self.sizing_manager.invalidate_cache(collection_name)
                # Update cache asynchronously
                await self.sizing_manager.update_collection_cache_async(collection_name, self.client)
                logger.info(f"Successfully {action}d {total_updated} documents for client '{client_id}' with sources: {source_names}")
            else:
                logger.info(f"No documents matched for client '{client_id}' and sources: {source_names}")

            return total_updated

        except Exception as e:
            logger.error(f"Error in update_client_id: {e}")
            raise

    async def move_sources_to_temp(self, source_names, client_id, dept_id, url_uuid):
        """Move documents to temp collection using offset-based pagination"""
        await self._ensure_client_initialized()
        
        moved_count = 0
        batch_size = 1000  # Tune as needed
        try:
            current_collection_name = self.get_collection_name(client_id)
            temp_collection_name = f"{current_collection_name}_temp"

            # Create temp collection if it doesn't exist
            if not await self._collection_exists(temp_collection_name):
                await self._create_collection(temp_collection_name)

            # Build base filter
            filter_conditions = [
                FieldCondition(key="client_id", match=MatchValue(value=client_id)),
                FieldCondition(key="dept_id", match=MatchValue(value=dept_id))
            ]
            
            if url_uuid:
                filter_conditions.append(
                    FieldCondition(key="url_uuid", match=MatchValue(value=url_uuid))
                )
            else:
                filter_conditions.append(
                    FieldCondition(key="url_uuid", match=MatchValue(value=""))
                )

            scroll_filter = Filter(must=filter_conditions)    

            offset = None
            points_to_move = []
            points_to_delete = []

            while True:
                points, next_page_offset = await self.client.scroll(
                    collection_name=current_collection_name,
                    limit=batch_size,
                    offset=offset,
                    with_payload=True,
                    with_vectors=True,
                    scroll_filter=scroll_filter  # DATABASE-LEVEL FILTERING!
                )
                if not points:
                    break

                # Now only filter by source (much smaller dataset)
                for source_name in source_names:
                    for point in points:
                        payload = point.payload
                        matches = False
                        
                        if source_name.startswith(('http://', 'https://')):
                            parsed_url = urlparse(source_name)
                            main_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
                            url_pattern = re.compile(f"^{re.escape(main_url)}(/.*)?$")
                            matches = ('source' in payload and url_pattern.match(payload['source']))
                        else:
                            matches = (payload.get('source') == source_name)

                        if matches:
                            points_to_move.append(point)
                            points_to_delete.append(point.id)

                offset = next_page_offset
                if offset is None:
                    break

            # Move matched points in batches
            for i in range(0, len(points_to_move), batch_size):
                batch_points = points_to_move[i:i + batch_size]
                batch_ids = points_to_delete[i:i + batch_size]

                qdrant_points = [
                    PointStruct(id=point.id, vector=point.vector, payload=point.payload)
                    for point in batch_points
                ]

                await self.client.upsert(
                    collection_name=temp_collection_name,
                    points=qdrant_points
                )
                await self.client.delete(
                    collection_name=current_collection_name,
                    points_selector=batch_ids
                )

                moved_count += len(batch_points)

            # ADD: Cache management after successful moves
            if moved_count > 0:
                # Invalidate and update cache for both collections
                await self.sizing_manager.invalidate_cache(current_collection_name)
                await self.sizing_manager.update_collection_cache_async(current_collection_name, self.client)
                
                await self.sizing_manager.invalidate_cache(temp_collection_name)
                await self.sizing_manager.update_collection_cache_async(temp_collection_name, self.client)

            logger.info(f"Moved {moved_count} documents to temp collection for sources: {source_names}")
            return moved_count

        except Exception as e:
            logger.error(f"Error moving sources to temp collection: {e}")
            return 0
        
    async def move_sources_from_temp(self, source_names, client_id, dept_id, url_uuid):
        """
        Move documents from temp collection back to current collection using offset-based pagination
        """
        await self._ensure_client_initialized()
        
        moved_count = 0
        batch_size = 1000  # Tune for performance
        name = f"{client_id}_temp"
        temp_collection_name = self.get_collection_name(name)
        current_collection_name = self.get_collection_name(client_id)

        try:
            # Check if temp collection exists
            if not await self._collection_exists(temp_collection_name):
                logger.warning(f"Temp collection {temp_collection_name} not found")
                return 0
            
            # Build base filter conditions for database-level filtering
            filter_conditions = [
                FieldCondition(key="client_id", match=MatchValue(value=client_id)),
                FieldCondition(key="dept_id", match=MatchValue(value=dept_id))
            ]
            
            # Add url_uuid filter based on whether it's provided
            if url_uuid:
                filter_conditions.append(
                    FieldCondition(key="url_uuid", match=MatchValue(value=url_uuid))
                )
            else:
                # Filter for documents with empty url_uuid
                filter_conditions.append(
                    FieldCondition(key="url_uuid", match=MatchValue(value=""))
                )

            scroll_filter = Filter(must=filter_conditions)

            offset = None

            while True:
                # Fetch batch using offset
                points, next_page_offset = await self.client.scroll(
                    collection_name=temp_collection_name,
                    limit=batch_size,
                    offset=offset,
                    with_payload=True,
                    with_vectors=True,
                    scroll_filter=scroll_filter  # DATABASE-LEVEL FILTERING!
                )
                if not points:
                    break

                points_to_move = []
                points_to_delete = []

                # Now only filter by source (much smaller dataset after database filtering)
                for source_name in source_names:
                    for point in points:
                        payload = point.payload
                        matches = False

                        if source_name.startswith(('http://', 'https://')):
                            parsed_url = urlparse(source_name)
                            main_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
                            url_pattern = re.compile(f"^{re.escape(main_url)}(/.*)?$")
                            matches = ('source' in payload and url_pattern.match(payload['source']))
                        else:
                            matches = (payload.get('source') == source_name)

                        if matches and point not in points_to_move:
                            points_to_move.append(point)
                            points_to_delete.append(point.id)

                # Move documents in batches
                for i in range(0, len(points_to_move), batch_size):
                    batch_points = points_to_move[i:i + batch_size]
                    batch_ids = points_to_delete[i:i + batch_size]

                    qdrant_points = [
                        PointStruct(id=point.id, vector=point.vector, payload=point.payload)
                        for point in batch_points
                    ]

                    # Add back to current collection
                    await self.client.upsert(
                        collection_name=current_collection_name,
                        points=qdrant_points
                    )

                    # Delete from temp collection
                    await self.client.delete(
                        collection_name=temp_collection_name,
                        points_selector=batch_ids
                    )

                    moved_count += len(batch_points)

                offset = next_page_offset
                if offset is None:
                    break

            # ADD: Cache management after successful moves
            if moved_count > 0:
                # Invalidate and update cache for both collections
                await self.sizing_manager.invalidate_cache(current_collection_name)
                await self.sizing_manager.update_collection_cache_async(current_collection_name, self.client)
                
                await self.sizing_manager.invalidate_cache(temp_collection_name)
                await self.sizing_manager.update_collection_cache_async(temp_collection_name, self.client)
    
            logger.info(f"Moved {moved_count} documents from temp collection for sources: {source_names}")
            return moved_count

        except Exception as e:
            logger.error(f"Error moving sources from temp collection: {e}")
            return 0