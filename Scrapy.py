import requests
from bs4 import BeautifulSoup
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import functions as f

# URI connection to MongoDB Atlas
uri = "mongodb+srv://juanraque:Jc30213659@cluster0.rnw7ssa.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

url = "https://celulares.mercadolibre.com.ve/_NoIndex_True"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}


sys.stdout.reconfigure(encoding='utf-8')

while True:
    req = requests.get(url)

    soup = BeautifulSoup(req.text, "html.parser")
    product_List = soup.find_all("div", class_="ui-search-result__content-wrapper")

    siguiente_enlace = soup.select(".andes-pagination__button--next a")

    for product in product_List:

        product_link = product.find("a", class_="ui-search-item__group__element").get("href")
        
        #Configurar el navegador
        driver = webdriver.Chrome()
        driver.get(product_link)
        driver.maximize_window()

        #Esperar a que cargue la pagina
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[title='Ver todas las características']")))
        
        #driver.implicitly_wait(5)
        #specifications_btn = driver.find_element(By.CSS_SELECTOR, "svg[class='ui-pdp-icon--chevron-down']")
        print(element.text)
        print("hola")
        #specifications_btn.click()

        #Obtener el html
        html = driver.page_source
        driver.quit()

        #req = requests.get(product_link)        
        soup = BeautifulSoup(html, "html.parser")

        product_name = soup.find("h1", class_="ui-pdp-title").text
        product_price = float(soup.find("meta", itemprop="price").get("content"))          
        product_location = f.get_location(soup)
        product_brand = f.get_brand(soup)
        #product_linea = f.get_linea(soup)
        #product_model = f.get_model(soup)

        
        # Insert data into MongoDB Atlas
        #client.get_database("test").get_collection("test").insert_one({
        #    "Nombre": product_name,
        #    "Precio": product_price,
        #    "Ubicacion": product_location
        #})

        print(f"""
        Nombre: {product_name}
        Precio: {product_price}
        Ubicacion: {product_location}
        Marca: {product_brand}
        """)
    

    if siguiente_enlace:
        siguiente_enlace = siguiente_enlace[0].get("href")
        url = siguiente_enlace
    else:
        break

print("fin del programa")
