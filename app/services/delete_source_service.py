from fastapi import HTTPException
from typing import Optional
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

class DeleteSourceService:
    def __init__(self):
        pass

    async def delete_source_async(self, request, client_id: str, source_names: str, url_uuid: Optional[str]):
        try:
            from app.utils.shared_utils import log_request_details
            from app.services.service_utils import delete_url_and_file_sources
            from app.adapters.database.qdrantdb_handler import QdrantDBHandler
            qdrant_handler = QdrantDBHandler()

            # Parse inputs
            source_names_list = [name.strip() for name in source_names.split(',') if name.strip()]
            url_uuids = [uuid.strip() if uuid and uuid.strip() else None for uuid in url_uuid.split(',')] if url_uuid else []
            url_uuids.extend([None] * (len(source_names_list) - len(url_uuids)))
            url_uuids = url_uuids[:len(source_names_list)]

            dept_ids = "public"
            await log_request_details(request, dept_ids=dept_ids)

            if not client_id:
                raise HTTPException(status_code=400, detail="Client ID cannot be None.")
            if not source_names_list:
                raise HTTPException(status_code=400, detail="No valid source names provided.")

            collection_name = qdrant_handler.get_collection_name(client_id)
            temp_collection_name = f"{collection_name}_temp"
            deletion_results = []
            has_data = False

            for source_name, url_id in zip(source_names_list, url_uuids):
                try:
                    main_has_data = await qdrant_handler._collection_has_data(collection_name, source_name)
                    temp_exists = await qdrant_handler._collection_exists(temp_collection_name)
                    temp_has_data = (
                        temp_exists and await qdrant_handler._collection_has_data(temp_collection_name, source_name)
                    )
                    if main_has_data or temp_has_data:
                        has_data = True
                        await delete_url_and_file_sources([source_name], client_id, dept_ids, url_id)
                        deletion_results.append({"source_name": source_name, "url_uuid": url_id, "status": "deleted"})
                        logger.info(f"Successfully deleted source: {source_name} with URL UUID: {url_id}")
                    else:
                        deletion_results.append({"source_name": source_name, "url_uuid": url_id, "status": "no_data"})
                        logger.info(f"No data found for source: {source_name}")
                except Exception as source_error:
                    logger.warning(f"Failed to delete source {source_name} with URL UUID {url_id}: {str(source_error)}")
                    deletion_results.append({ "source_name": source_name, "url_uuid": url_id, "status": "failed", "error": str(source_error)})

            message = "No data found to delete" if not has_data else "Data deletion completed successfully"
            return {
                "message": message,
                "is_delete": True,
                "deletion_results": deletion_results
            }
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Exception while deleting data for the Sources: {source_names} : {e}")
            raise HTTPException(status_code=500, detail="Internal server error while deleting source data.")
