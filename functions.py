def get_brand(soup):

    product_brand = soup.find_all("th", class_="andes-table__header")
    if len(product_brand) == 0:
        product_brand = ""
    else:
        for x in product_brand:
            if x.text == "Marca":
                product_brand = x.find_next_sibling("td").text
                break
    return product_brand