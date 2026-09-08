from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


class Vectorstore:
    def __init__(self,collection_name):
        self.embedding = HuggingFaceEmbeddings(
                model_name="BAAI/bge-small-zh-v1.5"
            )
        self.vectorstore = Chroma(
            collection_name=collection_name,
            embedding_function=self.embedding,
            persist_directory="./chroma_db"
        )

    def create_vectorstore(self,chunk):
        self.vectorstore.add_documents(chunk)
        return self.vectorstore

    def load_vectorstore(self):
        return self.vectorstore
