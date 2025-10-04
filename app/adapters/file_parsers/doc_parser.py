from app.core.logger import Logger
logger = Logger.get_logger(__name__)
from docx import Document as DocxDocument

class DOCParser:
    def __init__(self):
        self.psm_config = '--psm 6'
        self.min_text_length = 5
        self.max_width = 1000

    async def load_async(self, file_path):
        # try:
        import mammoth
        # Convert .doc to .docx if needed
        if file_path.lower().endswith('.doc'):
            file_path = self._convert_doc_to_docx(file_path)
        # Extract raw text using mammoth
        result = mammoth.extract_raw_text(file_path)
        text = result.value
        # Extract image text (sync, but can be offloaded)
        loop = None
        try:
            import asyncio
            loop = asyncio.get_running_loop()
        except RuntimeError:
            import asyncio
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        image_text = await loop.run_in_executor(None, self._extract_text_from_doc_images, file_path)
        return text + "\n" + image_text
        # except Exception as e:
        #     logger.error(f"Exception while loading doc: {e}")
        #     return ""

    def _convert_doc_to_docx(self, input_file):
        try:
            import aspose.words as aw
            output_file = input_file.rsplit('.', 1)[0] + '.docx'
            doc = aw.Document(input_file)
            doc.save(output_file, aw.SaveFormat.DOCX)
            return output_file
        except Exception as e:
            logger.error(f"Exception while converting doc to docx: {e}")
            return input_file

    def _extract_text_from_doc_images(self, file_path):
        # try:
        from concurrent.futures import ThreadPoolExecutor, as_completed
        doc = DocxDocument(file_path)
        image_parts = [rel.target_part for rel in doc.part.rels.values() if "image" in rel.target_ref]
        with ThreadPoolExecutor() as executor:
            future_to_image = {executor.submit(self._process_image, img_part, idx): idx
                            for idx, img_part in enumerate(image_parts, start=1)}
            results = []
            for future in as_completed(future_to_image):
                idx = future_to_image[future]
                text = future.result()
                if text:
                    results.append(f"Image {idx}:\n{text}")
        return "\n\n".join(results)
        # except Exception as e:
        #     logger.error(f"Exception while extracting text from doc image: {e}")
        #     return ""

    def _process_image(self, img_part, idx):
        # try:
        import io, cv2, numpy as np, pytesseract
        img = Image.open(io.BytesIO(img_part.blob))
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        img_cv = self._downscale_image(img_cv)
        preprocessed_images = [
            self._preprocess_default(img_cv),
            self._preprocess_adaptive(img_cv),
            self._preprocess_color_filter(img_cv)
        ]
        all_texts = []
        for preprocessed in preprocessed_images:
            text = pytesseract.image_to_string(preprocessed, config=self.psm_config)
            if len(text.strip()) >= self.min_text_length:
                all_texts.append(text.strip())
        text = pytesseract.image_to_string(img_cv, config=self.psm_config)
        if len(text.strip()) >= self.min_text_length:
            all_texts.append(text.strip())
        return "\n".join(set(all_texts)) if all_texts else ""
        # except Exception as e:
        #     logger.error(f"Exception while process image: {e}")
        #     return ""

    def _preprocess_default(self, img):
        # try:
        import cv2
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        denoised = cv2.fastNlMeansDenoising(gray)
        return cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        # except Exception as e:
        #     logger.error(f"Exception while preprocess default image: {e}")
        #     return img

    def _preprocess_adaptive(self, img):
        # try:
        import cv2
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        # except Exception as e:
        #     logger.error(f"Exception while preprocess adaptive image: {e}")
        #     return img

    def _preprocess_color_filter(self, img):
        # try:
        import cv2, numpy as np
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        return cv2.bitwise_not(mask)
        # except Exception as e:
        #     logger.error(f"Exception while preprocess color filter image: {e}")
        #     return img

    def _downscale_image(self, img, max_width=1500):
        # try:
        import cv2
        height, width = img.shape[:2]
        if width > max_width:
            scale = max_width / width
            new_height = int(height * scale)
            return cv2.resize(img, (max_width, new_height), interpolation=cv2.INTER_AREA)
        return img
        # except Exception as e:
        #     logger.error(f"Exception while downscale image: {e}")
        #     return img
