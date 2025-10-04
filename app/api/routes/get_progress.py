from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

router = APIRouter()

@router.get("/get_progress")
async def get_progress(task_id: str = Query(None)):
    try:
        from app.adapters.database.redisdb_handler import RedisDBHandler
        redis_handler = RedisDBHandler()
 
        if not task_id:
            return JSONResponse(status_code=400, content={"error": "Task ID not provided"})

        progress_data = await redis_handler.get_progress_from_store(task_id)

        if progress_data is None:
            return JSONResponse(status_code=404, content={"error": "Task ID not found"})

        # If progress is just an int
        if isinstance(progress_data, int):
            return JSONResponse(status_code=200, content={
                "task_id": task_id,
                "progress": progress_data
            })

        # If progress is a dict
        if isinstance(progress_data, dict):
            progress = progress_data.get('progress', 0)
            execution_time = progress_data.get('execution_time', None)
            end_time = progress_data.get('end_time', None)
            data_size = progress_data.get('data_size', 0)
            uploaded_files_details = progress_data.get('uploaded_files_details', [])
            website_links_status = progress_data.get('website_links', [])
            documents_files = progress_data.get('documents_files', [])
            process_type_files = progress_data.get('process_type', 'files')
            total_tokens = progress_data.get('total_tokens', 0)
            total_cost = progress_data.get('total_cost', 0)
            urls = progress_data.get('input_urls', [])

            response = {
                "task_id": task_id,
                "progress": progress
            }

            if execution_time is not None:
                response.update({
                    "execution_time": execution_time,
                    "end_time": end_time
                })

            if process_type_files != "files":
                response.update({
                    "website_links": website_links_status,
                    "documents_files": documents_files,
                    "data_size": data_size,
                    "input_urls": urls
                })

            if process_type_files == "files":
                response["uploaded_files_details"] = uploaded_files_details

            if progress == 100:
                response.update({
                    "total_tokens": total_tokens,
                    "total_cost": total_cost
                })

            return JSONResponse(status_code=200, content=response)

        return JSONResponse(status_code=500, content={
            "error": f"Unexpected progress data type: {type(progress_data).__name__}"
        })

    except Exception as e:
        logger.error(f"Exception while fetching progress: {e}")
        return JSONResponse(status_code=500, content={"error": "Error while fetching progress"})