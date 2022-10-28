import requests
from bs4 import BeautifulSoup

# SCRAPING DU PREMIER PRODUIT LA PAGE N°1
url = 'http://books.toscrape.com/'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

products = soup.findAll('article', class_='product_pod')
# récupérer le titre du livre
title = products[0].find('h3').find('a').get('title')
# récupérer l'image du livre
image = products[0].find(
    'div', class_='image_container').find('img').get('src')
# récupérer la note du livre
rating = products[0].find('p', class_='star-rating')['class'][1]
# récupérer le prix du livre
price = products[0].find('div', class_='product_price').find(
    'p', class_='price_color').text.strip()
# récupérer le stock du livre
stock = products[0].find('div', class_='product_price').find(
    'p', class_='instock availability').text.strip()
# récupérer le lien du livre
link = products[0].find('h3').find('a').get('href')

print('Title: ', title)
print('Image: ', image)
print('Rating: ', rating)
print('Price: ', price)
print('Stock: ', stock)
print('Link: ', link)

     # stocké les données dans un fichier csv
with open('books.csv', 'a') as csv_file:
         writer = csv.writer(csv_file)
         writer.writerow([title, image, rating, price, stock, link])

print('---------------------------------------')
















 
 