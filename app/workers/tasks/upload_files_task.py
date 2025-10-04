async def upload_and_process_files_task(ctx, files, task_id, client_id, dept_id, duplicate_files, url_uuid):
    import logging
    logger = logging.getLogger(__name__)
    try:
        from app.services.upload_service import handle_upload_files
        # Flatten nested list if needed (multiple files)
        if files and isinstance(files[0], list):
            files = [tuple(f) for f in files]
        if files and isinstance(files[0], str) and len(files) % 2 == 0:
            files = [(files[i], files[i+1]) for i in range(0, len(files), 2)]
   
        result = await handle_upload_files(
           files=files,
           task_id=task_id,
           client_id=client_id,
           dept_ids=dept_id,
           duplicate_file_name=duplicate_files,
           url_uuid=url_uuid,
           postgres_handler=ctx['postgres_handler']
       )
        return result
    except Exception as e:
        logger.error(f"Exception in upload_and_process_files: {e}")
        return {"status": "error", "message": str(e)}
