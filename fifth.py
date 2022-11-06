import requests
from bs4 import BeautifulSoup
import csv

# definir constante html.parser



url = 'http://books.toscrape.com/'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# calculer le nombre d'article par page

products = soup.findAll('article', class_='product_pod')
nb_products = len(products)
print('Nombre d\'articles par page: ', nb_products)

# récupérer le nombre de pages
pages = soup.find('ul', class_='pager').findAll('li')
nb_pages = len(pages) - 2

# récupérer le nombre d'article total
nb_total_products = soup.find('form', class_='form-horizontal').find(
     'strong').text
print('Nombre d\'articles total: ', nb_total_products)

# récupérer le nombre de pages total
nb_total_pages = int(nb_total_products) // int(nb_products)
print('Nombre de pages total: ', nb_total_pages)

# récupérer les données de chaque article
for page in range(1, nb_total_pages + 1):
     url = 'http://books.toscrape.com/catalogue/page-' + str(page) + '.html'
     page = requests.get(url)
     soup = BeautifulSoup(page.content, 'html.parser')
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
          

        #scraping des données de chaque livre
        
          url = 'http://books.toscrape.com/catalogue/' + link
          page = requests.get(url)
          soup = BeautifulSoup(page.content, 'html.parser')
          upc = soup.find('table', class_='table table-striped').findAll('td')[0].text
          product_type = soup.find('table', class_='table table-striped').findAll('td')[1].text
          price_excluding_tax = soup.find('table', class_='table table-striped').findAll('td')[2].text
          price_including_tax = soup.find('table', class_='table table-striped').findAll('td')[3].text
          tax = soup.find('table', class_='table table-striped').findAll('td')[4].text
          availability = soup.find('table', class_='table table-striped').findAll('td')[5].text
          number_of_reviews = soup.find('table', class_='table table-striped').findAll('td')[6].text
         
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

# création header csv


         




