import requests
from bs4 import BeautifulSoup
import sys
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import time

# URI connection to MongoDB Atlas
uri = "mongodb+srv://juanraque:Jc30213659@cluster0.rnw7ssa.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

url = "https://celulares.mercadolibre.com.ve/_NoIndex_True"
detail_links = []


sys.stdout.reconfigure(encoding='utf-8')

while True:
    req = requests.get(url)

    soup = BeautifulSoup(req.text, "html.parser")
    product_List = soup.find_all("div", class_="ui-search-result__content-wrapper")
    #print(product_List)
    

    for product in product_List:

        #product_name = product.find("h2", class_="ui-search-item__title")
        #product_price = product.find("span", class_="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript")

        product_link = product.find("a", class_="ui-search-item__group__element")
        detail_links.append(product_link.get("href"))        
    
    for link in detail_links:
        req = requests.get(link)
        soup = BeautifulSoup(req.text, "html.parser")

        product_name = soup.find("h1", class_="ui-pdp-title").text
        product_price = float(soup.find("meta", itemprop="price").get("content"))          
        product_location = soup.find("p", class_="ui-pdp-media__text").text 

        # Insert data into MongoDB Atlas
        #client.get_database("test").get_collection("test").insert_one({
        #    "Nombre": product_name,
        #    "Precio": product_price,
        #    "Ubicacion": product_location
        #})

        print(f"""
        Nombre: {product_name}
        Precio: {product_price}
        Ubicacion: {product_location}""")

    siguiente_enlace = soup.select(".andes-pagination__button--next a")

    if siguiente_enlace:
        siguiente_enlace = siguiente_enlace[0]["href"]
        url = siguiente_enlace
    else:
        break
