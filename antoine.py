import requests
from bs4 import BeautifulSoup
import csv


def scrap_book(book_url):
    page = requests.get(book_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('h1').text
    price = soup.find('p', class_='price_color').text
    stock = soup.find('p', class_='instock availability').text.strip()
    description = soup.find(
        'div', id='product_description').next_sibling.next_sibling.text.strip()
    category = soup.find('ul', class_='breadcrumb').find_all('a')[2].text
    rating = soup.find('p', class_='star-rating')['class'][1]
    image_url = soup.find('div', class_='item active').find('img')['src']

    upc = soup.find('table', class_='table table-striped')[0].find('td').text

    return {
        upc,
        title,
        price,
        stock,
        description,
        category,
        rating,
        image_url
    }


def scrap_category(category_name, category_url):
    page = requests.get(category_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    books_info = []
