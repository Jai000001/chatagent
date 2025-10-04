from langchain_text_splitters import RecursiveCharacterTextSplitter
import tiktoken

# Singleton for text splitting
class SharedTextSplitter:
    def __init__(self, chunk_size=500, chunk_overlap=100):
        #self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

        # Define token-based length function
        def token_length(text: str) -> int:
            encoding = tiktoken.get_encoding("cl100k_base")  # For text-embedding-3-large
            return len(encoding.encode(text))

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=token_length,
            separators=["\n\n", "\n", "<br />", " ", ""],  # Respect HTML and section boundaries
            keep_separator=True,
        )

    def split_documents(self, docs):
        import logging
        result = self.text_splitter.split_documents(docs)
        logging.info(f"Split {len(docs)} docs into {len(result)} chunks")
        return result

shared_text_splitter = SharedTextSplitter()
