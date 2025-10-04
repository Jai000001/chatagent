from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse
from typing import Optional
from app.services.delete_source_service import DeleteSourceService

router = APIRouter()

@router.post("/delete_source")
async def delete_source_async(
    request: Request,
    client_id: str = Form(...),
    source_names: str = Form(...),
    url_uuid: Optional[str] = Form(None)
):
    service = DeleteSourceService()
    try:
        result = await service.delete_source_async(request, client_id, source_names, url_uuid)
        return JSONResponse(content=result, status_code=200)
    except Exception as e:
        from fastapi import HTTPException
        if isinstance(e, HTTPException):
            return JSONResponse(status_code=e.status_code, content={"error": e.detail})
        return JSONResponse(status_code=500, content={"error": str(e)})
