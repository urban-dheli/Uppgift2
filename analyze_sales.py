import csv
import os
import locale
from collections import Counter


def analyze_sales_data(filename):
    products = {} # bibliotek
    all_products = [] # lista

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row['Product']
            all_products.append(product)
            sales = float(row['Sales'])
            
            if product in products:
                products[product] += sales
            else:
                products[product] = sales
    
    # Hitta den mest sålda produkten
    most_sold_products = Counter(all_products).most_common(1)[0]
    product_count = most_sold_products[1]
        
    # Hitta den mest lukrativa produkten
    most_lucrative_product = max(products, key=products.get)
    
    # Genomsnittlig försäljning per produkt
    average_sales = sum(products.values()) / len(products)

    print(f"Mest sålda produkt: {most_sold_products[0]}, Antal: {product_count}")
    print(f"Mest lukrativa produkt: \"{most_lucrative_product}\" med försäljning på {locale.currency(products[most_lucrative_product],grouping=True)}")
    print(f"Genomsnittlig försäljning per produkt: {locale.currency(average_sales, grouping=True)}")


# Sätt språkinställning till svenska (Sverige) används för att skriva ut formaterad valuta
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls')
analyze_sales_data('sales_data.csv')
