from vec_db.BaseVecDB import BaseVecDB;
from typing import List
from langchain_core.documents import Document
import chromadb


class ChromaVecDB(BaseVecDB):
    def __init__(self, name:str):
        super().__init__()
        self.CHROMA_DB_DIR = f"./{name}"
        client = chromadb.PersistentClient(path=self.CHROMA_DB_DIR)
        self.collection = client.get_or_create_collection(name)

    def add_documents(self,documents: List[Document]):
        doc_id=0
        for doc in documents:
            doc_id+=1
            print(f"Size of the doc: {len(doc.page_content)}")
            self.collection.add(ids=[str(doc_id)], documents=[doc.page_content])
    
    def get_related_data(self, query:List[str], n_results:int = 10):
        return self.collection.query(query_texts=query, n_results=n_results)
