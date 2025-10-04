from fastapi import HTTPException
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

class CollectionPropertiesService:
    def __init__(self):
        pass

    async def get_collection_properties(self, request, client_id: str):
        from app.utils.shared_utils import log_request_details
        from app.adapters.database.qdrantdb_handler import QdrantDBHandler
        qdrant_handler = QdrantDBHandler()
        await qdrant_handler._ensure_client_initialized()

        if not client_id:
            raise HTTPException(status_code=400, detail="Missing client_id")
        await log_request_details(request)
        collection_name = qdrant_handler.get_collection_name(client_id)
        try:
            collection_info = await qdrant_handler.client.get_collection(collection_name=collection_name)
            props = {
                "name": collection_name,
                "status": collection_info.status,
                "optimizer_status": collection_info.optimizer_status,
                "vectors_count": collection_info.vectors_count,
                "indexed_vectors_count": collection_info.indexed_vectors_count,
                "points_count": collection_info.points_count,
                "segments_count": collection_info.segments_count,
                "config": {
                    "params": {
                        "vector_size": collection_info.config.params.vectors.size if hasattr(collection_info.config.params, 'vectors') else None,
                        "distance": collection_info.config.params.vectors.distance.value if hasattr(collection_info.config.params, 'vectors') else None,
                        "shard_number": collection_info.config.params.shard_number,
                        "replication_factor": collection_info.config.params.replication_factor,
                        "write_consistency_factor": collection_info.config.params.write_consistency_factor,
                        "on_disk_payload": collection_info.config.params.on_disk_payload
                    },
                    "hnsw_config": {
                        "m": collection_info.config.hnsw_config.m,
                        "ef_construct": collection_info.config.hnsw_config.ef_construct,
                        "full_scan_threshold": collection_info.config.hnsw_config.full_scan_threshold,
                        "max_indexing_threads": collection_info.config.hnsw_config.max_indexing_threads,
                        "on_disk": collection_info.config.hnsw_config.on_disk,
                        "payload_m": collection_info.config.hnsw_config.payload_m if hasattr(collection_info.config.hnsw_config, 'payload_m') else None
                    },
                    "optimizer_config": {
                        "deleted_threshold": collection_info.config.optimizer_config.deleted_threshold,
                        "vacuum_min_vector_number": collection_info.config.optimizer_config.vacuum_min_vector_number,
                        "default_segment_number": collection_info.config.optimizer_config.default_segment_number,
                        "max_segment_size": collection_info.config.optimizer_config.max_segment_size,
                        "memmap_threshold": collection_info.config.optimizer_config.memmap_threshold,
                        "indexing_threshold": collection_info.config.optimizer_config.indexing_threshold,
                        "flush_interval_sec": collection_info.config.optimizer_config.flush_interval_sec,
                        "max_optimization_threads": collection_info.config.optimizer_config.max_optimization_threads
                    }
                },
                "payload_schema": collection_info.payload_schema if hasattr(collection_info, 'payload_schema') else {},
                "embedding_function": str(qdrant_handler.embedding_function.__class__.__name__)
                    if hasattr(qdrant_handler, "embedding_function") and qdrant_handler.embedding_function else None
            }
            return props
        except Exception as e:
            logger.error(f"Error in get_collection_properties: {e}")
            raise HTTPException(status_code=500, detail=str(e))
