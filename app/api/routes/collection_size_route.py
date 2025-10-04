from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse
from fastapi import HTTPException

router = APIRouter()

@router.post("/collection_size")
async def collection_size(request: Request, client_id: str = Form(...)):
    from app.services.collection_size_service import CollectionSizeService
    service = CollectionSizeService()
    try:
        size_mb = await service.get_collection_size(request, client_id)
        return JSONResponse(status_code=200, content={"client_id": client_id, "collection_size_mb": size_mb})
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})
    except Exception as e:
        import logging
        logging.getLogger(__name__).error(f"Error getting collection size: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
