from fastapi import HTTPException

class CreateClientCollectionService:
    def __init__(self):
        pass

    async def create_client_collection(self, request, client_id: str) -> dict:
        from app.utils.shared_utils import log_request_details
        if not client_id:
            raise HTTPException(status_code=400, detail="Missing client_id in request")
        await log_request_details(request)
        from app.adapters.database.qdrantdb_handler import QdrantDBHandler
        qdrant_handler = QdrantDBHandler()
        try:
            collection_name = await qdrant_handler.get_or_create_collection(client_id)
            return {
                "message": "Collection created or retrieved successfully",
                "collection_name": collection_name
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to create collection for client_id {client_id}: {e}")
