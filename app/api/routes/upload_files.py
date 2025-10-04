from fastapi import APIRouter, Request, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import List

router = APIRouter()

@router.post("/upload_files")
async def upload_files(
    request: Request,
    file: List[UploadFile] = File(...),
    task_id: str = Form(None),
    client_id: str = Form(...),
    dept_id: str = Form("public"),
    duplicate_files: str = Form(""),
    url_uuid: str = Form("")
):
    from app.utils.shared_utils import generate_task_id, log_request_details
    from app.core.app_config import app_config
    import aiofiles
    import os
    from datetime import datetime
    from arq import create_pool
    from arq.connections import RedisSettings
    from app.core.logger import Logger
    logger = Logger.get_logger(__name__)

    if not task_id:
        task_id = generate_task_id()

    if not client_id or not dept_id:
        return JSONResponse(status_code=400, content={"error": "Client ID and Department ID are required."})
    
    await log_request_details(
        request,
        task_id=task_id,
        dept_ids=dept_id
    )

    from app.adapters.database.redisdb_handler import RedisDBHandler
    redis_handler = RedisDBHandler()
    await redis_handler.set_progress_in_store(task_id, {"progress": 0, "execution_time": None, "end_time": None, "process_type": "files", "total_tokens": 0, "total_cost": 0, "uploaded_files_details": []})

    # Save files to disk first (reuse upload logic)
    upload_dir = os.path.join("/tmp", "uploads")
    os.makedirs(upload_dir, exist_ok=True)
    saved_files = []
    for upload in file:
        safe_filename = upload.filename
        file_path = os.path.join(upload_dir, safe_filename)
        async with aiofiles.open(file_path, 'wb') as out_file:
            content = await upload.read()
            await out_file.write(content)
        saved_files.append((safe_filename, file_path))

    start_time_full = datetime.now()
    start_date = start_time_full.strftime('%Y-%m-%d')
    start_time = start_time_full.strftime('%H:%M:%S')

    # Call Arq task for background processing
    redis = await create_pool(RedisSettings(host=app_config.REDIS_HOST, port=app_config.REDIS_PORT))
    await redis.enqueue_job(
        "upload_and_process_files_task",
        saved_files,
        task_id,
        client_id,
        dept_id,
        duplicate_files,
        url_uuid
    )
    await redis.close()
    return {
        "message": "Uploading file(s) initiated",
        "start_date": start_date,
        "start_time": start_time,
        "task_id": task_id
    }
