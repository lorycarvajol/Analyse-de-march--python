import requests
from bs4 import BeautifulSoup
import csv


url = "http://books.toscrape.com/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


def scrape_book_page(url):
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
    table = soup.find('table', class_='table table-striped')
    rows = table.find_all('tr')
    upc = rows[0].find('td').text
    product_type = rows[1].find('td').text
    price_excluding_tax = rows[2].find('td').text
    price_including_tax = rows[3].find('td').text
    tax = rows[4].find('td').text
    availability = rows[5].find('td').text
    print(upc, product_type, price_excluding_tax,
          price_including_tax, tax, availability)
    return [url, upc, title, price, price, stock, description, category, rating, image_url]

# scrape du livre a light in the attic


url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
scrape_book_page(url)

# print the data in a csv file

with open('books.csv', 'w', encoding='utf-8-sig', newline='') as f:

    writer = csv.writer(f)
    writer.writerow(['product_page_url', 'universal_product_code',
                     'title', 'price_including_tax', 'price_excluding_tax',
                     'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
    writer.writerow(scrape_book_page(url))
