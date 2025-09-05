import cloudscraper
from bs4 import BeautifulSoup
import json
import time

scrapper = cloudscraper.create_scraper()
href_list = [ ]


for i in range(0, 6):
    url = f"https://digitalarchive.wilsoncenter.org/search?f[0]=topics:86411&fo[0]=86411&page={i}"

    response = scrapper.get(url)

    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    table = soup.find("table", class_="table table-hover table-striped")

    list_of_rows = table.find_all('a')

    for anchor in list_of_rows:
        href_list.append(anchor['href'])

    time.sleep(15)



file_name = "hrefs.json"
with open(file_name, 'w') as f:
    json.dump(href_list, f, indent=4)
print(f"Hrefs saved to {file_name}")








# print(list_of_rows)