from fastapi import HTTPException
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

class GetCollectionDataService:
    def __init__(self):
        pass

    async def get_collection_data_async(self, request, client_id, dept_id):
        try:
            from app.utils.shared_utils import log_request_details
            if not client_id:
                raise HTTPException(status_code=400, detail="Missing client_id")

            await log_request_details(request, dept_ids=dept_id)

            from app.adapters.database.qdrantdb_handler import QdrantDBHandler
            qdrant_handler = QdrantDBHandler()

            # Convert empty string to None for consistent handling
            dept_id = dept_id if dept_id and dept_id.strip() else None
            collection_data = await qdrant_handler.get_collection_data(client_id, dept_id)
            logger.info({"message": "Collection data fetched successfully", "client_id": client_id, "dept_id": dept_id})
            return {"collection_name": collection_data}
        except Exception as e:
            logger.error(f"Exception while fetching collection data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch the collection")
