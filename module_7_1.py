
from pprint import pprint

def check(search_product, shop_product):
    for i in shop_product:
        if str(search_product) == str(i):
            return 1
    return 0

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self, *args):
        file = open(self.__file_name, 'r')
        return file.read()

    def add(self, *products):

        products_in_shop = self.get_products().split('\n')


        file = open(self.__file_name, 'a')
        for i in products:
            if check(i, products_in_shop) == 1:
                print(f'Продукт {i} уже есть в магазине')
            else:
                file.write(str(i) + '\n')
        file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())