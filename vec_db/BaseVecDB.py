from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class BaseVecDB(ABC):
    @abstractmethod
    def add_documents(documents: List[Document]):
        pass

    def get_related_data(query:str, n_results:int = 10):
        pass