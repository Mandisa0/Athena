import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url

    def fetch_content(self):
        response = requests.get(self.url)
        print("Status Code:", response.status_code)
        scrape_response = ''

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')  # Get a slice of the text content
            paragraphs = soup.find_all('p')
            for paragraph in paragraphs:
                if 'data-component' in paragraph.parent.attrs:
                    scrape_response += paragraph.getText()
        
        return scrape_response
    
# a = WebScraper('https://www.bbc.com/news/articles/cp9005z1pljo')
# print(a.fetch_content())