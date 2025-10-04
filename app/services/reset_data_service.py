from fastapi.responses import JSONResponse
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

class ResetDataService:
    def __init__(self):
        pass

    async def reset_data_async(self, request, client_id):
        try:
            from app.utils.shared_utils import log_request_details
            from app.adapters.database.qdrantdb_handler import QdrantDBHandler
            qdrant_handler = QdrantDBHandler()
            # Log request details
            await log_request_details(request)

            if not client_id:
                raise ValueError("client_id is required")

            # Reset QdrantDB collection based on client_id
            await qdrant_handler.reset_collection(client_id)

            from app.core.chat_memory_store import chat_memories
            # Clear all sessions matching this client_id
            to_delete = [sid for sid, entry in chat_memories.items() if entry.get("client_id") == client_id]
            for sid in to_delete:
                del chat_memories[sid]
    
            logger.info({"message": f"Data reset successfully for client_id: {client_id}"})
            return {"message": f"Data reset successfully for client_id: {client_id}"}

        except Exception as e:
            logger.error(f"Exception while resetting data for client_id {client_id}: {e}")
            raise Exception(f"Failed to reset the data for client_id: {client_id}")
