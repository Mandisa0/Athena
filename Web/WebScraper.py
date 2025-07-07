import requests
import json
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url, tag = 'p', parent_attr = 'article', parent_attr_value = ''):
        self.url = url
        self.tag = tag
        self.parent_attr = parent_attr
        self.parent_attr_value = parent_attr_value

    def fetch_content(self):
        response = requests.get(self.url)
        print("Status Code:", response.status_code)
        scrape_response = ''

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all(self.tag)
            for paragraph in paragraphs:
                if self.parent_attr in paragraph.parent.attrs:
                    if paragraph.parent.attrs[self.parent_attr] == self.parent_attr_value:
                        scrape_response += paragraph.getText()
        
        return scrape_response
