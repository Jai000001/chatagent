from app.core.logger import Logger
logger = Logger.get_logger(__name__)

class WebsiteScrapingService:
    def __init__(self):
        self.client_content_hashes = {}   

    async def handle_scrape_websites(self, scan_options, urls, task_id, client_id, dept_id, duplicate_urls, url_uuid, postgres_handler):
        import time
        from urllib.parse import urlparse
        from app.adapters.web_scraper.scraper import WebScraper
        from app.adapters.database.redisdb_handler import RedisDBHandler
        from app.adapters.database.qdrantdb_handler import QdrantDBHandler
        from app.utils.text_splitter import shared_text_splitter
        from app.utils.scraping_utils_manager.scraping_utils import ScrapingManager
        from app.utils.shared_utils import delete_existing_source
        from app.core.app_config import app_config
        
        redis_handler = RedisDBHandler()
        qdrant_handler = QdrantDBHandler()
        scraping_manager = ScrapingManager()
        start_time = time.time()
        webscraper = WebScraper(postgres_handler=postgres_handler)

        if not urls:
            logger.error({"error": "No URLs provided"})
            raise ValueError("No URLs provided")
                            
        # Handle both string and list inputs for URLs
        if isinstance(urls, str):
            url_list = [url.strip() for url in urls.split(',')]
        elif isinstance(urls, list):
            url_list = [url.strip() if isinstance(url, str) else url for url in urls]
        else:
            logger.error({"error": "Invalid URL input type"})
            raise ValueError("URLs must be provided as a comma-separated string or a list")
        
        logger.info(f"Scraping process started: {urls}")
        
        # Handle duplicate URLs logic - FIXED: missing filtered_url_list usage
        if duplicate_urls:
            duplicate_url_list = [u.strip() for u in duplicate_urls.split(",") if u.strip()]
            filtered_url_list = []
            for url in url_list:
                if url in duplicate_url_list:
                    if isinstance(dept_id, str):
                        dept_ids = [dept_id]
                    elif isinstance(dept_id, list):
                        dept_ids = dept_id
                    else:
                        dept_ids = []
                    try:
                        # Delete existing source for the duplicate URL
                        await delete_existing_source(client_id, url, dept_ids)
                        filtered_url_list.append(url)
                        logger.info(f"Found duplicate URL: {url}. Existing source will be replaced.")
                    except Exception as e:
                        logger.warning(f"Failed to delete existing source for URL {url}: {e}")
                else:
                    filtered_url_list.append(url)
            # Use filtered list for further processing
            url_list = filtered_url_list

        # Initialize website_links_status using PostgresHandler - UPDATED
        website_links_status = {}
        for url in url_list:
            website_links_status[url] = {"url": url, "status": "pending", "error": None, "reason": None}
            # Store initial status in PostgresHandler
            await postgres_handler.add_scraped_status(task_id, url, "pending", error=None, reason=None)

        documents_files = {}
        all_docs = []
        visited = set()
        invalid_urls = [url for url in url_list if not all([urlparse(url).scheme, urlparse(url).netloc])]
        
        if invalid_urls:
            # Update website_links_status for invalid URLs and store in PostgresHandler
            for url in invalid_urls:
                website_links_status[url]["status"] = "failed"
                website_links_status[url]["error"] = "Invalid URL format"
                website_links_status[url]["reason"] = "URL is missing scheme or netloc"
                await postgres_handler.add_scraped_status(task_id, url, "failed", "Invalid URL format: URL is missing scheme or netloc")
            
            # Remove invalid URLs from the processing list
            url_list = [url for url in url_list if url not in invalid_urls]
            
            # If all URLs are invalid, complete the task with failure status
            if not url_list:
                # Use PostgresHandler to get status - UPDATED
                website_links_status_list = await postgres_handler.get_scraped_status(task_id)
                documents_files_list = await postgres_handler.get_website_pdf_files(task_id)
                
                await redis_handler.set_progress_in_store(task_id, {
                    "progress": 100, 
                    "execution_time": f"{round(time.time() - start_time, 2)} seconds",
                    "end_time": time.strftime("%H:%M:%S", time.localtime()),
                    "website_links": website_links_status_list,
                    "documents_files": documents_files_list,
                    "process_type": "urls",
                    "total_tokens": 0,
                    "total_cost": 0,
                    "data_size": 0,
                    "input_urls": [{"url": url} for url in url_list]
                })
                logger.error({"error": "All URLs are invalid", "invalid_urls": invalid_urls})
                
                return {
                    "task_id": task_id,
                    "message": "All provided URLs are invalid",
                    "execution_time": f"{round(time.time() - start_time, 2)} seconds",
                    "website_links": website_links_status_list,
                    "documents_files": documents_files_list,
                    "process_type": "urls",
                    "total_tokens": 0,
                    "total_cost": 0,
                    "data_size": 0,
                    "input_urls": [{"url": url} for url in url_list]
                }
            
            # Log the invalid URLs but continue processing valid ones
            logger.warning(f"Invalid URLs found and will be skipped: {invalid_urls}")
        
        try:
            import aiohttp
            async with aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(limit=app_config.HTTP_POOL_SIZE, force_close=False, enable_cleanup_closed=True),
                raise_for_status=True
            ) as session:
                pdf_files = {}  # Initialize/reset PDF files tracking
                scraped_status = {'scraped_urls': [], 'not_scraped_urls': {}}  # Reset scraped status
                task_content_hashes = set()
                for url in url_list:
                    # Update status to "in progress" in both memory and PostgresHandler - UPDATED
                    website_links_status[url]["status"] = "in progress"
                    await postgres_handler.add_scraped_status(task_id, url, "in progress")
                    
                    try:
                        await webscraper.scrape_website(scan_options, url, task_id, max_depth=app_config.MAX_DEPTH, session=session)
                    except Exception as e:
                        website_links_status[url]["status"] = "failed"
                        website_links_status[url]["error"] = str(e)
                        website_links_status[url]["reason"] = "Failed due to error in url."
                        # Store failure status in PostgresHandler - ADDED
                        await postgres_handler.add_scraped_status(task_id, url, "failed", f"Failed due to error in url: {str(e)}")
                        continue
                    
                # Get all scraped documents from PostgresHandler
                all_docs = await postgres_handler.get_scraped_documents(task_id)
                for doc in all_docs:
                    doc.metadata['dept_id'] = dept_id
                    
                # Update documents_files with found PDFs from webscraper
                documents_files.update(pdf_files)
                    
            # Update status for URLs based on scraping results using PostgresHandler - UPDATED
            for url in url_list:
                if url in scraped_status['scraped_urls']:
                    website_links_status[url]["status"] = "uploaded"
                    website_links_status[url]["error"] = None
                    website_links_status[url]["reason"] = None
                    await postgres_handler.add_scraped_status(task_id, url, "uploaded")
                elif url in scraped_status['not_scraped_urls']:
                    error_msg = scraped_status['not_scraped_urls'][url]
                    website_links_status[url]["status"] = "failed"
                    website_links_status[url]["error"] = error_msg
                    website_links_status[url]["reason"] = "Failed due to error in url."
                    await postgres_handler.add_scraped_status(task_id, url, "failed", error=error_msg, reason="Failed due to error in url.")
            
            # Handle any additional visited URLs not in the original list
            for url in visited:
                if url not in website_links_status:
                    if url in scraped_status['scraped_urls']:
                        website_links_status[url] = {
                            "url": url,
                            "status": "uploaded",
                            "error": None,
                            "reason": None
                        }
                        await postgres_handler.add_scraped_status(task_id, url, "uploaded")
                    else:
                        error_msg = scraped_status['not_scraped_urls'].get(url, "Unknown error")
                        website_links_status[url] = {
                            "url": url,
                            "status": "failed",
                            "error": error_msg,
                            "reason": "Failed due to error in url."
                        }
                        await postgres_handler.add_scraped_status(task_id, url, "failed", error=error_msg, reason="Failed due to error in url.")
            
            if not all_docs:
                # Use PostgresHandler to get final status - UPDATED
                website_links_status_list = await postgres_handler.get_scraped_status(task_id)
                documents_files_list = await postgres_handler.get_website_pdf_files(task_id)

                # Extract message for each url with failed/in progress/pending status
                status_messages = []
                for item in website_links_status_list:
                    status = item.get('status', '').lower()
                    msg = (item.get('error', '') or '') + (': ' + item.get('reason', '') if item.get('reason', '') else '')
                    if "message=''" in msg or not msg.strip():
                        msg = 'No text scraped'
                    if status in ['failed', 'in progress', 'pending']:
                        status_messages.append(msg)
                combined_status_message = '\n'.join(status_messages)
                
                for url in website_links_status:
                    if website_links_status[url]["status"] in ["pending", "in progress"]:
                        website_links_status[url]["status"] = "failed"
                        website_links_status[url]["error"] = combined_status_message
                        website_links_status[url]["reason"] = "Failed due to error."
                        # Store in PostgresHandler - ADDED
                        await postgres_handler.add_scraped_status(task_id, url, "failed", error=combined_status_message, reason="Failed due to error.")
                        
                website_links_status_list = await postgres_handler.get_scraped_status(task_id)

                await redis_handler.set_progress_in_store(task_id, {
                    "progress": 100, 
                    "execution_time": f"{round(time.time() - start_time, 2)} seconds",
                    "end_time": time.strftime("%H:%M:%S", time.localtime()),
                    "website_links": website_links_status_list,
                    "documents_files": documents_files_list,
                    "process_type": "urls",
                    "total_tokens": 0,
                    "total_cost": 0,
                    "data_size": 0,
                    "input_urls": [{"url": url} for url in url_list]
                })
                logger.error({"error": combined_status_message})
                
                return {
                    "task_id": task_id,
                    "message": "Website not scraped",
                    "execution_time": f"{round(time.time() - start_time, 2)} seconds",
                    "website_links": website_links_status_list,
                    "documents_files": documents_files_list,
                    "process_type": "urls",
                    "total_tokens": 0,
                    "total_cost": 0,
                    "data_size": 0,
                    "input_urls": [{"url": url} for url in url_list]
                }
            
            # Calculate character and word counts for all documents
            total_chars = sum(len(doc.page_content) for doc in all_docs)
            total_words = sum(len(doc.page_content.split()) for doc in all_docs)
            
            # First, split the documents into chunks
            import asyncio
            from app.core.app_config import app_config

            all_splits = shared_text_splitter.split_documents(all_docs)

            # Deduplicate and check for inappropriate content
            unique_splits = []
            duplicate_count = 0

            for split in all_splits:
                # Compute content hash
                if client_id in self.client_content_hashes:
                    # Remove hashes specific to these URLs
                    url_list_for_hash = [urls] if isinstance(urls, str) else urls
                    self.client_content_hashes[client_id] = {
                        content_hash for content_hash in self.client_content_hashes[client_id]
                        if not any(url in split.metadata.get('source', '') for url in url_list_for_hash)
                    }
                content_hash = await scraping_manager.compute_scraping_content_hash(split.page_content)
                # Check against both client-specific and task-specific hash sets
                is_duplicate = False
                if client_id in self.client_content_hashes:
                    if content_hash in self.client_content_hashes[client_id]:
                        is_duplicate = True
                if not is_duplicate:
                    unique_splits.append(split)
                    if client_id not in self.client_content_hashes:
                        self.client_content_hashes[client_id] = set()
                    self.client_content_hashes[client_id].add(content_hash)
                    task_content_hashes.add(content_hash)
                else:
                    duplicate_count += 1

            # Log statistics
            if duplicate_count > 0:
                logger.info(f"Removed {duplicate_count} duplicate chunks")

            # Add unique splits to QdrantDB
            if unique_splits:
                await qdrant_handler.add_documents(unique_splits, task_id, client_id, dept_id, url_uuid)

            # Calculate execution time and update progress
            end_time = time.time()
            execution_time_round = round(end_time - start_time, 2)
            execution_time = f"{execution_time_round} seconds"
            end_time_struct = time.localtime(end_time)
            formatted_end_time = time.strftime("%H:%M:%S", end_time_struct)
            
            # Use PostgresHandler to fetch final status and PDF files - CONSISTENT USAGE
            website_links_status_list = await postgres_handler.get_scraped_status(task_id)
            documents_files_list = await postgres_handler.get_website_pdf_files(task_id)
            
            # If PostgresHandler returns empty results, fall back to in-memory data
            if not website_links_status_list:
                website_links_status_list = list(website_links_status.values())
            if not documents_files_list:
                documents_files_list = [{"url": url, "filename": filename} for url, filename in documents_files.items()]
            
            data_size = await qdrant_handler.get_collection_size_mb(url_list[0] if url_list else "", client_id, dept_id)
                  
            current_progress = await redis_handler.get_progress_from_store(task_id) or {}           
            await redis_handler.set_progress_in_store(task_id, {
                "progress": 100, 
                "execution_time": execution_time,
                "end_time": formatted_end_time,
                "website_links": website_links_status_list,
                "documents_files": documents_files_list,
                "process_type": "urls",
                "total_tokens": current_progress.get("total_tokens", 0),
                "total_cost": current_progress.get("total_cost", 0),
                "data_size": f"{data_size:.6f}",
                "input_urls": [{"url": url} for url in url_list]
            })

            get_count = await postgres_handler.get_uploaded_and_failed_counts(task_id)
    
            logger.info({
                "task_id": task_id, 
                "message": "Websites have been scraped and documents added", 
                "execution_time": execution_time,
                "website_links_uploaded_count": get_count["uploaded"],
                "website_links_failed_count": get_count["failed"],
                "documents_files_count": len(documents_files_list),
                "process_type": "urls",
                "total_tokens": current_progress.get("total_tokens", 0),
                "total_cost": current_progress.get("total_cost", 0),
                "data_size": f"{data_size:.6f}",
                "character_count": total_chars,
                "word_count": total_words,
                "input_urls": [{"url": url} for url in url_list]
            })
            
            logger.info(f"Total documents scraped: {len(all_docs)}")
            logger.info(f"Total unique chunks: {len(unique_splits)}")
            
            return {
                "task_id": task_id, 
                "message": "Websites have been scraped and documents added", 
                "execution_time": execution_time,
                "website_links": website_links_status_list,
                "documents_files": documents_files_list,
                "process_type": "urls",
                "total_tokens": current_progress.get("total_tokens", 0),
                "total_cost": current_progress.get("total_cost", 0),
                "data_size": f"{data_size:.6f}",
                "character_count": total_chars,
                "word_count": total_words,
                "input_urls": [{"url": url} for url in url_list]
            }
        
        except Exception as e:
            logger.error({"error": str(e)})
            execution_time_round = round(time.time() - start_time, 2)
            execution_time = f"{execution_time_round} seconds"
            
            # Initialize current_progress with an empty dictionary if not already defined
            current_progress = await redis_handler.get_progress_from_store(task_id) or {}
            logger.info(f"website_links_status: {website_links_status}")

            # Use PostgresHandler to get final status - UPDATED
            website_links_status_list = await postgres_handler.get_scraped_status(task_id)
            documents_files_list = await postgres_handler.get_website_pdf_files(task_id)
            # Extract message for each url with failed/in progress/pending status
            status_messages = []
            for item in website_links_status_list:
                status = item.get('status', '').lower()
                msg = (item.get('error', '') or '') + (': ' + item.get('reason', '') if item.get('reason', '') else '')
                if "message=''" in msg or not msg.strip():
                    msg = 'No text scraped'
                if status in ['failed', 'in progress', 'pending']:
                    status_messages.append(msg)
            combined_status_message = '\n'.join(status_messages)
            
            for url in website_links_status:
                if website_links_status[url]["status"] in ["pending", "in progress"]:
                    website_links_status[url]["status"] = "failed"
                    website_links_status[url]["error"] = combined_status_message
                    website_links_status[url]["reason"] = "Failed due to error."
                    # Store in PostgresHandler - ADDED
                    await postgres_handler.add_scraped_status(task_id, url, "failed", error=combined_status_message, reason="Failed due to error.")
            
            website_links_status_list = await postgres_handler.get_scraped_status(task_id)
            
            # Fallback to in-memory data if PostgresHandler returns empty
            if not website_links_status_list:
                website_links_status_list = list(website_links_status.values())
            if not documents_files_list:
                documents_files_list = [{"url": url, "filename": filename} for url, filename in documents_files.items()]
            
            await redis_handler.set_progress_in_store(task_id, {
                "progress": 100, 
                "execution_time": execution_time,
                "website_links": website_links_status_list,
                "documents_files": documents_files_list,
                "process_type": "urls",
                "total_tokens": current_progress.get("total_tokens", 0),
                "total_cost": current_progress.get("total_cost", 0),
                "data_size": current_progress.get("data_size", 0),
                "character_count": 0,  # Add default values for error case
                "word_count": 0,       # Add default values for error case
                "input_urls": [{"url": url} for url in url_list]
            })
            logger.error(f"Exception during scraping for task {task_id}: {str(e)}")
            raise