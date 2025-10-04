"""
Adapter for web scraping logic, migrated from legacy plugins/web_scraper/scraper.py.
Supports async scraping with robots.txt checks, concurrency, and DB integration.
"""
import asyncio
from urllib.parse import urljoin, urlparse, urldefrag
from urllib import robotparser
from app.core.logger import Logger
from app.core.app_config import app_config

# This one is without queue
class WebScraper:
    def __init__(self, max_concurrent_requests=None, postgres_handler=None):
        if max_concurrent_requests is None:
            max_concurrent_requests = app_config.SCRAPING_CONCURRENCY
        if postgres_handler is None:
            raise ValueError("WebScraper requires a postgres_handler instance.")
        self.scraped_urls = 0
        self.lock = asyncio.Lock()
        self.semaphore = asyncio.Semaphore(max_concurrent_requests)
        self.db = postgres_handler
        self.logger = Logger.get_logger(__name__)
    
    def decode_content(self, content):
        try:
            return content.decode('utf-8')
        except UnicodeDecodeError:
            try:
                return content.decode('latin-1')
            except UnicodeDecodeError:
                return content.decode('utf-8', errors='ignore')

    async def fetch_content(self, session, url, task_id):
        import aiohttp
        # import re
        import random

        # Helper to detect dynamic extensions
        # def is_dynamic_url(url):
        #     return re.search(r"\.(jsp|aspx|php|org)", url, re.IGNORECASE)

        # if is_dynamic_url(url):
        #         try:
        #             content = await self.fetch_content_playwright(url, task_id)
        #             if not content:
        #                 await self.db.add_scraped_status(task_id, url, 'failed', error="empty content", reason="No content returned from fetch.")
        #             return content
        #         except Exception as e:
        #             await self.db.add_scraped_status(task_id, url, 'failed', error=str(e), reason="Exception during scraping.")

        async with self.semaphore:
            # Pool of User-Agent strings (rotate to avoid detection)
            user_agents = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
            ]   
            headers = {
                'User-Agent': random.choice(user_agents),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Cache-Control': 'max-age=0'
            }   
            timeout_main = aiohttp.ClientTimeout(total=20)
            try:
                async with session.get(url, timeout=timeout_main, headers=headers) as response:
                    content = await response.content.read()
                    return self.decode_content(content)
            except Exception as e:
                error_msg = f'{str(e)}' if str(e) else "Unable to fetch URL"
                await self.db.add_scraped_status(task_id, url, 'failed', error=error_msg, reason="Unable to fetch content")
                return ""

    # async def fetch_content_playwright(self, url, task_id):
    #     from playwright.async_api import async_playwright
    #     from playwright_stealth import stealth_async
    #     import random
    #     import asyncio
    #     async with self.semaphore:
    #         try:
    #             async with async_playwright() as p:
    #                 browser = await p.chromium.launch(headless=True)
    #                 context = await browser.new_context(
    #                     user_agent=random.choice([
    #                         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    #                         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    #                         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    #                     ]),
    #                     viewport={'width': 1280, 'height': 720},
    #                     locale='en-US',
    #                     timezone_id='America/New_York',
    #                     java_script_enabled=True,
    #                     ignore_https_errors=True
    #                 )
    #                 page = await context.new_page()
    #                 await stealth_async(page)
    #                 try:
    #                     # Timeout for the entire playwright operation
    #                     async def playwright_task():
    #                         await page.goto(url, timeout=20000)
    #                         await page.wait_for_load_state('networkidle', timeout=20000)
    #                         await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
    #                         await page.wait_for_timeout(1000)
    #                         return await page.content()
    #                     content = await asyncio.wait_for(playwright_task(), timeout=30)
    #                     return content
    #                 except asyncio.TimeoutError as timeout_error:
    #                     await self.db.add_scraped_status(task_id, url, 'failed', str(timeout_error))
    #                     return ""
    #                 except Exception as e:
    #                     await self.db.add_scraped_status(task_id, url, 'failed', error=str(e), reason="Exception during scraping.")
    #                     return ""
    #                 finally:
    #                     await browser.close()
    #         except Exception as e:
    #             await self.db.add_scraped_status(task_id, url, 'failed', error=str(e), reason="Exception during scraping.")
    #             return ""

    async def is_visited(self, url, task_id):
        return await self.db.is_visited(url, task_id)

    async def mark_visited(self, url, task_id):
        await self.db.mark_visited(url, task_id)

    async def store_document(self, doc, task_id):
        doc.metadata['task_id'] = task_id
        await self.db.store_website_links_document(doc)
        await asyncio.sleep(0)  # Yield control

    async def is_allowed_to_scrape(self, session, url):
       """Check robots.txt (cached version)"""  
       parsed_url = urlparse(url)
       robots_url = urljoin(f"{parsed_url.scheme}://{parsed_url.netloc}", "/robots.txt")
        
       # Cache robots.txt per domain
       if not hasattr(self, '_robots_cache'):
           self._robots_cache = {}
            
       domain = parsed_url.netloc
       if domain in self._robots_cache:
           return self._robots_cache[domain]
        
       rp = robotparser.RobotFileParser()
       try:
           async with session.get(robots_url, timeout=5) as response:
               if response.status == 200:
                   robots_txt = await response.text()
                   rp.parse(robots_txt.splitlines())
                   can_fetch = rp.can_fetch("*", url)
                   self._robots_cache[domain] = can_fetch
                   return can_fetch
               else:
                   self._robots_cache[domain] = True
                   return True
       except Exception as e:
           self._robots_cache[domain] = True
           return True

    async def scrape_website(self, scan_options, url, task_id, max_depth=3, current_depth=0, session=None):
        try:
            url, _ = urldefrag(url)

            if await self.is_visited(url, task_id):
                return []

            import re
            pdf_pattern = re.compile(app_config.PDF_FILE_EXT_REGEX, re.IGNORECASE)
            file_pattern = re.compile(app_config.FILE_EXT_REGEX, re.IGNORECASE)

            # Check for PDF files
            if pdf_pattern.search(url) or url.startswith('#'):
                pdf_filename = url.split('/')[-1]
                await self.db.add_website_pdf_file(task_id, url, pdf_filename)
                await self.db.add_scraped_status(task_id, url, 'failed', 'It is not an HTML page')
                return []

            # Check for non-HTML file types (e.g., .png, .jpg, .mp4, etc.)
            if file_pattern.search(url):
                filename = url.split('/')[-1]
                await self.db.add_scraped_status(task_id, url, 'failed', 'It is not an HTML page')
                return []

            # Mark the URL as visited in Postgres
            await self.mark_visited(url, task_id)

            if current_depth > max_depth:
                return []

            if not await self.is_allowed_to_scrape(session, url):
                await self.db.add_scraped_status(task_id, url, 'failed', error="Scraping not allowed by robots.txt", reason="Blocked by robots.txt policy.")
                return []

            return await self._scrape_website_with_session(scan_options, url, task_id, max_depth, current_depth, session)

        except Exception as e:
            return []  
    
    async def _scrape_website_with_session(self, scan_options, url, task_id, max_depth, current_depth, session):
        import re
        from langchain.docstore.document import Document
        from bs4 import BeautifulSoup
        from app.utils.scraping_utils_manager.scraping_utils import ScrapingManager
        scraping_manager = ScrapingManager()
        pdf_pattern = re.compile(app_config.PDF_FILE_EXT_REGEX, re.IGNORECASE)
        file_pattern = re.compile(app_config.FILE_EXT_REGEX, re.IGNORECASE)

        html_content = await self.fetch_content(session, url, task_id)
        if not html_content:
            return []

        # Try lxml, fallback to html.parser
        try:
            soup = BeautifulSoup(html_content, 'lxml')
        except Exception as e:
            self.logger.error(f"lxml parser failed for {url}: {str(e)}. Falling back to html.parser")
            try:
                soup = BeautifulSoup(html_content, 'html.parser')
            except Exception as e:
                self.logger.error(f"html.parser failed for {url}: {str(e)}")
                await self.db.add_scraped_status(task_id, url, 'failed', f'Parsing failed: {str(e)}')
                return []
        
        current_domain = urlparse(url).netloc
        current_path = urlparse(url).path

        # Store the document if not in external_links mode
        if scan_options != 'external_links':
            text = soup.get_text()
            cleaned_text = scraping_manager.clean_html_text(text)
            advanced_cleaned_text = scraping_manager.advanced_clean_text(cleaned_text)
          
            if advanced_cleaned_text.strip():
                doc = Document(page_content=advanced_cleaned_text, metadata={"source": url, "task_id": task_id})
                await self.store_document(doc, task_id)
                await self.db.add_scraped_status(task_id, url, 'uploaded', None)
            else:
                await self.db.add_scraped_status(task_id, url, 'failed', 'Empty content after cleaning')

        # Extract and process links
        tasks = []
        links = [urljoin(url, a.get('href')) for a in soup.find_all('a', href=True)]

        if scan_options == 'external_links':
            # Process all links to handle PDFs and external links
            for link in links:
                next_url, _ = urldefrag(link)
                next_domain = urlparse(next_url).netloc
                
                # Skip if it's not a valid URL or has no domain
                if not next_domain:
                    continue
                
                # Handle PDF files
                if pdf_pattern.search(next_url.lower()):
                    pdf_filename = next_url.split('/')[-1]
                    await self.db.add_website_pdf_file(task_id, next_url, pdf_filename)
                    await self.db.add_scraped_status(task_id, next_url, 'failed', error="It is a PDF file", reason="PDF files are not scraped.")
                    continue
                
                # Filter valid external links for scraping
                if (next_domain != current_domain and
                    not file_pattern.search(next_url) and
                    not next_url.startswith('#') and
                    not await self.is_visited(next_url, task_id)):
                    await self.db.add_external_link(task_id, url, next_url, next_domain)
                    tasks.append(self.scrape_website('single_page', next_url, task_id, 0, 0, session=session))

        elif scan_options == 'full_page':
            # Process all links to handle PDFs and same-domain links
            for link in links:
                next_url, _ = urldefrag(link)
                # Handle PDF files
                if pdf_pattern.search(next_url.lower()):
                    pdf_filename = next_url.split('/')[-1]
                    await self.db.add_website_pdf_file(task_id, next_url, pdf_filename)
                    await self.db.add_scraped_status(task_id, next_url, 'failed', error="It is a PDF file", reason="PDF files are not scraped.")
                    continue
                # Filter valid same-domain links for scraping
                if (urlparse(next_url).netloc == current_domain and
                    not file_pattern.search(next_url) and
                    not next_url.startswith('#') and
                    not await self.is_visited(next_url, task_id)):
                    tasks.append(self.scrape_website(scan_options, next_url, task_id, max_depth, current_depth + 1, session=session))

        elif scan_options == 'nested_page':
            # Process all links to handle PDFs and same-domain subdirectory links
            for link in links:
                next_url, _ = urldefrag(link)
                next_path = urlparse(next_url).path
                # Handle PDF files
                if pdf_pattern.search(next_url.lower()):
                    pdf_filename = next_url.split('/')[-1]
                    await self.db.add_website_pdf_file(task_id, next_url, pdf_filename)
                    await self.db.add_scraped_status(task_id, next_url, 'failed', error="It is a PDF file", reason="PDF files are not scraped.")
                    continue
                # Filter valid same-domain subdirectory links for scraping
                if (urlparse(next_url).netloc == current_domain and
                    next_path.startswith(current_path) and
                    next_path != current_path and
                    not file_pattern.search(next_url) and
                    not next_url.startswith('#') and
                    not await self.is_visited(next_url, task_id)):
                    tasks.append(self.scrape_website(scan_options, next_url, task_id, max_depth, current_depth + 1, session=session))

        elif scan_options == 'single_page':
            # No links to follow
            pass

        else:
            # Default: Process all links to handle PDFs and same-domain links
            for link in links:
                next_url, _ = urldefrag(link)
                # Handle PDF files
                if pdf_pattern.search(next_url.lower()):
                    pdf_filename = next_url.split('/')[-1]
                    await self.db.add_website_pdf_file(task_id, next_url, pdf_filename)
                    await self.db.add_scraped_status(task_id, next_url, 'failed', error="It is a PDF file", reason="PDF files are not scraped.")
                    continue
                # Filter valid same-domain links for scraping
                if (urlparse(next_url).netloc == current_domain and
                    not file_pattern.search(next_url) and
                    not next_url.startswith('#') and
                    not await self.is_visited(next_url, task_id)):
                    tasks.append(self.scrape_website(scan_options, next_url, task_id, max_depth, current_depth + 1, session=session))

        # Run tasks concurrently
        try:
            await asyncio.gather(*tasks, return_exceptions=True)
        except Exception as e:
            await self.db.add_scraped_status(task_id, url, 'failed', error=str(e), reason="Exception during scraping.")

        # Update scraping progress
        async with self.lock:
            self.scraped_urls += 1
            await scraping_manager.update_scraping_progress(task_id, self.scraped_urls, 0)

        return []  # Documents are stored in DB, no need to return