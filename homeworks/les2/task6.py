'''
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
'''


products = []
id = 0

while True:
    count_products = input('Введите количество товаров: ')
    if count_products.isdigit():
        count_products = int(count_products)
        break
    else:
        print('Введите число!')


while count_products:
    products.insert(id, (id+1, {"название": input("Введите название: "), "цена": input("Введите цену: "),
                                "количество": input('Введите количество: '), "ед": input('Введите еденицы измерения: ')}))
    id += 1
    count_products -=1

print(products)

'''
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
 например название, а значение — список значений-характеристик, например список названий товаров.
'''

prod_name = []
price = []
count = []
unit = []


for id, dictenary in products:
    print(dictenary)
    print(dictenary.get("название"))
    prod_name.append(dictenary.get("название"))
    price.append(dictenary.get("цена"))
    count.append(dictenary.get("количество"))
    unit.append(dictenary.get("ед"))


product_dictenary = {"название": prod_name, "цена": price,"количество": count, "ед": unit}

print(product_dictenary)