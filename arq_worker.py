from arq import run_worker

async def on_startup(ctx):
    from app.core.logger import Logger
    logger = Logger.get_logger(__name__)

    from app.adapters.database.postgres_handler import PostgresHandler
    ctx['postgres_handler'] = PostgresHandler()
    await ctx['postgres_handler'].init()
    logger.info("[Arq] PostgresHandler initialized in worker context.")

def get_cpu_count():
    try:
        import os
        return len(os.sched_getaffinity(0))
    except AttributeError:
        import multiprocessing
        return multiprocessing.cpu_count()

def safe_cpu_count():
    return max(1, get_cpu_count() - 1)

async def on_shutdown(ctx):
    from app.core.logger import Logger
    from app.adapters.database.redisdb_handler import RedisDBHandler
    logger = Logger.get_logger(__name__)
    
    # Close Postgres pool
    if 'postgres_handler' in ctx and ctx['postgres_handler']:
        await ctx['postgres_handler'].close()
        logger.info("[Arq] PostgresHandler connection pool closed.")
    
    # Close Redis connection
    redis_handler = RedisDBHandler()
    await redis_handler.close()
    logger.info("[Arq] Redis connection closed.")

class WorkerSettings:
    """
    Arq Worker Settings for CPU-bound tasks:
    - max_jobs: Set from app_config.ARQ_MAX_JOBS or safe_cpu_count().
    - worker_pool_size: Set from app_config.WORKER_POOL_SIZE.
    - max_total_concurrency: Set from app_config.MAX_TOTAL_CONCURRENCY.
    - on_startup: Preloads embedding model (and optionally LLM) for all tasks.
    """
    from arq.connections import RedisSettings
    from app.workers.tasks.website_scraping_task import scrape_websites_task
    from app.workers.tasks.upload_files_task import upload_and_process_files_task
    from app.workers.tasks.postgres_cleanup_task import postgres_cleanup_task
    from app.core.app_config import app_config

    functions = [scrape_websites_task, upload_and_process_files_task, postgres_cleanup_task]
    redis_settings = RedisSettings(
        host=app_config.REDIS_HOST,
        port=app_config.REDIS_PORT
    )
    # All concurrency and pool settings from app_config
    max_jobs = max(app_config.ARQ_MAX_JOBS, safe_cpu_count())
    # worker_pool_size = app_config.WORKER_POOL_SIZE
    # max_total_concurrency = app_config.MAX_TOTAL_CONCURRENCY
    job_timeout = 21600  # 6 hours in seconds
    on_startup = on_startup
    on_shutdown = on_shutdown
    max_tries = 1               # No retries for failed jobs
    keep_result = 8 * 3600      # Keep job results for 8 hours only

    # Run Postgres cleanup every hour
    from arq import cron
    cron_jobs = [
        cron(postgres_cleanup_task, minute=0)  # every hour at minute 0
    ]

if __name__ == "__main__":
    run_worker(WorkerSettings)
