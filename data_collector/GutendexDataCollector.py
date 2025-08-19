import requests
from data_collector.BaseDataCollector import BaseDataCollector
from typing import List
from data_model.wwi_data_model import WWIDataModel 

class GutendexDataCollector(BaseDataCollector):
    def get_data(self):

        url = "https://gutendex.com/books/?topic=world%20war%20I"
        response = requests.get(url)
        data = response.json()
        data_result : List[WWIDataModel] = []

        for result in data['results']:
            text_plain_url = result['formats']["text/plain; charset=us-ascii"]
            title = result['title']
            if text_plain_url:
                text_result = requests.get(text_plain_url)
                wwi_book_text = text_result.text
                wwi_data_model = WWIDataModel(title=title, text=wwi_book_text)
                data_result.append(wwi_data_model)

        return data_result