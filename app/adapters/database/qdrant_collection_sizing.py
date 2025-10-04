import time
import asyncio
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

class QdrantCollectionSizing:
    """
    Manages Qdrant collection sizing with caching for performance
    """
    
    def __init__(self, redis_handler=None):
        from app.adapters.database.redisdb_handler import RedisDBHandler
        self.redis_handler = redis_handler or RedisDBHandler()
        self._cache_ttl = 300  # 5 minutes cache TTL
        
    # Size thresholds (number of points)
    SIZE_THRESHOLDS = {
        'tiny': 1000,
        'small': 10000, 
        'medium': 1000000,
        'large': 100000000,
        'huge': float('inf')
    }
    
    # Context window mapping based on collection size
    CONTEXT_WINDOWS = {
        'tiny': 4096,
        'small': 8192,
        'medium': 16384,
        'large': 32768,
        'huge': 65536
    }
    
    # Search result limits based on collection size
    # SEARCH_LIMITS = {
    #     'tiny': 3,
    #     'small': 4,
    #     'medium': 5,
    #     'large': 6,
    #     'huge': 8
    # }

    SEARCH_LIMITS = {
        'tiny': 5,
        'small': 10,
        'medium': 15,
        'large': 20,
        'huge': 25
    }
    
    # Score thresholds for different collection sizes
    SCORE_THRESHOLDS = {
        'tiny': 0.15,    # Will catch your 0.27 and 0.39 scores
        'small': 0.25,   # Will catch your 0.27 and 0.39 scores  
        'medium': 0.30,  # Will catch your 0.39 score only
        'large': 0.40,   # Will filter out both (too strict)
        'huge': 0.45     # Will filter out both (too strict)
    }
    
        # 'tiny': 0.15,    # Catches both 0.39 and 0.27
        # 'small': 0.25,   # Catches both 0.39 and 0.27  
        # 'medium': 0.30,  # Catches only 0.39 (filters out 0.27)
        # 'large': 0.35,   # Catches only 0.39 (filters out 0.27)
        # 'huge': 0.42     # Filters out everything (too strict for your data)



    @classmethod
    async def get_collection_category(cls, point_count: int) -> str:
        """Determine collection category based on point count"""
        for category, threshold in cls.SIZE_THRESHOLDS.items():
            if point_count < threshold:
                return category
        return 'huge'
    
    @classmethod
    async def get_context_window(cls, point_count: int) -> int:
        """Get appropriate context window based on collection size"""
        category = await cls.get_collection_category(point_count)
        return cls.CONTEXT_WINDOWS[category]
    
    @classmethod
    async def get_search_limit(cls, point_count: int) -> int:
        """Get appropriate search result limit based on collection size"""
        category = await cls.get_collection_category(point_count)
        return cls.SEARCH_LIMITS[category]
    
    @classmethod
    async def get_score_threshold(cls, point_count: int) -> float:
        """Get appropriate score threshold based on collection size"""
        category = await cls.get_collection_category(point_count)
        return cls.SCORE_THRESHOLDS[category]
    
    async def get_cached_collection_info(self, collection_name: str, client=None) -> dict:
        """Get collection info with caching - much faster for queries (now Redis-backed)"""
        cached_info = await self.redis_handler.get_collection_sizing_cache(collection_name)
        if cached_info:
            logger.info(f"Using cached sizing info for {collection_name}")
            return cached_info
        # If no cache or expired, get fresh data (but only if client provided)
        if client is not None:
            try:
                point_count = await self._get_point_count_fast(client, collection_name)
                info = await self.get_collection_info(point_count)
                await self.redis_handler.set_collection_sizing_cache(collection_name, info, ttl=self._cache_ttl)
                logger.info(f"Updated sizing cache for {collection_name}: {info['category']} ({point_count} points)")
                return info
            except Exception as e:
                logger.warning(f"Failed to get fresh collection info for {collection_name}: {e}")
        # Fallback to default if no cache and no client or error
        default_info = await self.get_collection_info(10000)  # Assume medium as default
        logger.info(f"Using default sizing info for {collection_name}")
        return default_info

    
    async def _get_point_count_fast(self, client, collection_name: str) -> int:
        """Fast point count retrieval using collection info API"""
        try:
            # This is much faster than scroll-based counting
            collection_info = await client.get_collection(collection_name)
            return collection_info.points_count
        except Exception as e:
            logger.warning(f"Could not get point count for collection {collection_name}: {e}")
            return 10000  # Default to medium size
    
    async def update_collection_cache_async(self, collection_name: str, client):
        """Asynchronously update cache after bulk operations (now Redis-backed)"""
        try:
            await asyncio.sleep(2)  # Small delay to allow indexing to settle
            point_count = await self._get_point_count_fast(client, collection_name)
            info = await self.get_collection_info(point_count)
            await self.redis_handler.set_collection_sizing_cache(collection_name, info, ttl=self._cache_ttl)
            logger.info(f"Async updated sizing cache for {collection_name}: {info['category']} ({point_count} points)")
        except Exception as e:
            logger.warning(f"Failed to async update cache for {collection_name}: {e}")
    
    async def invalidate_cache(self, collection_name: str):
        """Invalidate cache for a specific collection (now Redis-backed)"""
        await self.redis_handler.delete_collection_sizing_cache(collection_name)
        logger.info(f"Invalidated cache for {collection_name}")

    
    @classmethod
    async def get_collection_info(cls, point_count: int) -> dict:
        """Get comprehensive collection sizing information"""
        category = await cls.get_collection_category(point_count)
        return {
            'category': category,
            'point_count': point_count,
            'context_window': cls.CONTEXT_WINDOWS[category],
            'search_limit': cls.SEARCH_LIMITS[category],
            'score_threshold': cls.SCORE_THRESHOLDS[category]
        }