import requests
import re
from bs4 import BeautifulSoup
import json

marcas = [
    "samsumg",
    "motorola",
    "xiaomi",
    "iphone",
    "huawei",
]
def scrap(url):
    try:
        response = requests.get(url_dinamica)
        soup = BeautifulSoup(response.content, "html.parser")

        cards = soup.find_all("div", class_="poly-card poly-card--list")
        for card in cards:
            print(card)
    except Exception as e:
        print(e)

for marca in marcas:
    url_dinamica = f"https://listado.mercadolibre.com.ar/{marca}#D[A:{marca}]"
    scrap(url_dinamica)

