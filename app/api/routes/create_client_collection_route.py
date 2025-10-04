from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/create_client_collection")
async def create_client_collection(request: Request, client_id: str = Form(...)):
    from app.services.create_client_collection_service import CreateClientCollectionService
    service = CreateClientCollectionService()
    try:
        result = await service.create_client_collection(request, client_id)
        return JSONResponse(status_code=200, content=result)
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})
    except Exception as e:
        import logging
        logging.getLogger(__name__).error(f"Failed to create collection for client_id {client_id}: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
