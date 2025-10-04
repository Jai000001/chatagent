import os
from langchain.docstore.document import Document
from typing import List
import re
from app.core.logger import Logger
logger = Logger.get_logger(__name__)

class FileProcessor:
    def __init__(self, upload_dir="uploads"):
        self.upload_dir = upload_dir
        if not os.path.exists(self.upload_dir):
            os.makedirs(self.upload_dir)
        self.psm_config = '--psm 6'
        self.min_text_length = 5
        self.max_width = 1000
        
        from app.adapters.file_parsers.pdf_parser import PDFParser
        from app.adapters.file_parsers.doc_parser import DOCParser
        from app.adapters.file_parsers.ppt_parser import PPTParser
        from app.adapters.file_parsers.txt_parser import TXTParser
        self.parsers = {
            ".pdf": PDFParser(),
            ".docx": DOCParser(),
            ".doc": DOCParser(),
            ".ppt": PPTParser(),
            ".pptx": PPTParser(),
            ".txt": TXTParser()
        }

    async def load_file_async(self, file_path, docs, filename):
        #try:
        file_text = self._load_file(file_path, filename)
        if isinstance(file_text, list):
            # Already a list of Document objects
            docs.extend(file_text)
        else:
            # Single string (fallback for PDF, DOC, etc.)
            docs.append(Document(page_content=str(file_text), metadata={"source": filename}))
        # except Exception as e:
        #     logger.error(f"Cannot process file, Exception while loading file: {e}")

    async def _load_file(self, file_path: str, filename: str):
        extension = os.path.splitext(filename)[1].lower()
        parser = self.parsers.get(extension)

        if not parser:
            logger.error(f"Unsupported file type: {extension}")
            return None

        return await parser.load_async(file_path)

    def cleanup_files(self, file_paths: List[str]):
        for _, path in file_paths:
            try:
                if os.path.exists(path):
                    os.remove(path)
                    logger.info(f"Deleted file: {path}")
                else:
                    logger.warning(f"File not found during cleanup: {path}")
            except Exception as e:
                logger.warning(f"Could not remove file {path}: {e}")

    def secure_filename(self, filename: str) -> str:
        filename = os.path.basename(filename)
        filename = re.sub(r"[^A-Za-z0-9_.-]", "_", filename)
        return filename
