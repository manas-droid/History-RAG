import cloudscraper
from bs4 import BeautifulSoup
import json
import time

scrapper = cloudscraper.create_scraper()
document_list = []
base_url = "https://digitalarchive.wilsoncenter.org"


with open('hrefs.json', 'r') as file:
    data = json.load(file)
    for link in data:
        try: 
            response = scrapper.get(f'{base_url}{link}')
            soup = BeautifulSoup(response.text, 'html.parser')
            div_document = soup.find(class_='content-block') 
            document_html = soup.find(id='documentTabs')

            if document_html and div_document: 
                document = document_html.get_text()
                title = div_document.find(class_="title").get_text()
                date = div_document.find(class_="date").get_text()
                print("title", title, "date", date)

                document_list.append({
                    "title" : title,
                    "document" : document,
                    "date" : date,
                    "link": link
                })

            else:
                print(link, "Has NO DOCUMENT TAB")

        except:
            file_name = "docs.json"
            with open(file_name, 'w') as f:
                json.dump(document_list, f, indent=4)
        
        time.sleep(15)
        



file_name = "docs.json"

with open(file_name, 'w') as f:
    json.dump(document_list, f, indent=4)


print(f"documents saved to {file_name}")