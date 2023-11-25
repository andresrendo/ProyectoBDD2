


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


def get_ventas(soup):
        a = 0
        ventas = soup.find_all("strong", class_="ui-pdp-seller__sales-description")
        for x in ventas:
            a += 1
            if a == 3:
                ventas = x.text
                return ventas

def get_recomendacion(soup):
    a = 0
    recomendacion = soup.find_all("strong", class_="ui-pdp-seller__sales-description")
    for x in recomendacion:
        a += 1
        if a == 1:
            recomendacion = x.text
            return recomendacion
        
def get_aniosExp(soup):
    a = 0
    aniosExp = soup.find_all("strong", class_="ui-pdp-seller__sales-description")
    for x in aniosExp:
        a += 1
        if a == 2:
            aniosExp = x.text
            return aniosExp
        
def get_vendidos(soup):
    estadisticas = soup.find_all("span", class_="ui-pdp-subtitle")
    for x in estadisticas:
        if x.text != "":
            estadisticas = x.text
            cantidad_vendidos= ""
            for letra in estadisticas:
                if letra == "|":
                    cantidad_vendidos = estadisticas.split("|")[1]
            return cantidad_vendidos
        
def get_estado(soup):
    estado = soup.find_all("span", class_="ui-pdp-subtitle")
    for x in estado:
        if x.text != "":
            estado = x.text
            for letra in estado:
                if letra == "|":
                    estado = estado.split("|")[0]
                    return estado

def get_vendedor(soup):
    vendedor = soup.find_all("span", class_="ui-pdp-color--BLUE ui-pdp-family--REGULAR")
    for x in vendedor:
        if x.text != "":
            vendedor = x.text
            return vendedor
        else:
            vendedor = ""
            return vendedor