import os


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def __eq__(self, other):
        return self.name == other.name and self.weight == other.weight and self.category == other.category


class Shop:
    __file_name = 'products.txt'

    def _check_and_create_products_file(self):
        if not os.path.isfile(self.__file_name):
            fs = open(self.__file_name, 'w')
            fs.close()
            return False
        return True

    def _read_products(self):
        if self._check_and_create_products_file():
            fs = open(self.__file_name, 'r')
            products = []
            for line in fs.read().split('\n'):
                words = line.split(', ')
                if len(words) == 3:
                    name, weight, category = words[0], float(words[1]), words[2]
                    products.append(Product(name, weight, category))
            return products
        return []

    def get_products(self):
        products = self._read_products()
        text = ''
        for product in products:
            text += f'{str(product)}\n'
        return text

    def add(self, *products):
        self._check_and_create_products_file()
        shop_products = self._read_products()
        fs = open(self.__file_name, 'a')
        for product in products:
            if product not in shop_products:
                fs.seek(0, 2)
                fs.write(f'{str(product)}\n')
            else:
                print(f'{str(product)} уже есть в магазине')


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
