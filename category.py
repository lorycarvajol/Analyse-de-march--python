import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/catalogue/category/books/poetry_23/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.find('h3').find('a')['title']
    price = book.find('div', class_='product_price').find(
        'p', class_='price_color').text
    stock = book.find('div', class_='product_price').find(
        'p', class_='instock availability').text.strip()
    url = book.find('h3').find('a')['href']
    print(title, price, stock, url)
