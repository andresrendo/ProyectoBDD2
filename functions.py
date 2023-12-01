


def get_location(soup):
    
    location = soup.find_all("p", class_="ui-pdp-color--GRAY ui-pdp-family--REGULAR ui-pdp-media__text")

    if len(location) == 0:
        return "No disponible"
    
    for x in location:
        if x.text != "":
            location = x.text
            return location


def get_brand(soup):
    marcas_telefonos = [
    "Samsung",
    "Xiaomi",
    "Apple",
    "Huawei",
    "Iphone",
    "Redmi",
    "iPhone",
    "Técno",
    "Tecno",
    "Infinix",
    "Techo",
    "Hk8",
    "Umidigi",
    "Logic",
    "BLU",
    "Motorola",
    "Infinix",
    "Panita",
    "Alcatel",
    "Android",
    "Honor",
    "Huawei",
    "LG",
    "Sony",
    "BLU",
    "Galaxy",
    "Hyundai",
    "HTC"   ,   
    "Haier",
    "Movistar",
    "Microsoft",
    "Nexus",
    "Otros",
    "Phillips",
    "Razer",
    "Siragon",
    "Sky",
    "Skyworth",
    "Toshiba",
    "Vtelca",
    "Zonda",
    "ZTE",
    "Acer",
    "Ainol",
    "Airis",
    "Sansung",
    "AOC",
    "TCL",
    "T-Mobile",
    "Vivo",
    "Yezz",
    "Yoobao",
    "Uniwa"
    "Nokia",
    "Oppo",
    "Asus",
    "Lenovo",
    "ZTE",
    "HTC",
    "Honor",
    "Meizu",
    "Google",
    "OnePlus",
    "Realme",
    "Vivo",
    "BlackBerry",
    "Cat",
    "Doogee",
    "Gigabyte",
    "Hisense",
    "JBL",
    "LeEco",
    "Panasonic",
    "Philips",
    "Razer",
    "Sharp",
    "TCL",
    "Vodafone",
    "Wiko",
    "Xolo",
    "Yota",
    "Zopo"
]
    nombre = soup.find("h1", class_="ui-pdp-title").text
    nombre = nombre.split()
    for x in nombre:
        if x in marcas_telefonos:
            if x == "iPhone":
                return "Apple"
            elif x == "Iphone":
                return "Apple"
            elif x == "Galaxy":
                return "Samsung"
            elif x == "Sansung":
                return "Samsung"
            elif x == "Técno":
                return "Tecno"
            elif x == "Redmi":
                return "Xiaomi"
            else:
                return x
                
    return "Otros"


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
        num_ventas = None
        for x in ventas:
            a += 1
            if a == 3:
                num_ventas = int(x.text)
                break

        if num_ventas == None or len(ventas) == 0:
            num_ventas = "No disponible"
        return num_ventas

def get_recomendacion(soup):
    a = 0
    recomendacion_arr = soup.find_all("strong", class_="ui-pdp-seller__sales-description")
    recomendacion = None
    for x in recomendacion_arr:
        a += 1
        if a == 1:
            recomendacion = int(x.text.replace("%", ""))
            break

    if recomendacion == None or len(recomendacion_arr) == 0:
        recomendacion = "No disponible"
    return recomendacion
        
def get_aniosExp(soup):
    a = 0
    aniosExp_arr = soup.find_all("strong", class_="ui-pdp-seller__sales-description")
    aniosExp = None
    for x in aniosExp_arr:
        a += 1
        if a == 2:
            aniosExp = x.text.split()
            if aniosExp[1] == "meses" or aniosExp[1] == "mes":
                aniosExp = int(aniosExp[0])/12
                aniosExp = round(aniosExp, 1)
            else:
                aniosExp = float(aniosExp[0])
            break
    
    if aniosExp == None or len(aniosExp_arr) == 0:
        aniosExp = "No disponible"
    return aniosExp
        
def get_vendidos(soup):
    estadisticas_arr = soup.find_all("span", class_="ui-pdp-subtitle")
    cantidad_vendidos = None
    for x in estadisticas_arr:
        if x.text != "":
            estadisticas = x.text
            cantidad_vendidos= ""
            for letra in estadisticas:
                if letra == "|":
                    cantidad_vendidos = int(estadisticas.split("|")[1].strip().split()[0])
                    break

    if cantidad_vendidos == None or len(estadisticas_arr) == 0:
        cantidad_vendidos = "No disponible"
    
    return cantidad_vendidos
        
def get_estado(soup):
    estado = soup.find_all("span", class_="ui-pdp-subtitle")
    for x in estado:
        if x.text != "":
            estado = x.text
            for letra in estado:
                if letra == "|":
                    estado = estado.split("|")[0]
                    return estado.strip()

def get_vendedor(soup):
    vendedor = soup.find_all("span", class_="ui-pdp-color--BLUE ui-pdp-family--REGULAR")
    for x in vendedor:
        if x.text != "":
            vendedor = x.text
            return vendedor
        else:
            vendedor = ""
            return vendedor