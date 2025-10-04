from pydantic_settings import BaseSettings
from pydantic import Field

# This class loads and validates environment variables using Pydantic.
# It provides a central configuration object for the entire app.
# Values are automatically loaded from a `.env` file (or system environment),
# and you can access them as attributes (e.g., app_config.APP_PORT).
class AppConfig(BaseSettings):
    # App configuration
    APP_PORT: int = Field(5000, env="APP_PORT")
    APP_WORKERS: int = Field(4, env="APP_WORKERS")

    # Redis / ARQ configuration
    REDIS_HOST: str = Field("redis", env="REDIS_HOST")
    REDIS_PORT: int = Field(6379, env="REDIS_PORT")
    ARQ_MAX_JOBS: int = Field(20, env="ARQ_MAX_JOBS")

    # Qdrant vector DB configuration
    QDRANT_HOST: str = Field("qdrant", env="QDRANT_HOST")
    QDRANT_PORT: int = Field(6333, env="QDRANT_PORT")
    QDRANT_GRPC_PORT: int = Field(6334, env="QDRANT_GRPC_PORT")
    QDRANT_COLLECTION_NAME: str = Field("document_collection", env="QDRANT_COLLECTION_NAME")
    # Qdrant upsert tuning
    QDRANT_UPSERT_BATCH_SIZE: int = Field(500, env="QDRANT_UPSERT_BATCH_SIZE")  # Number of points per upsert batch
    QDRANT_GRPC_TIMEOUT: int = Field(60, env="QDRANT_GRPC_TIMEOUT")  # gRPC deadline for upsert in seconds


    # Postgres DB configuration
    POSTGRES_USER: str = Field("myuser", env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field("mypassword", env="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field("mydb", env="POSTGRES_DB")
    POSTGRES_PORT: int = Field(5432, env="POSTGRES_PORT")
    POSTGRES_DATABASE_URL: str = Field(
        "postgresql://myuser:mypassword@postgres:5432/mydb",
        env="POSTGRES_DATABASE_URL"
    )

    # Model and embedding configuration
    MODEL: str = Field("gpt-4o-mini", env="MODEL")
    EMBEDDING_MODEL: str = Field("text-embedding-3-large", env="EMBEDDING_MODEL")
    EMBEDDING_VECTOR_SIZE: int = Field(3072, env="EMBEDDING_VECTOR_SIZE")
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY") 
    
    # Tokenizer options
    TOKENIZERS_PARALLELISM: bool = Field(False, env="TOKENIZERS_PARALLELISM")

    # Upload settings
    UPLOAD_FILES_MAX_CONCURRENT_TASKS: int = Field(50, env="UPLOAD_FILES_MAX_CONCURRENT_TASKS")
    UPLOAD_FILES_BATCH_SIZE: int = Field(100, env="UPLOAD_FILES_BATCH_SIZE")

    # Token pricing configuration
    INPUT_RATE_PER_1K_TOKENS: float = Field(0.00015, env="INPUT_RATE_PER_1K_TOKENS")
    OUTPUT_RATE_PER_1K_TOKENS: float = Field(0.0006, env="OUTPUT_RATE_PER_1K_TOKENS")
    EMBEDDING_MODEL_RATE_PER_1K_TOKENS: float = Field(0.00013, env="EMBEDDING_MODEL_RATE_PER_1K_TOKENS")

    # Website scraping configuration
    MAX_DEPTH: int = Field(3, env="MAX_DEPTH")
    FILE_EXT_REGEX: str = Field(r'\.(csv|pdf|xlsx|jpg|jpeg|png|mp4|avi|mov|mkv|epub|mobi|dmg|css|pptx|docx|zip|exe|ppt|doc)', env="FILE_EXT_REGEX")
    PDF_FILE_EXT_REGEX: str = Field(r'\.pdf', env="PDF_FILE_EXT_REGEX")  # Matches .pdf anywhere in the URL path

    # --- Performance and concurrency tuning for scraping/embedding ---
    # Number of docs to embed in a batch (per worker)
    EMBEDDING_BATCH_SIZE: int = Field(32, env="EMBEDDING_BATCH_SIZE")
    # Max concurrent HTTP requests per worker
    SCRAPING_CONCURRENCY: int = Field(20, env="SCRAPING_CONCURRENCY")
    # HTTP connection pool size for async HTTP clients
    HTTP_POOL_SIZE: int = Field(50, env="HTTP_POOL_SIZE")
    # Postgres DB connection pool size
    POSTGRES_POOL_SIZE: int = Field(50, env="POSTGRES_POOL_SIZE")
    # Total number of ARQ worker processes
    WORKER_POOL_SIZE: int = Field(4, env="WORKER_POOL_SIZE")
    # Max concurrent jobs across all workers
    MAX_TOTAL_CONCURRENCY: int = Field(100, env="MAX_TOTAL_CONCURRENCY")
    # --- End performance tuning ---

    # Tell Pydantic to load from `.env` file by default
    class Config:
        env_file = ".env"
        case_sensitive = True


# Singleton instance that can be imported directly from anywhere in the app
app_config = AppConfig()
