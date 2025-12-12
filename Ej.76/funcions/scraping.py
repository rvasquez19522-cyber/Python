# funcions/scraping.py
import requests
from bs4 import BeautifulSoup

def scraping_pagina():
    url = 'https://www.uib.cat/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraer el título de la página
    print(f"Título de la página: {soup.title.string}")
