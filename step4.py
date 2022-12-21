import requests
from bs4 import BeautifulSoup
import os


url = "http://books.toscrape.com/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


categories = soup.find('ul', class_='nav nav-list').find_all('li')
categories_urls = []
for category in categories:
    categories_urls.append('http://books.toscrape.com/' +
                           category.find('a')['href'])


# get all books urls from a category


def get_books_urls(category_url):
    page = requests.get(category_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    books = soup.find_all('h3')
    books_urls = []
    for book in books:
        books_urls.append('http://books.toscrape.com/catalogue/' +
                          book.find('a')['href'].replace('../', ''))
    return books_urls


# scrape book info from a book url


def get_book_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('h1').text
    image_url = soup.find('div', class_='item active').find(
        'img')['src']

    return [url, title,  image_url]

# create a folder for each category and download all books images in it


for category_url in categories_urls:
    page = requests.get(category_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    category_name = soup.find('li', class_='active').text
    books_urls = get_books_urls(category_url)
    for book_url in books_urls:
        book_info = get_book_info(book_url)
        image_url = book_info[2]
        image_name = image_url.split('/')[-1]
        if not os.path.exists('categories/' + category_name):
            os.makedirs('categories/' + category_name)
        with open('categories/' + category_name + '/' + image_name, 'wb') as f:
            f.write(requests.get(image_url).content)


# if not os.path.exists('categories/' + category_name):
#     os.makedirs('categories/' + category_name)
