from typing import List
from langchain_openai import OpenAIEmbeddings
import os
import tiktoken
from app.core.app_config import app_config
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

os.environ["OPENAI_API_KEY"]=app_config.OPENAI_API_KEY

class EmbeddingFunction():
    def __init__(self, embedding_model):
        self.embedding_function = OpenAIEmbeddings(
            model=embedding_model,
            max_retries=3,
            request_timeout=120  # Increased timeout
        )
        self.model_name = embedding_model
        
        # Initialize tokenizer for accurate token counting
        try:
            self.tokenizer = tiktoken.encoding_for_model(embedding_model)
        except KeyError:
            # Fallback for custom models
            self.tokenizer = tiktoken.get_encoding("cl100k_base")
        
        # Conservative token limits (leave buffer for API overhead)
        self.max_tokens_per_request = 250000  # Below 300k limit
        self.optimal_batch_size = 256  # Optimal batch size for processing
        
        # Since documents are pre-chunked, we expect smaller individual docs
        self.expected_chunk_size = 1000  # Expected size from your chunking

    def count_tokens(self, text: str) -> int:
        """Count tokens in text using the model's tokenizer"""
        try:
            return len(self.tokenizer.encode(text))
        except Exception as e:
            logger.warning(f"Token counting failed, using character estimate: {e}")
            # Fallback: rough estimate (1 token ≈ 4 characters for English)
            return len(text) // 4

    def group_documents_by_tokens(self, documents: List[str], target_batch_size: int = 256) -> List[List[str]]:
        """
        Group pre-chunked documents into batches that respect token limits.
        Since documents are already chunked (1000 tokens + 100 overlap), 
        we just need to group them for efficient API calls.
        """
        if not documents:
            return []

        batches = []
        current_batch = []
        current_tokens = 0
        
        for doc in documents:
            doc_tokens = self.count_tokens(doc)
            
            # Log warning for unexpectedly large documents (shouldn't happen with pre-chunking)
            if doc_tokens > self.max_tokens_per_doc:
                logger.warning(f"Pre-chunked document unexpectedly large: {doc_tokens} tokens. Using as-is.")
            
            # Check if adding this document would exceed the token limit
            if current_tokens + doc_tokens > self.max_tokens_per_request and current_batch:
                # Start a new batch
                batches.append(current_batch)
                current_batch = [doc]
                current_tokens = doc_tokens
            elif len(current_batch) >= target_batch_size and current_batch:
                # Start new batch if we've reached target batch size
                batches.append(current_batch)
                current_batch = [doc]
                current_tokens = doc_tokens
            else:
                # Add to current batch
                current_batch.append(doc)
                current_tokens += doc_tokens
        
        # Add the last batch if it exists
        if current_batch:
            batches.append(current_batch)
        
        # logger.info(f"Grouped {len(documents)} pre-chunked documents into {len(batches)} batches (target: {target_batch_size} docs/batch)")
        return batches

    async def __call__(self, input_docs: List[str]) -> List[List[float]]:
        """
        Process documents with intelligent token-based chunking
        """
        try:
            if not isinstance(input_docs, list):
                logger.error("Input to embedding function is not a list.")
                return []
            
            if not input_docs:
                logger.warning("Empty document list provided to embedding function")
                return []

            # Filter out empty documents
            valid_docs = [doc.strip() for doc in input_docs if doc and doc.strip()]
            if not valid_docs:
                logger.warning("No valid documents after filtering empty ones")
                return []

            # Quick token check for the entire batch
            total_tokens = sum(self.count_tokens(doc) for doc in valid_docs)
            # logger.info(f"Processing {len(valid_docs)} pre-chunked documents with {total_tokens} total tokens")

            # For pre-chunked documents (~1000 tokens each), we can be more aggressive
            # 256 docs * 1000 tokens = ~256k tokens (perfect for API limit)
            if total_tokens <= self.max_tokens_per_request and len(valid_docs) <= 256:
                try:
                    if hasattr(self.embedding_function, 'aembed_documents'):
                        embeddings = await self.embedding_function.aembed_documents(valid_docs)
                    else:
                        embeddings = self.embedding_function.embed_documents(valid_docs)
                    
                    # logger.info(f"Successfully generated {len(embeddings)} embeddings in single batch")
                    return embeddings
                except Exception as e:
                    if "max_tokens_per_request" in str(e):
                        logger.warning("Hit token limit despite pre-check, falling back to batching")
                    else:
                        logger.error(f"Embedding API error: {e}")
                        return []

            # Group into batches for API calls
            # logger.info(f"Grouping pre-chunked documents into batches of ~{self.optimal_batch_size}...")
            
            doc_batches = self.group_documents_by_tokens(valid_docs, self.optimal_batch_size)
            all_embeddings = []
            
            for i, batch in enumerate(doc_batches):
                batch_tokens = sum(self.count_tokens(doc) for doc in batch)
                # logger.info(f"Processing batch {i+1}/{len(doc_batches)} with {len(batch)} docs ({batch_tokens} tokens)")
                
                try:
                    if hasattr(self.embedding_function, 'aembed_documents'):
                        batch_embeddings = await self.embedding_function.aembed_documents(batch)
                    else:
                        batch_embeddings = self.embedding_function.embed_documents(batch)
                    
                    all_embeddings.extend(batch_embeddings)
                    
                except Exception as batch_error:
                    logger.error(f"Failed to process batch {i+1}: {batch_error}")
                    # For pre-chunked docs, we shouldn't need further splitting
                    # Just skip this batch and continue
                    continue
            
            logger.info(f"Successfully processed {len(all_embeddings)}/{len(valid_docs)} documents")
            
            # Ensure we return the right number of embeddings
            if len(all_embeddings) != len(valid_docs):
                logger.error(f"Embedding count mismatch: expected {len(valid_docs)}, got {len(all_embeddings)}")
                return []
            
            return all_embeddings
            
        except Exception as e:
            logger.error(f"Error in embedding function: {e}")
            return []

    def calculate_tokens(self, text: str) -> int:
        """Public method for token calculation (used by other parts of the system)"""
        return self.count_tokens(text)
    