import requests
import json
import cloudscraper
from bs4 import BeautifulSoup

scrapper = cloudscraper.create_scraper()
file_name = "docs.json"
base_url = 'https://digitalarchive.wilsoncenter.org'


with open(file_name, 'r') as f:
    data = json.load(f)
    for doc in data:
        document = doc['document'].replace('\n', '')
        link = doc['link']
        if not document:
            response = scrapper.get(f"{base_url}{link}")
            soup = BeautifulSoup(response.text, 'html.parser')
            pdf_obj = soup.find(class_='pdf-preview')
            if pdf_obj:
                pdf_url = pdf_obj['data']
                pdf_title = pdf_url.split('/')[-1]
                print(pdf_title)
                result = requests.get(f"{base_url}{pdf_url}")
                with open(f'./pdfs/{pdf_title}', 'wb') as f:
                    f.write(result.content)


# with open(file_name, 'r') as f:
#     data = json.load(f)

#     for doc in data:
#         document = doc['document'].replace('\n', '')
#         link = doc['link']
#         if not document:



# result = requests.get("https://digitalarchive.wilsoncenter.org/sites/default/files/shared-media/imported_document_original_file/1944_11_25__Wilgress_to_Secretary_of_State.pdf")

# with open('./pdfs/downloaded_document.pdf', 'wb') as f:
#     f.write(result.content)



