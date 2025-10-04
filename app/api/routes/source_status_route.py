from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse
from typing import Optional
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

router = APIRouter()

@router.post("/toggle_source_status")
async def toggle_source_status(
    request: Request,
    source_name: str = Form(...),
    action: str = Form(...),
    client_id: str = Form(...),
    url_uuid: Optional[str] = Form(None)
):
    try:
        from app.utils.shared_utils import generate_task_id, log_request_details

        task_id = generate_task_id()       
        source_names = [name.strip() for name in source_name.split(',') if name.strip()]
        dept_ids = "public"

        await log_request_details(
            request,
            task_id=task_id,
            dept_ids=dept_ids
        )

        if not source_names:
            return JSONResponse(status_code=400, content={"error": "No valid source names provided."})
        if not action:
            return JSONResponse(status_code=400, content={"error": "No valid action provided."})
        if not client_id:
            return JSONResponse(status_code=400, content={"error": "Client ID cannot be None."})
        # if not dept_ids:
        #     raise HTTPException(status_code=400, detail="At least one Department ID must be provided.")


        from app.services.source_status_service import SourceStatusService
        service = SourceStatusService()
        result = await service.toggle_source_status(request, source_name, action, client_id, url_uuid, dept_ids, task_id)
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        logger.error(f"Exception in toggle_source_status: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
