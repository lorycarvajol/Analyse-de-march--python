import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

products = soup.findAll('article', class_='product_pod')
nb_products = len(products)
print('Nombre d\'articles par page: ', nb_products)

pages = soup.find('ul', class_='pager').findAll('li')
nb_pages = len(pages) - 2

nb_total_products = soup.find('form', class_='form-horizontal').find(
    'strong').text
print('Nombre d\'articles total: ', nb_total_products)

nb_total_pages = int(nb_total_products) // int(nb_products)
print('Nombre de pages total: ', nb_total_pages)

for page in range(1, nb_total_pages + 1):
    products = soup.findAll('article', class_='product_pod')
    for product in range(0, len(products)):
        title = products[product].find('h3').find('a').get('title')
        image = products[product].find(
            'div', class_='image_container').find('img').get('src')
        rating = products[product].find(
            'p', class_='star-rating')['class'][1]
        price = products[product].find('div', class_='product_price').find(
            'p', class_='price_color').text.strip()
        stock = products[product].find('div', class_='product_price').find(
            'p', class_='instock availability').text.strip()
        link = products[product].find('h3').find('a').get('href')
        info_table = soup.find(
            'table', class_='table table-striped').findAll('td')
        upc = info_table[0].text
        product_type = info_table[1].text
        price_excluding_tax = info_table[2].text
        price_including_tax = info_table[3].text
        tax = info_table[4].text
        availability = info_table[5].text
        number_of_reviews = info_table[6].text

    # création header csv
    with open('books.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['title', 'image', 'rating', 'price', 'stock', 'link', 'upc', 'product_type',
                         'price_excluding_tax', 'price_including_tax', 'tax', 'availability', 'number_of_reviews'])

    with open('books.csv', 'a') as csv_file:

        writer = csv.writer(csv_file)
        writer.writerow([title, image, rating, price, stock, link, upc, product_type,
                         price_excluding_tax, price_including_tax, tax, availability, number_of_reviews])
        csv_file.close()
