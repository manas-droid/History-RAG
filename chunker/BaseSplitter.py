
from typing import List
from langchain_core.documents import Document
from abc import ABC, abstractmethod



class BaseSplitter(ABC):
    @abstractmethod
    def get_chunks(self, texts:List[str])->List[Document]:
        pass