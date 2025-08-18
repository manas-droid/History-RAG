from abc import ABC, abstractmethod
import re
from data_model.wwi_data_model import WWIDataModel
from typing import List

class BaseDataCollector(ABC):
    @abstractmethod
    def get_data(self)->List[WWIDataModel]:
        pass

    def clean_text(self,text:str):
        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
