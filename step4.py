import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


images = soup.find_all('img')
for image in images:
    print(image['src'])
