from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse
from app.services.reset_data_service import ResetDataService

router = APIRouter()

@router.post("/reset_data")
async def reset_data_async(
    request: Request,
    client_id: str = Form(...)
):
    service = ResetDataService()
    try:
        result = await service.reset_data_async(request, client_id)
        return JSONResponse(content=result, status_code=200)
    except ValueError as ve:
        return JSONResponse(status_code=400, content={"error": str(ve)})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
