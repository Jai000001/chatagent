# Async log_request_details for FastAPI requests
import json
from fastapi import Request
from typing import Optional
import uuid
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

def generate_task_id():
    # Generate task ID
    task_id = str(uuid.uuid4())
    return task_id

async def log_request_details(request: Optional[Request] = None, **additional_info):
    details = {}

    if request:
        details.update({
            "method": request.method,
            "url": str(request.url),
            "path": request.url.path,
            "headers": get_sanitized_headers(request.headers),
        })

        try:
            form_data = await request.form()
            form_data_dict = {}
            for key in form_data.keys():
                values = form_data.getlist(key)
                form_data_dict[key] = [
                    v.filename if hasattr(v, "filename") else str(v)
                    for v in values
                ] if len(values) > 1 else (
                    values[0].filename if hasattr(values[0], "filename") else str(values[0])
                )
            details["form_data"] = form_data_dict
        except Exception:
            pass

        try:
            if request.query_params:
                details["query_params"] = dict(request.query_params)
        except Exception:
            pass

        try:
            json_body = await request.json()
            if json_body:
                details["json_payload"] = json_body
        except Exception:
            pass

    details.update(additional_info)
    logger.info("Request Details:\n%s", json.dumps(details, indent=4))

def get_sanitized_headers(headers):
    relevant_headers = {
        'Content-Type',
        'Accept',
        'User-Agent',
        'X-Request-ID'
    }
    return {k: v for k, v in dict(headers).items() if k in relevant_headers}

def clean_answer(answer: str) -> str:
    """
    Remove markdown headers, bold/italic, and code blocks from the answer string.
    """
    import re
    # Remove markdown headers (###, ##, #)
    answer = re.sub(r"^#{1,3} .*", "", answer, flags=re.MULTILINE)
    # Remove bold/italic (**text**, *text*)
    answer = re.sub(r"(\*\*|__)(.*?)\1", r"\2", answer)
    answer = re.sub(r"(\*|_)(.*?)\1", r"\2", answer)
    # Remove code blocks (```...```)
    answer = re.sub(r"```[\s\S]*?```", "", answer)
    # Remove inline code (`...`)
    answer = re.sub(r"`([^`]*)`", r"\1", answer)
    return answer.strip()  

async def delete_existing_source(client_id, source, dept_ids=None, batch_size=1000):
    """
    Asynchronously delete documents from Qdrant collection based on source and department filters.
    Uses proper Qdrant filtering and pagination for efficient deletion.
    """
    try:
        import asyncio
        from app.adapters.database.qdrantdb_handler import QdrantDBHandler
        from qdrant_client.models import Filter, FieldCondition, MatchValue, MatchAny
        qdrant_handler = QdrantDBHandler()
        await qdrant_handler._ensure_client_initialized()

        collection_name = qdrant_handler.get_collection_name(client_id)
        
        # Build Qdrant filter conditions
        filter_conditions = [
            FieldCondition(
                key="source",
                match=MatchValue(value=source)
            ),
            FieldCondition(
                key="client_id", 
                match=MatchValue(value=client_id)
            )
        ]
        
        # Add department filter if dept_ids provided
        if dept_ids:
            filter_conditions.append(
                FieldCondition(
                    key="dept_id",
                    match=MatchAny(any=dept_ids)
                )
            )
        
        # Create the main filter
        query_filter = Filter(
            must=filter_conditions
        )
        
        total_deleted = 0
        offset = 0
        
        # Use scroll with pagination to handle large datasets
        while True:
            # Scroll through documents with the filter using native async
            scroll_result = await qdrant_handler.client.scroll(
                collection_name=collection_name,
                scroll_filter=query_filter,
                limit=batch_size,
                offset=offset,
                with_payload=True,
                with_vectors=False
            )
            
            points, next_page_offset = scroll_result
            
            # If no more points, break the loop
            if not points:
                break
                
            # Extract point IDs for deletion
            ids_to_delete = [point.id for point in points]
            
            if ids_to_delete:
                # Delete the batch of documents using native async
                await qdrant_handler.client.delete(
                    collection_name=collection_name,
                    points_selector=ids_to_delete
                )
                
                batch_deleted = len(ids_to_delete)
                total_deleted += batch_deleted
                
                logger.info({
                    "message": f"Deleted batch of {batch_deleted} documents",
                    "source": source,
                    "client_id": client_id,
                    "dept_ids": dept_ids,
                    "total_deleted_so_far": total_deleted,
                    "batch_size": batch_size
                })
                
                # Add a small delay between batches to prevent overwhelming the system
                await asyncio.sleep(0.01)
            
            # Update offset for next iteration
            if next_page_offset is not None:
                offset = next_page_offset
            else:
                # No more pages
                break
        
        logger.info({
            "message": f"Successfully deleted all matching documents",
            "total_deleted": total_deleted,
            "source": source,
            "client_id": client_id,
            "dept_ids": dept_ids
        })
    except Exception as e:
        logger.error({
            "message": "Error deleting existing source",
            "error": str(e),
            "source": source,
            "client_id": client_id,
            "dept_ids": dept_ids
        })
        raise        

def clean_source(source):
    # Remove HTML tags using regex
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', source).strip()