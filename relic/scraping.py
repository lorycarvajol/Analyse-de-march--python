import requests
from bs4 import BeautifulSoup
import csv


url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find('h1').text
price = soup.find('p', class_='price_color').text
stock = soup.find('p', class_='instock availability').text.strip()
description = soup.find(
    'div', id='product_description').next_sibling.next_sibling.text.strip()
category = soup.find('ul', class_='breadcrumb').find_all('a')[2].text
rating = soup.find('p', class_='star-rating')['class'][1]
image_url = soup.find('div', class_='item active').find('img')['src']
print(title, price, stock, description, category)

table = soup.find('table', class_='table table-striped')

rows = table.find_all('tr')

for row in rows:
    key = row.find('th').text
    value = row.find('td').text
    print(key, value)

# with open('books.csv', 'w', encoding='utf-8-sig', newline='') as f:

#     writer = csv.writer(f)
#     writer.writerow(['product_page_url', 'universal_product_code',
#                      'title', 'price_including_tax', 'price_excluding_tax',
#                      'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
#     writer.writerow([url, upc, title, price, price, stock,
#                      ])
