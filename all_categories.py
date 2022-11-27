import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/catalogue/category/books/poetry_23/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
books = soup.find_all('article', class_='product_pod')


categories = soup.find('ul', class_='nav nav-list').find_all('li')[1:]
for category in categories:
    category_name = category.find('a').text
    print(category_name)

# write al categories in csv file
with open('categories.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['category_name'])
    writer.writerow([category_name])
