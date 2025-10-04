from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from app.services.ask_question_service import AskQuestionService

router = APIRouter()

@router.post("/ask_question")
async def ask_question(
    request: Request,
    session_id: Optional[str] = Form(None),
    client_id: str = Form(...),
    prompt_type: str = Form('default'),
    fromSlack: str = Form('false'),
    question: str = Form('')
):
    service = AskQuestionService()
    try:
        result = await service.ask_question(request, session_id, client_id, prompt_type, fromSlack, question)
        return JSONResponse(status_code=200, content=result)
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
