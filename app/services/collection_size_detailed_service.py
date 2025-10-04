import sys
import pickle
from fastapi import HTTPException

class CollectionSizeDetailedService:
    def __init__(self):
        pass

    async def get_collection_size_detailed(self, request, client_id: str) -> dict:
        """ Get detailed size breakdown of a Qdrant collection. """
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
            return {
                'vectors_mb': 0,
                'payload_mb': 0,
                'ids_mb': 0,
                'total_items': 0,
                'total_mb': 0
            }
        
        size_breakdown = {
            'vectors_mb': 0,
            'payload_mb': 0,
            'ids_mb': 0,
            'total_items': 0,
            'total_mb': 0
        }
        
        vectors_bytes = 0
        payload_bytes = 0
        ids_bytes = 0
        total_items = 0
        
        # Build filter for this client
        filter_conditions = [
            FieldCondition(key="client_id", match=MatchValue(value=client_id))
        ]
        scroll_filter = Filter(must=filter_conditions)
        
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
                    total_items += 1
                    
                    # Calculate vector size
                    if point.vector:
                        if isinstance(point.vector, dict):
                            # Named vectors
                            for vector_name, vector_data in point.vector.items():
                                if isinstance(vector_data, list):
                                    vectors_bytes += len(vector_data) * 4  # 4 bytes per float32
                        elif isinstance(point.vector, list):
                            # Single vector
                            vectors_bytes += len(point.vector) * 4  # 4 bytes per float32
                    
                    # Calculate payload size
                    if point.payload:
                        payload_bytes += sys.getsizeof(pickle.dumps(point.payload))
                    
                    # Calculate ID size
                    if point.id:
                        ids_bytes += sys.getsizeof(str(point.id).encode('utf-8'))
                
                offset = next_page_offset
                if offset is None:
                    break
                    
            except Exception as e:
                logger.error(f"Error during detailed collection scroll: {e}")
                break
        
        # Convert to MB
        size_breakdown['vectors_mb'] = round(vectors_bytes / (1024 * 1024), 4)
        size_breakdown['payload_mb'] = round(payload_bytes / (1024 * 1024), 4)
        size_breakdown['ids_mb'] = round(ids_bytes / (1024 * 1024), 4)
        size_breakdown['total_items'] = total_items
        size_breakdown['total_mb'] = round(
            (vectors_bytes + payload_bytes + ids_bytes) / (1024 * 1024), 4
        )
        
        return size_breakdown