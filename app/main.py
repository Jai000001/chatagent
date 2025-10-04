import os
from app.core.app_config import app_config
os.environ["OPENAI_API_KEY"]=app_config.OPENAI_API_KEY
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

from app.adapters.database.postgres_handler import postgres_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    import asyncio
    from app.utils.chat_session_cleanup import cleanup_inactive_sessions
    from app.adapters.database.redisdb_handler import RedisDBHandler
    redis_handler = RedisDBHandler()

    # Initialize the Postgres connection pool
    await postgres_handler.init()

    try:
        asyncio.create_task(cleanup_inactive_sessions())
        yield
    finally:
        await postgres_handler.close_db_pool()
        await redis_handler.close()

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Custom HTTPException handler to return {"error": ...} instead of {"detail": ...}
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )

# Register routers
from app.api.routes.upload_files import router as upload_files_router
from app.api.routes.get_progress import router as get_progress_router
from app.api.routes.process_pdf_url_route import router as process_pdf_url_router
from app.api.routes.website_scraping import router as website_scraping_router
from app.api.routes.source_status_route import router as source_status_router
from app.api.routes.ask_question_route import router as ask_question_router
from app.api.routes.delete_source_route import router as delete_source_router
from app.api.routes.get_collection_data_route import router as get_collection_data_router
from app.api.routes.reset_data_route import router as reset_data_router
from app.api.routes.collection_properties_route import router as collection_properties_router
from app.api.routes.collection_size_route import router as collection_size_router
from app.api.routes.collection_size_detailed_route import router as collection_size_detailed_router
from app.api.routes.create_client_collection_route import router as create_client_collection_router
from app.api.routes.get_collection_streaming_data_route import router as get_collection_streaming_data_router

app.include_router(ask_question_router, tags=["Question Answering"])
app.include_router(delete_source_router, tags=["Delete Source"])
app.include_router(get_collection_data_router, tags=["Collection Data"])
app.include_router(reset_data_router, tags=["Reset Data"])
app.include_router(collection_properties_router, tags=["Collection Properties"])
app.include_router(collection_size_router, tags=["Collection Size"])
app.include_router(collection_size_detailed_router, tags=["Collection Size Detailed"])
app.include_router(create_client_collection_router, tags=["Client Collection"])
app.include_router(get_collection_streaming_data_router, tags=["Collection Streaming Data"])
app.include_router(upload_files_router, tags=["Upload"])
app.include_router(get_progress_router, tags=["Progress"])
app.include_router(process_pdf_url_router, tags=["PDF Processing"])
app.include_router(website_scraping_router, tags=["Website Scraping"])
app.include_router(source_status_router, tags=["Source Status"])