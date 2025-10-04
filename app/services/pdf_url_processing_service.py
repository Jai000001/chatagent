from app.core.logger import Logger

class PDFUrlProcessingService:
    def __init__(self):
        self.logger = Logger.get_logger(__name__)

    async def handle_process_pdf_urls(self, pdf_urls, task_id, client_id, dept_ids, url_uuid):
        import time
        import requests
        from io import BytesIO
        import PyPDF2
        from app.adapters.database.redisdb_handler import RedisDBHandler
        from app.adapters.database.postgres_handler import postgres_handler
        from app.adapters.database.qdrantdb_handler import QdrantDBHandler
        from app.utils.text_splitter import shared_text_splitter
        from app.utils.file_utils_manager.file_utils import FileManager

        redis_handler = RedisDBHandler()

        qdrant_handler = QdrantDBHandler()
        file_manager = FileManager()
        all_docs = []
        total_pages = 0
        processed_pages = 0
        start_time = time.time()

        try:
            all_docs = []
            total_pages = 0
            processed_pages = 0
            start_time = time.time()
    
            # Update progress store with initial URL statuses BEFORE processing
            current_progress = await redis_handler.get_progress_from_store(task_id) or {}
           
            await redis_handler.set_progress_in_store(task_id, {
                "progress": current_progress.get("progress", 0),
                "process_type": "files",
                "uploaded_files_details": await postgres_handler.get_website_pdf_status(task_id),
                "total_count": len(pdf_urls),
                **{k: current_progress.get(k, 0) for k in ["total_tokens", "cost"]}
            })

            # First pass: count total pages
            for url in pdf_urls:
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    content_type = response.headers.get('content-type', '')
                    if 'application/pdf' not in content_type.lower():
                        await postgres_handler.add_website_pdf_status(task_id, url, 'failed', 'Not a PDF file', 0, 'File could not be read.')
                        continue
                    pdf_file = BytesIO(response.content)
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    page_count = len(pdf_reader.pages)
                    total_pages += page_count
                    await postgres_handler.add_website_pdf_status(task_id, url, None, None, page_count, None)
                except requests.RequestException as e:
                    await postgres_handler.add_website_pdf_status(task_id, url, 'failed', f'Download failed: {str(e)}', 0, 'File could not be read.')
                except Exception as e:
                    await postgres_handler.add_website_pdf_status(task_id, url, 'failed', f'Processing failed: {str(e)}', 0, 'File could not be read.')
           
            # Second pass: process PDFs
            for url in pdf_urls:
                # Skip already failed URLs
                status_records = await postgres_handler.get_website_pdf_status(task_id)
                url_status = next((s for s in status_records if s['url'] == url), None)
                if url_status and url_status['status'] == 'failed':
                    continue
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    content_type = response.headers.get('content-type', '')
                    if 'application/pdf' not in content_type.lower():
                        continue
                    doc, num_pages = await file_manager.extract_text_from_pdf(response.content, url)
                    all_docs.append(doc)
                    processed_pages += num_pages
                    await file_manager.update_upload_file_progress(task_id, processed_pages, total_pages)
                    await postgres_handler.add_website_pdf_status(task_id, url, 'uploaded', None, num_pages, None)
                except requests.RequestException as e:
                    await postgres_handler.add_website_pdf_status(task_id, url, 'failed', f'Download failed: {str(e)}', 0, 'File could not be read.')
                except Exception as e:
                    self.logger.error(f"Error processing PDF URLs2: {e}")
                    await postgres_handler.add_website_pdf_status(task_id, url, 'failed', f'Processing failed: {str(e)}', 0, 'File could not be read.')
            
            if all_docs:
                splits = shared_text_splitter.split_documents(all_docs)
                await qdrant_handler.add_documents(splits, task_id, client_id, dept_ids, url_uuid)
                # Fetch updated token/cost info from Redis
                updated_progress = await redis_handler.get_progress_from_store(task_id) or {}
                total_tokens = updated_progress.get("total_tokens", 0)
                total_cost = updated_progress.get("total_cost", 0)
                end_time = time.time()
                execution_time_round = round(end_time - start_time, 2)
                execution_time = f"{execution_time_round} seconds"
                end_time_struct = time.localtime(end_time)
                formatted_end_time = time.strftime("%H:%M:%S", end_time_struct)
                # Update all uploaded statuses
                status_records = await postgres_handler.get_website_pdf_status(task_id)
                for status in status_records:
                    if status['status'] is None:
                        await postgres_handler.add_website_pdf_status(task_id, status['url'], 'uploaded', None, status['pages'], None)
                await redis_handler.set_progress_in_store(task_id, {
                    "progress": 100,
                    "end_time": formatted_end_time,
                    "execution_time": execution_time,
                    "process_type": "files",
                    "total_tokens": total_tokens,
                    "total_cost": f"{total_cost:.6f}",
                    "uploaded_files_details": status_records,
                    "processed_count": len([s for s in status_records if s['status'] == 'uploaded']),
                    "total_count": len(pdf_urls)
                })
            else:
                status_records = await postgres_handler.get_website_pdf_status(task_id)
                await redis_handler.set_progress_in_store(task_id, {
                    "progress": 100,
                    "error": "No documents were successfully processed",
                    "uploaded_files_details": status_records,
                    "end_time": time.strftime("%H:%M:%S", time.localtime()),
                    "execution_time": f"{round(time.time() - start_time, 2)} seconds",
                    "process_type": "files",
                    "total_tokens": current_progress.get("total_tokens", 0),
                    "total_cost": f"{current_progress.get('total_cost', 0):.6f}",
                    "processed_count": len([s for s in status_records if s['status'] == 'uploaded']),
                    "total_count": len(pdf_urls)
                })
        except Exception as e:
            self.logger.error(f"Error processing PDF URLs: {e}")
            status_records = await postgres_handler.get_website_pdf_status(task_id)
            await redis_handler.set_progress_in_store(task_id, {
                "progress": 100,
                "error": f"Processing failed: {str(e)}",
                "uploaded_files_details": status_records,
                "end_time": time.strftime("%H:%M:%S", time.localtime()),
                "execution_time": f"{round(time.time() - start_time, 2)} seconds",
                "process_type": "files",
                "total_tokens": 0,
                "cost": f"{0:.6f}",
                "processed_count": len([s for s in status_records if s['status'] == 'uploaded']),
                "total_count": len(pdf_urls)
            })