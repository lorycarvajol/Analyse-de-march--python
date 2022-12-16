import requests
from bs4 import BeautifulSoup
import csv


url = "http://books.toscrape.com/catalogue/category/books/romance_8/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


books = soup.find_all('h3')
# for book in books:
#     # print(book.find('a')['href'].replace('../../', ''))


# books_urls = []


def get_book_info(url):

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('h1').text
    print(title)
    table = soup.find('table', class_='table table-striped')
    rows = table.find_all('tr')
    upc = rows[0].find('td').text
    product_type = rows[1].find('td').text
    price_excluding_tax = rows[2].find('td').text
    price_including_tax = rows[3].find('td').text
    tax = rows[4].find('td').text
    availability = rows[5].find('td').text
    image_url = soup.find('div', class_='item active').find('img')['src']
    print('image_url')
    return [url, upc, title, product_type, price_excluding_tax, price_including_tax, tax, availability, image_url]


with open('books_romance.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['product_page_url', 'universal_product_code', 'title', 'price_including_tax',
                    'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
# recup page n°1
    pages = soup.find('ul', class_='pager').find_all('li')
    pages_urls = []
    for page in pages:
        pages_urls.append('http://books.toscrape.com/catalogue/category/books/romance_8/' +
                          page.find('a')['href'])
    print(pages_urls)

# recup élément des bouquins
    # for book in books:
    #     url = 'http://books.toscrape.com/catalogue/' + \
    #         book.find('a')['href'].replace('../', '')
    #     print(url)
    #     writer.writerow(get_book_info(url))
