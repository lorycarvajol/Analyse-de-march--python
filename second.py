import requests
from bs4 import BeautifulSoup

#SCRAPING DU PREMIER PRODUIT LA PAGE N°2

url = 'http://books.toscrape.com/catalogue/page-2.html'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

products = soup.findAll('article', class_='product_pod')

title = products[0].find('h3').find('a').get('title')
image = products[0].find('div', class_='image_container').find('img').get('src')
rating = products[0].find('p', class_='star-rating')['class'][1]
price = products[0].find('div', class_='product_price').find('p', class_='price_color').text.strip()
stock = products[0].find('div', class_='product_price').find('p', class_='instock availability').text.strip()
link = products[0].find('h3').find('a').get('href')

print('Title: ', title)
print('Image: ', image)
print('Rating: ', rating)
print('Price: ', price)
print('Stock: ', stock)
print('Link: ', link)


