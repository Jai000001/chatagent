async def postgres_cleanup_task(ctx):
    import logging
    logger = logging.getLogger(__name__)
    try:
        postgres_handler = ctx['postgres_handler']
        await postgres_handler.delete_old_data(hours=8)
        logger.info("Postgres cleanup: deleted data older than 8 hours.")
    except Exception as e:
        logger.error(f"Postgres cleanup failed: {e}")
