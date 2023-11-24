
def get_location(soup):
    
    location = soup.find_all("p", class_="ui-pdp-color--GRAY ui-pdp-family--REGULAR ui-pdp-media__text")
    for x in location:
        if x.text != "":
            location = x.text
            break
    return location


def get_brand(soup):

    product_brand = soup.find_all("th", class_="andes-table__header")
    if len(product_brand) == 0:
        product_brand = ""
    else:
        for x in product_brand:
            if x.text == "Marca":
                product_brand = x.find_next_sibling("td").text
                return product_brand
        product_brand = ""
    return product_brand

def get_linea(soup):
    
    product_linea = soup.find_all("th", class_="andes-table__header")
    if len(product_linea) == 0:
        product_linea = ""
    else:
        for x in product_linea:
            if x.text == "Línea":
                product_linea = x.find_next_sibling("td").text
                break
        product_linea = ""
    return product_linea

def get_model(soup):
    
    product_model = soup.find_all("th", class_="andes-table__header")
    if len(product_model) == 0:
        product_model = ""
    else:
        for x in product_model:
            if x.text == "Modelo":
                product_model = x.find_next_sibling("td").text
                break
        product_model = ""
    return product_model
