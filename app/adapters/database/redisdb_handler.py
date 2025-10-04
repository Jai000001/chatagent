from redis.asyncio import Redis
import json
from app.core.app_config import app_config
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

class RedisDBHandler:
    _instance = None
    _redis = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    async def get_redis(self):
        if not self._redis:
            self._redis = await Redis.from_url(
                f"redis://{app_config.REDIS_HOST}:{app_config.REDIS_PORT}",
                decode_responses=True
            )
        return self._redis

    async def close(self):
        if self._redis:
            await self._redis.close()
            self._redis = None

    async def get_progress_from_store(self, task_id: str):
        redis = await self.get_redis()
        raw = await redis.get(f"progress:{task_id}")
        if not raw:
            return None
        try:
            result = json.loads(raw)
        except json.JSONDecodeError:
            logger.error(f"Failed to decode JSON for task ID: {task_id}")
            return None
        return result

    async def set_progress_in_store(self, task_id: str, data: dict, ttl: int = 8 * 3600):
        try:
            redis = await self.get_redis()
            await redis.setex(f"progress:{task_id}", ttl, json.dumps(data))
        except Exception as e:
            logger.error(f"Failed to set progress for task ID: {task_id}: {e}")
            return None

    async def add_content_hash(self, client_id: str, content_hash: str, ttl: int = 8 * 3600):
        """
        Add a content hash to the Redis set for a client and set expiry (ttl) on the set.
        If the set already exists, expiry is refreshed.
        """
        redis = await self.get_redis()
        key = f"content_hashes:{client_id}"
        added = await redis.sadd(key, content_hash)
        if added:
            await redis.expire(key, ttl)

    async def is_content_hash_duplicate(self, client_id: str, content_hash: str) -> bool:
        redis = await self.get_redis()
        key = f"content_hashes:{client_id}"
        result = await redis.sismember(key, content_hash)
        return result

    async def get_content_hashes(self, client_id: str):
        redis = await self.get_redis()
        key = f"content_hashes:{client_id}"
        result = await redis.smembers(key)
        return result

    async def set_collection_sizing_cache(self, collection_name: str, info: dict, ttl: int = 300):
        redis = await self.get_redis()
        key = f"sizing_cache:{collection_name}"
        await redis.setex(key, ttl, json.dumps(info))

    async def get_collection_sizing_cache(self, collection_name: str) -> dict:
        redis = await self.get_redis()
        key = f"sizing_cache:{collection_name}"
        raw = await redis.get(key)
        if not raw:
            return None
        try:
            result = json.loads(raw)
            logger.info(f"Collection sizing cache for {collection_name}: {result}")
        except json.JSONDecodeError:
            return None
        return result

    async def delete_collection_sizing_cache(self, collection_name: str):
        redis = await self.get_redis()
        key = f"sizing_cache:{collection_name}"
        await redis.delete(key)
