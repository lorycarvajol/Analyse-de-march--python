import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.find_all('p', class_='price_color')

#return universal_product_code

def get_product_name(soup):
    return soup.find('h1').text



    
    
    


    
 
 
 




    
    return soup

print (get_soup(url))