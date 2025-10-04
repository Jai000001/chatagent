from app.core.logger import Logger
logger = Logger.get_logger(__name__)

async def delete_url_and_file_sources(source_names, client_id, dept_id, url_uuid):
    import os
    import re
    from urllib.parse import urlparse
    from app.adapters.database.qdrantdb_handler import QdrantDBHandler
    qdrant_handler = QdrantDBHandler()
    deleted_sources = []
    for source_name in source_names:
        if source_name.startswith(('http://', 'https://')):
            # Handle URL
            parsed_url = urlparse(source_name)
            main_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
            url_pattern = re.compile(f"^{re.escape(main_url)}(/.*)?$")
            await qdrant_handler.delete_documents_by_url_pattern(source_name, url_pattern, client_id, dept_id, url_uuid)
            deleted_sources.append(main_url)
        else:
            # Handle file
            await qdrant_handler.delete_documents_by_source(source_name, client_id, dept_id)
            upload_file_path = os.path.join("uploads", os.path.basename(source_name))
            if os.path.exists(upload_file_path):
                os.remove(upload_file_path)
                logger.info(f"File {upload_file_path} deleted from uploads directory.")
            deleted_sources.append(source_name)

    logger.info({"message": f"Data from sources: {', '.join(deleted_sources)} deleted successfully"})
    return deleted_sources

async def split_answer_and_source(answer: str, is_slack: bool = False):
    source = ""

    if "Source:" in answer:
        if is_slack:
            parts = answer.split("Source:", 1)
            answer = parts[0].strip()
            source = parts[1].strip() if len(parts) > 1 else ""
        else:
            if "\n<p>Source:" in answer:
                parts = answer.split("\n<p>Source:", 1)
                answer = parts[0].strip()
                source = parts[1].strip() if len(parts) > 1 else ""
            elif "\nSource:" in answer:
                parts = answer.split("\nSource:", 1)
                answer = parts[0].strip()
                source = parts[1].strip() if len(parts) > 1 else ""

    # Clean the source value
    source = await clean_source(source)
    return answer, source

async def clean_source(source: str) -> str:
    import re
    if not source:
        return ""

    # Regex to extract href if exists
    match = re.search(r'href="([^"]+)"', source)
    if match:
        return match.group(1).strip()

    # Remove "Source:" text and HTML tags
    cleaned = re.sub(r"Source: ?", "", source, flags=re.IGNORECASE)
    cleaned = re.sub(r"<.*?>", "", cleaned).strip()

    return "" if cleaned.lower() == "None" else cleaned
