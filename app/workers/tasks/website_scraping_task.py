async def scrape_websites_task(ctx, scan_options, urls, task_id, client_id, dept_id, duplicate_urls, url_uuid):
    import logging
    logger = logging.getLogger(__name__)
    try:
        from app.services.website_scraping_service import WebsiteScrapingService
        service = WebsiteScrapingService()
        await service.handle_scrape_websites(
            scan_options=scan_options,
            urls=urls,
            task_id=task_id,
            client_id=client_id,
            dept_id=dept_id,
            duplicate_urls=duplicate_urls,
            url_uuid=url_uuid,
            postgres_handler=ctx['postgres_handler']
        )
    except Exception as e:
        logger.error(f"Exception during scraping for task {task_id}: {e}")
