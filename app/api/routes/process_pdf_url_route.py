from fastapi import APIRouter, Request, BackgroundTasks, Form
from fastapi.responses import JSONResponse
from typing import Optional
from app.core.logger import Logger

router = APIRouter()
logger = Logger.get_logger(__name__)

@router.post("/process_pdf_urls")
async def process_pdf_urls(
    request: Request,
    background_tasks: BackgroundTasks,
    urls: str = Form(...),
    client_id: str = Form(...),
    task_id: Optional[str] = Form(None)
):
    try:
        from app.adapters.database.redisdb_handler import RedisDBHandler
        from app.utils.shared_utils import generate_task_id, log_request_details
        from app.services.pdf_url_processing_service import PDFUrlProcessingService
        from datetime import datetime
        import time
        redis_handler = RedisDBHandler()

        pdf_urls = [url.strip() for url in urls.split(',') if url.strip()]
        dept_ids = "public"
        url_uuid = ""
        if not task_id:
            task_id = generate_task_id()

        await log_request_details(
            request,
            task_id=task_id,
            dept_ids=dept_ids
        )    

        start_datetime = datetime.now()
        await redis_handler.set_progress_in_store(task_id, {
            "progress": 0,
            "execution_time": None,
            "process_type": "files",
            "start_time": time.time()
        })
        service = PDFUrlProcessingService()

        # Launch background task (non-blocking)
        background_tasks.add_task(
            service.handle_process_pdf_urls,
            pdf_urls, task_id, client_id, dept_ids, url_uuid
        )

        return JSONResponse(status_code=200, content={
            "message": "PDF urls processing initiated",
            "start_date": start_datetime.strftime("%Y-%m-%d"),
            "start_time": start_datetime.strftime("%H:%M:%S"),
            "task_id": task_id
        })
    except Exception as e:
        logger.error(f"Error processing PDF URLs: {e}")
        return JSONResponse(status_code=500, content={"error": f"Server error: {str(e)}"})
