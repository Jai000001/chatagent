from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse
from fastapi import HTTPException

router = APIRouter()

@router.post("/collection_size_detailed")
async def collection_size_detailed(request: Request, client_id: str = Form(...)):
    from app.services.collection_size_detailed_service import CollectionSizeDetailedService
    service = CollectionSizeDetailedService()
    try:
        size_breakdown = await service.get_collection_size_detailed(request, client_id)
        return JSONResponse(status_code=200, content={"client_id": client_id, **size_breakdown})
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})
    except Exception as e:
        import logging
        logging.getLogger(__name__).error(f"Error getting collection size detailed: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
