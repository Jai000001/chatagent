from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse
from fastapi import HTTPException

router = APIRouter()

@router.post("/collection_properties")
async def collection_properties(request: Request, client_id: str = Form(...)):
    from app.services.collection_properties_service import CollectionPropertiesService
    service = CollectionPropertiesService()
    try:
        result = await service.get_collection_properties(request, client_id)
        return JSONResponse(status_code=200, content=result)
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
