from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse
from typing import Optional
from app.services.get_collection_streaming_data_service import GetCollectionStreamingDataService
from fastapi import HTTPException
router = APIRouter()

@router.post("/get_collection_streaming_data")
async def get_collection_streaming_data_async(
    request: Request,
    client_id: str = Form(...),
    dept_id: Optional[str] = Form(None)
):
    service = GetCollectionStreamingDataService()
    try:
        return await service.get_collection_streaming_data_async(request, client_id, dept_id)
       
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})