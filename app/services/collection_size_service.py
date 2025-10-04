import sys
import pickle
from fastapi import HTTPException

class CollectionSizeService:
    def __init__(self):
        pass

    async def get_collection_size(self, request, client_id: str) -> float:
        """ Calculate the total size of a Qdrant collection in MB. """
        from app.utils.shared_utils import log_request_details

        if not client_id:
            raise HTTPException(status_code=400, detail="Missing client_id")

        await log_request_details(request)

        from app.adapters.database.qdrantdb_handler import QdrantDBHandler
        from qdrant_client.models import (
            Filter, FieldCondition, MatchValue
        )
        qdrant_handler = QdrantDBHandler()
        collection_name = qdrant_handler.get_collection_name(client_id)
        if not await qdrant_handler._collection_exists(collection_name):
            logger.warning(f"Collection {collection_name} for client {client_id} does not exist")
            return 0.0
        
        total_size_bytes = 0
        
        # Build filter for this client
        filter_conditions = [
            FieldCondition(key="client_id", match=MatchValue(value=client_id))
        ]
        scroll_filter = Filter(must=filter_conditions)
        
        # Scroll through all points in the collection
        offset = None
        batch_size = 1000
        
        while True:
            try:
                response = await qdrant_handler.client.scroll(
                    collection_name=collection_name,
                    limit=batch_size,
                    offset=offset,
                    with_payload=True,
                    with_vectors=True,
                    scroll_filter=scroll_filter
                )
                
                points, next_page_offset = response
                
                if not points:
                    break
                
                for point in points:
                    # Calculate vector size (embeddings)
                    if point.vector:
                        if isinstance(point.vector, dict):
                            # Named vectors
                            for vector_name, vector_data in point.vector.items():
                                if isinstance(vector_data, list):
                                    total_size_bytes += len(vector_data) * 4  # 4 bytes per float32
                        elif isinstance(point.vector, list):
                            # Single vector
                            total_size_bytes += len(point.vector) * 4  # 4 bytes per float32
                    
                    # Calculate payload size (metadata + documents)
                    if point.payload:
                        payload_size = sys.getsizeof(pickle.dumps(point.payload))
                        total_size_bytes += payload_size
                    
                    # Calculate ID size
                    if point.id:
                        id_size = sys.getsizeof(str(point.id).encode('utf-8'))
                        total_size_bytes += id_size
                
                offset = next_page_offset
                if offset is None:
                    break
                    
            except Exception as e:
                logger.error(f"Error during collection scroll: {e}")
                break
        
        # Convert bytes to megabytes
        size_mb = total_size_bytes / (1024 * 1024)
        return round(size_mb, 4)
