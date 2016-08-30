import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://creativeworks.tistory.com/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for title_list in soup.find_all(['h3', 'class']):
            href = url
            title = title_list.text
            print(href)
            print(title)

        #print(soup)
        page += 1

spider(10)
