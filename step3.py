import requests
from bs4 import BeautifulSoup
import csv


url = "http://books.toscrape.com/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


categories = soup.find('ul', class_='nav nav-list').find_all('li')
categories_urls = []
for category in categories:
    categories_urls.append('http://books.toscrape.com/' +
                           category.find('a')['href'])
print(categories_urls)


for category_url in categories_urls:
    page = requests.get(category_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    category_name = soup.find('li', class_='active').text

    books = soup.find_all('h3')

    def get_book_info(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find('h1').text
        table = soup.find('table', class_='table table-striped')
        rows = table.find_all('tr')
        upc = rows[0].find('td').text

        price_excluding_tax = rows[2].find('td').text
        price_including_tax = rows[3].find('td').text
        availability = rows[5].find('td').text
        image_url = soup.find('div', class_='item active').find(
            'img')['src']  # recup chemin absolu voir plus bas
        print(image_url)
        return [url, upc, title,   price_including_tax, price_excluding_tax, availability,

                # recup product descrip, review rating

                image_url]




    # with open('categories/' + category_name + '.csv', 'w', encoding='utf-8-sig', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['product_page_url', 'universal_product_code', 'title', 'price_including_tax',
    #                     'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
    #     for book in books:
    #         url = 'http://books.toscrape.com/catalogue/' + \
    #             book.find('a')['href'].replace('../', '')
    #         writer.writerow(get_book_info(url))
