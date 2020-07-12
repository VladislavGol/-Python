quantity = int(input("Введите количество товаров: "))
products_list = []

for i in range(0, quantity):
    product_name = input(f"Введите название {i + 1}-ого товара: ")
    product_price = int(input("Введите цену на данный товар: "))
    product_quantity = int(input("Введите количество данного товара: "))
    product_unit = input("Введите единицу измерения данного товара: ")
    product_info_dict = {"название": product_name, "цена": product_price, "количество": product_quantity, "ед.": product_unit}
    product_info_tuple = (i + 1, product_info_dict)
    products_list.append(product_info_tuple)

list_names = []
list_prices = []
list_quantity = []
list_units = []

for i in range(0, quantity):
    list_names.append(products_list[i][1].get("название"))

for i in range(0, quantity):
    list_prices.append(products_list[i][1].get("цена"))

for i in range(0, quantity):
    list_quantity.append(products_list[i][1].get("количество"))

for i in range(0, quantity):
    list_units.append(products_list[i][1].get("ед."))

info_dict = {
    "название": list_names,
    "цена": list_prices,
    "количество": list_quantity,
    "ед.": list_units
}

print(info_dict)
