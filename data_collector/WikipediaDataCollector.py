import data_collector.BaseDataCollector as bdc
import requests
from typing import List
from data_model.wwi_data_model import WWIDataModel
import time


titles = ["World War 1", "The Great War", "1914-1918", "First World War"]

class WikipediaDataCollector(bdc.BaseDataCollector):
    def __init__(self):
        self.WIKI_API_URL =  "https://en.wikipedia.org/w/api.php"
        self.HEADERS = {"User-Agent": "WWI-RAG-Bot/1.0 (email)"}

    def get_data(self):
        all_wiki_page_titles = set()

        for title in titles:
            time.sleep(0.5)
            all_wiki_page_titles.update(self.get_wiki_titles(title))

        result: List[WWIDataModel] = []
        for title in all_wiki_page_titles:
            time.sleep(0.5)
            text_output = self.get_wiki_text(title)
            wiki_dict: WWIDataModel = WWIDataModel(title,super().clean_text(text_output))
            result.append(wiki_dict)

        return result



    def get_wiki_titles(self,query):
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "srlimit": 20 
        }
        resp = requests.get(self.WIKI_API_URL, params=params, headers=self.HEADERS)
        resp.raise_for_status()
        return [item["title"] for item in resp.json()["query"]["search"]]
    
    def get_wiki_text(self,title):
        params = {
            "action": "query",
            "prop": "extracts",
            "explaintext": True,
            "titles": title,
            "format": "json"
        }
        resp = requests.get(self.WIKI_API_URL, params=params,headers=self.HEADERS)
        resp.raise_for_status()
        pages = resp.json()["query"]["pages"]
        return list(pages.values())[0].get("extract", "")
    


