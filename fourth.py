import requests
from bs4 import BeautifulSoup
import csv

# Récupérer les données de tout les produits de toutes les pages

url = 'http://books.toscrape.com/'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

products = soup.findAll('article', class_='product_pod')

for product in products:
     title = product.find('h3').find('a').get('title')
     image = product.find('div', class_='image_container').find('img').get('src')
     rating = product.find('p', class_='star-rating')['class'][1]
     price = product.find('div', class_='product_price').find('p', class_='price_color').text.strip()
     stock = product.find('div', class_='product_price').find('p', class_='instock availability').text.strip()
     link = product.find('h3').find('a').get('href')
     
     print('Title: ', title)
     print('Image: ', image)
     print('Rating: ', rating)
     print('Price: ', price)
     print('Stock: ', stock)
     print('Link: ', link)

with open('books.csv', 'a') as csv_file:
         writer = csv.writer(csv_file)
         writer.writerow([title, image, rating, price, stock, link])
         
print('---------------------------------------')