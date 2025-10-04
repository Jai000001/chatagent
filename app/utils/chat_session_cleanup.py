async def cleanup_inactive_sessions(expiry_minutes: int = 30, interval_seconds: int = 3600):
    import asyncio
    from datetime import datetime, timedelta, timezone
    from app.core.chat_memory_store import chat_memories
    from app.core.logger import Logger
    logger = Logger.get_logger(__name__)
    logger.info("Running chat memories cleanup cycle...")
    while True:
        now = datetime.now(timezone.utc)
        expired_sessions = [
            session_id for session_id, entry in chat_memories.items()
            if now - entry["last_used"] > timedelta(minutes=expiry_minutes)
        ]
        for sid in expired_sessions:
            logger.info(f"Cleaning up expired session for chat memories: {sid}")
            del chat_memories[sid]
        logger.info(f"Cleanup cycle completed for chat memories. Sleeping for {interval_seconds} seconds.")
        await asyncio.sleep(interval_seconds)
