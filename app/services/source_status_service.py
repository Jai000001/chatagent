from app.core.logger import Logger
logger = Logger.get_logger(__name__)

class SourceStatusService:
    def __init__(self):
        pass

    async def toggle_source_status(self, request, source_name, action, client_id, url_uuid, dept_ids, task_id):
        source_names = [name.strip() for name in source_name.split(',') if name.strip()]
        # Status trackers
        activated_sources = []
        deactivated_sources = []
        action_type = ""
        success_count = 0
        old_success_count = 0
        
        from app.core.app_config import app_config
        from app.adapters.database.qdrantdb_handler import QdrantDBHandler
        qdrant_handler = QdrantDBHandler()
        await qdrant_handler._ensure_client_initialized()
        temp_collection_name = f"{app_config.QDRANT_COLLECTION_NAME}_client_{client_id}_temp"
        existing_collections = (await qdrant_handler.client.get_collections()).collections
        temp_collection_exists = any(col.name == temp_collection_name for col in existing_collections)

        # Perform action
        from fastapi import HTTPException
        try:
            if action == 'inactive':
                success_count = await qdrant_handler.move_sources_to_temp(source_names, client_id, dept_ids, url_uuid)
                deactivated_sources.extend(source_names)
                action_type = "is_inactive"
                logger.info(f"Sources {source_names} moved to temp collection")
                   
            elif action == 'active':
                if temp_collection_exists:
                    success_count = await qdrant_handler.move_sources_from_temp(source_names, client_id, dept_ids, url_uuid)
                old_success_count = await qdrant_handler.update_client_id(client_id, source_names, action, dept_ids, url_uuid)
                activated_sources.extend(source_names)
                action_type = "is_active"
                logger.info(f"Sources {source_names} moved back to active collection")
                
            else:
                raise HTTPException(status_code=400, detail=f"Invalid action: {action}")
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error processing sources: {e}")
            raise HTTPException(status_code=500, detail=f"Error processing sources: {str(e)}")

        from app.adapters.database.redisdb_handler import RedisDBHandler
        redis_handler = RedisDBHandler()
        current_progress = await redis_handler.get_progress_from_store(task_id) or {}
        # cost = current_progress.get("cost", 0)
        # total_cost = f"{cost:.6f}"

        action_type = {"active": "is_active", "inactive": "is_inactive"}.get(action)
        success = (success_count + old_success_count)
        if success > 0:
            message = f"Sources {action} successfully."
        else:
            message = f"Sources have already been {action}."

        logger.info({
            "message": message,
            action_type: True,
            "activated_sources": activated_sources,
            "deactivated_sources": deactivated_sources,
            "client_id": client_id,
            "total_tokens": current_progress.get("total_tokens", 0),
            "cost": 0
        })

        return {
            "message": message,
            action_type: True,
            "activated_sources": activated_sources,
            "deactivated_sources": deactivated_sources,
            "client_id": client_id,
            "total_tokens": current_progress.get("total_tokens", 0),
            "cost": 0
        }
