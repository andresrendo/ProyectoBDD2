import requests
from bs4 import BeautifulSoup
import sys

url = "https://listado.mercadolibre.com.ve/_Deal_especial-computacion-y-gaming-laptops#deal_print_id=91429510-7f5d-11ee-bbf1-7343fc42acdc&c_id=special-withoutlabel&c_element_order=1&c_campaign=LAPTOPS&c_uid=91429510-7f5d-11ee-bbf1-7343fc42acdc"


sys.stdout.reconfigure(encoding='utf-8')

while True:
    req = requests.get(url)

    soup = BeautifulSoup(req.text, "html.parser")
    product_List = soup.find_all("div", class_="ui-search-result__content-wrapper")
    # print(product_List)

    

    for product in product_List:
        product_name = product.find("h2", class_="ui-search-item__title")
        product_price = product.find("span", class_="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript")
        # print(product_price.text)
        # print(product_name.text)

        print(f'''
        Product: {product_name.text}
        Price: {product_price.text}
        ''')
    
    siguiente_enlace = soup.select(".andes-pagination__button--next a")


    if siguiente_enlace:
        siguiente_enlace = siguiente_enlace[0]["href"]
        url = siguiente_enlace
    else:
        break
    