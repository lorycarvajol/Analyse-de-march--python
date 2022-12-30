import requests
from bs4 import BeautifulSoup
import csv
import os


url = "http://books.toscrape.com/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


categories = soup.find('ul', class_='nav nav-list').find_all('li')
categories_urls = []
for category in categories:
    categories_urls.append('http://books.toscrape.com/' +
                           category.find('a')['href'])


def get_books_urls(category_url):
    page = requests.get(category_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    books = soup.find_all('h3')
    books_urls = []
    for book in books:
        books_urls.append('http://books.toscrape.com/catalogue/' +
                          book.find('a')['href'].replace('../', ''))
    return books_urls


def get_book_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('h1').text
    price = soup.find('p', class_='price_color').text
    stock = soup.find('p', class_='instock availability').text
    stock = stock.strip()
    stock = stock.replace('In stock (', '')
    stock = stock.replace(' available)', '')
    stock = int(stock)

    description = soup.find(
        'div', id='product_description')
    if description:
        description = description.find_next_sibling('p').text

    category = soup.find('ul', class_='breadcrumb').find_all('li')[2].text
    upc = soup.find('td').text
    rating = soup.find('p', class_='star-rating')['class'][1]
    rating = rating.replace('One', '1')
    rating = rating.replace('Two', '2')
    rating = rating.replace('Three', '3')
    rating = rating.replace('Four', '4')
    rating = rating.replace('Five', '5')
    rating = int(rating)
    image = soup.find('img')['src']
    image = image.replace('../../', 'http://books.toscrape.com/')
    return {
        'product_page_url': url,
        'universal_product_code': upc,
        'title': title,
        'price_including_tax': price,
        'price_excluding_tax': price,
        'number_available': stock,
        'product_description': description,
        'category': category,
        'review_rating': rating,
        'image_url': image
    }


for category_url in categories_urls:
    page = requests.get(category_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    category_name = soup.find('li', class_='active').text
    books_urls = get_books_urls(category_url)
    print(category_name)

    if not os.path.exists('categories/' + category_name):
        os.makedirs('categories/' + category_name)
    with open('categories/' + category_name + '/books.csv', 'w', encoding='utf-8-sig', newline='') as csvfile:
        fieldnames = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax',
                      'number_available', 'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.DictWriter(
            csvfile,  fieldnames=fieldnames)
        writer.writeheader()
        for book_url in books_urls:
            print(book_url)
            book_info = get_book_info(book_url)
            writer.writerow(book_info)
