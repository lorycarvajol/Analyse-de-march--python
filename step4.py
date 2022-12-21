import requests
from bs4 import BeautifulSoup
import os

url = "http://books.toscrape.com/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


# créer un dossier nommé categorie à la racine du projet

os.mkdir("test")
