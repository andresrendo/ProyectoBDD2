import requests
from bs4 import BeautifulSoup
import sys

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
    
    siguiente_enlace = soup.select(".andes-pagination__button--next a")


    if siguiente_enlace:
        siguiente_enlace = siguiente_enlace[0]["href"]
        url = siguiente_enlace
    else:
        break

for link in detail_links:
    pass