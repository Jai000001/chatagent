from app.core.logger import Logger
logger = Logger.get_logger(__name__)
from langchain_community.document_loaders import PyMuPDFLoader
import fitz
from PIL import Image
import pytesseract
import io

class PDFParser:
    def __init__(self):
        pass

    async def load_async(self, file_path):
        # try:
            import asyncio
            loader = PyMuPDFLoader(file_path)
            docs = loader.load()
            text = "\n".join(doc.page_content for doc in docs)
            loop = asyncio.get_running_loop()
            image_text = await loop.run_in_executor(None, self._extract_text_from_images, file_path)
            return text + "\n" + image_text
        # except Exception as e:
        #     logger.error(f"Exception while loading pdf: {e}")
        #     return ""

    def _extract_text_from_images(self, file_path):
        """Extract text from images in the PDF using OCR."""
        # try:
        image_text = ""
        pdf_document = fitz.open(file_path)
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                img = Image.open(io.BytesIO(image_bytes))
                image_text += pytesseract.image_to_string(img) + "\n"

        pdf_document.close()
        return image_text
        # except Exception as e:
        #     logger.error(f"Exception while extracting text from image: {e}")

    def count_pages_bytes(self, pdf_bytes):
        """Count the number of pages in a PDF from bytes."""
        try:
            import fitz
            import io
            pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
            num_pages = pdf_document.page_count
            pdf_document.close()
            return num_pages
        except Exception as e:
            logger.error(f"Exception while counting pages from bytes: {e}")
            return 0

    async def load_bytes_async(self, pdf_bytes, url):
        """
        Asynchronously load PDF from bytes, extract text and page count.
        Returns (doc, num_pages)
        """
        import asyncio
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, self._load_bytes_sync, pdf_bytes, url)

    def _load_bytes_sync(self, pdf_bytes, url):
        """
        Synchronous helper to extract text and page count from PDF bytes.
        """
        try:
            import fitz
            pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
            num_pages = pdf_document.page_count
            text = ""
            for page in pdf_document:
                text += page.get_text()
            pdf_document.close()
            return text, num_pages
        except Exception as e:
            logger.error(f"Exception while loading PDF bytes for {url}: {e}")
            return "", 0        
