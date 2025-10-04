from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse
from app.core.logger import Logger
from datetime import datetime

router = APIRouter()
logger = Logger.get_logger(__name__)

@router.post("/scrape_website")
async def scrape_website_route(
    request: Request,
    scan_options: str = Form(None),
    url: str = Form(...),
    client_id: str = Form(...),
    duplicate_urls: str = Form(""),
    url_uuid: str = Form(""),
    task_id: str = Form(None),
    dept_id: str = Form("public")
):
    try:
        from app.utils.shared_utils import generate_task_id, log_request_details
        from app.core.app_config import app_config
        if not task_id:
            task_id = generate_task_id()
            
        await log_request_details(
            request,
            task_id=task_id,
            dept_ids=dept_id
        )
        from arq import create_pool
        from arq.connections import RedisSettings
        url_list = [u.strip() for u in url.split(",") if u.strip()]
        if not url_list:
            return JSONResponse(status_code=400, content={"error": "No valid URLs provided."})

        from app.adapters.database.redisdb_handler import RedisDBHandler
        redis_handler = RedisDBHandler()
        await redis_handler.set_progress_in_store(task_id, {"progress": 0, "execution_time": None, "end_time": None, "process_type": "urls", "total_tokens": 0, "total_cost": 0, "data_size": 0, "input_urls": [{"url": url} for url in url_list]})
        
        start_time_full = datetime.now()
        start_date = start_time_full.strftime('%Y-%m-%d')
        start_time = start_time_full.strftime('%H:%M:%S')
        # Trigger Arq async scraping task
        redis = await create_pool(RedisSettings(host=app_config.REDIS_HOST, port=app_config.REDIS_PORT))
        await redis.enqueue_job(
            "scrape_websites_task",
            scan_options,
            url_list,
            task_id,
            client_id,
            dept_id,
            duplicate_urls,
            url_uuid
        )
        await redis.close()
        
        logger.info({
            "task_id": task_id,
            "message": "Scraping task initiated",
            "start_date": start_date,
            "start_time": start_time
        })
        return JSONResponse(
            status_code=200,
            content={
                "task_id": task_id,
                "message": "Scraping task initiated",
                "start_date": start_date,
                "start_time": start_time
            }
        )
    except Exception as e:
        logger.error(f"Exception while scraping website: {e}")
        return JSONResponse(status_code=500, content={"error": "Error while scraping website"})
