import hashlib
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

class ScrapingManager:
    def __init__(self):
        pass

    @staticmethod
    async def compute_scraping_content_hash(content: str) -> str:
        """Async compute SHA-256 hash of normalized content."""
        # Split content into sentences for better duplicate detection
        sentences = content.split('.')
        normalized_sentences = [
            ' '.join(sentence.lower().split())
            for sentence in sentences if sentence.strip()
        ]
        normalized_sentences.sort()
        normalized_content = '.'.join(normalized_sentences)
        return hashlib.sha256(normalized_content.encode('utf-8')).hexdigest()

    async def is_duplicate_scraping(self, doc, client_id: str, ttl: int = 8 * 3600) -> bool:
        """
        Async check if a document is a duplicate for a client using Redis set.
        Content hashes expire after the same duration as progress keys (default 8 hours).
        """
        try:
            from app.adapters.database.redisdb_handler import RedisDBHandler
            redis_handler = RedisDBHandler()
            content_hash = await self.compute_scraping_content_hash(doc.page_content)
            # Fast check in Redis set
            if await redis_handler.is_content_hash_duplicate(client_id, content_hash):
                logger.info(f"Duplicate detected for client_id={client_id}")
                return True
            # Not duplicate, add hash for future checks (with expiry)
            await redis_handler.add_content_hash(client_id, content_hash, ttl=ttl)
            return False
        except Exception as e:
            logger.error(f"Deduplication error: {e}")
            return False

    async def update_scraping_progress(self, task_id: str, scraped_urls: int, total_urls: int):
        """ Async function to update progress for website scraping. """
        from app.adapters.database.redisdb_handler import RedisDBHandler
        max_scraping_progress = 70
        min_increment = 1
        redis_handler = RedisDBHandler()

        if total_urls > 0:
            dynamic_increment = int(max(max_scraping_progress / total_urls, min_increment))
            current_progress = min(scraped_urls * dynamic_increment, max_scraping_progress)
        else:
            current_progress = max_scraping_progress

        current_data = await redis_handler.get_progress_from_store(task_id) or {}
        initial_progress = current_data.get("progress", 0)

        if current_progress > initial_progress:
            current_data["progress"] = current_progress
            await redis_handler.set_progress_in_store(task_id, current_data)
            logger.info(f"Progress for task {task_id}: {current_progress}%")

        if scraped_urls == total_urls:
            final_data = await redis_handler.get_progress_from_store(task_id) or {}
            final_data["progress"] = max_scraping_progress
            await redis_handler.set_progress_in_store(task_id, final_data)
            logger.info(f"Scraping completed for task {task_id}. Progress: {max_scraping_progress}%")

    def clean_html_text(self, text: str) -> str:
        import re
        # Remove leading/trailing whitespace
        text = text.strip()
        # Collapse multiple newlines into one
        text = re.sub(r'\n{2,}', '\n', text)
        # Remove lines that are just empty or spaces
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return '\n'.join(lines)

    def remove_xml_blocks(self, text):
        import re
        # Remove <x:xmpmeta ...>...</x:xmpmeta> and similar RDF/XML blocks
        text = re.sub(r'<x:xmpmeta[\\s\\S]*?</x:xmpmeta>', '', text, flags=re.IGNORECASE)
        text = re.sub(r'<rdf:RDF[\\s\\S]*?</rdf:RDF>', '', text, flags=re.IGNORECASE)
        return text    

    def remove_pdf_streams(self, text):
        import re
        # Remove everything between 'stream' and 'endstream'
        return re.sub(r'stream[\s\S]*?endstream', '', text, flags=re.IGNORECASE)
    
    def advanced_clean_text(self, text):
        import re
        import string

        # Step 1: Remove XML, PDF streams, script/style blocks and HTML comments
        text = self.remove_xml_blocks(text)
        text = self.remove_pdf_streams(text)
        text = re.sub(r'<style[\s\S]*?</style>', '', text, flags=re.IGNORECASE)
        text = re.sub(r'<script[\s\S]*?</script>', '', text, flags=re.IGNORECASE)
        text = re.sub(r'<!--[\s\S]*?-->', '', text, flags=re.MULTILINE)  # Remove HTML comments
        text = re.sub(r'/\*[\s\S]*?\*/', '', text, flags=re.MULTILINE)  # Remove CSS comments
        text = re.sub(r'<!$$ CDATA\[[\s\S]*? $$\]>', '', text, flags=re.MULTILINE)  # CDATA sections
        text = re.sub(r'<<[\s\S]*?>>', '', text)  # PDF dictionaries

        lines = text.splitlines()
        cleaned_lines = []
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Skip error messages, stack traces, and template code
            if re.search(
                r'(An error occurred while processing the template|Failed to \\"?eval|Syntax error|FTL stack trace|in template|end-message|stack trace|at line|at column|begin-message|end-message|Traceback|Exception|Error:)',
                line, re.IGNORECASE
            ):
                continue
            if re.match(r'^<#', line) or re.match(r'^<@', line) or re.match(r'^\s*//', line):
                continue

            # Skip HTML/CSS/JS code lines
            if re.match(r'^<[^>]+>$', line) or re.match(r'^\s*\w+\s*=.*;$', line) or re.match(r'^\s*\.[\w-]+\s*\{', line):
                continue

            # Skip PDF-specific markers
            if line.startswith('%PDF-') or line == '%%EOF' or line.endswith('obj') or line == 'endobj':
                continue
            if line in {'xref', 'trailer', 'startxref'}:
                continue
            if re.match(r'^\d{8,}\s+\d+\s+[nf]$', line):  # Strict PDF object table
                continue
            if re.match(r'^\d+\s+\d+\s+R$', line):  # Object reference
                continue
            if re.match(r'^<<.*>>$', line):  # Single-line PDF dictionary
                continue

            # Preserve lines with email-like patterns (e.g., [at], [dot])
            if re.search(r'\[at\]|\[dot\]', line):
                cleaned_lines.append(line)
                continue

            # Preserve lines with phone number patterns (international, US, and common delimiters)
            phone_regex = re.compile(r"""
                (?:\+\d{1,3}[\s-]?)?                 # Optional country code
                (?:\(\d{2,4}\)[\s-]?|\d{2,4}[\s-])? # Optional area code (with or without parens)
                \d{2,4}[\s.-]?\d{2,4}[\s.-]?\d{2,4} # Main number blocks (allows various splits)
                (?:\s*(?:ext|x|\#)\s*\d{1,6})?       # Optional extension
            """, re.VERBOSE)
            if phone_regex.search(line):
                cleaned_lines.append(line)
                continue

            # Skip lines with high density of PDF keys (e.g., /Key1 /Key2)
            if len(re.findall(r'/[A-Za-z0-9]+', line)) >= 4 and len(line) < 400:
                continue
            if re.match(r'^/\w+(\s+\d+\s+0\s+R)?$', line):  # /Key or /Key 123 0 R
                continue
            if re.match(r'^/\w+\(.*\)$', line):  # /Key(Value)
                continue
            if re.match(r'^/\w+(\[.*\])?$', line):  # /Key[...]
                continue
            if re.match(r'^/\w+<.*>$', line):  # /Key<...>
                continue
            if re.match(r'^/\w+\s+\d+$', line):  # /Key 123
                continue

            # Skip PDF signature or binary junk
            if line == '%âãÏÓ':
                continue
            printable = set(string.printable)
            num_printable = sum(1 for c in line if c in printable)
            if len(line) > 0 and num_printable / len(line) < 0.3:
                continue

            # Preserve lines with mixed content (names, dates, emails, etc.)
            if re.search(r'[A-Za-z]+\s+[A-Za-z]+.*\d{4}', line):  # Name and year (e.g., TUHIN KANTA PANDEY Mar 01, 2025)
                cleaned_lines.append(line)
                continue

            cleaned_lines.append(line)

        return '\n'.join(cleaned_lines)    