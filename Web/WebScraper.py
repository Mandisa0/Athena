import requests
from html.parser import HTMLParser

response = requests.get("https://www.enca.com/")
print("Status Code:", response.status_code)
if response.status_code == 200:
    print("Successfully fetched the webpage.")
    print("Content:", response.text[:1000])  # Print the first 1000 characters of the content