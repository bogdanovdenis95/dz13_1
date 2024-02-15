class Category:
    total_categories = 0
    categories = set()

    def __init__(self, name):
        self.name = name
        self.__products = []  # Список товаров в категории
        Category.categories.add(name)
        Category.total_categories = len(Category.categories)

    def add_product(self, product):
        self.__products.append(product)

    def get_products(self):
        return self.__products



class Product:
    total_unique_products = 0

    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        Product.total_unique_products += 1
        category.add_product(self)


    @classmethod
    def create_product(cls, name, price, quantity):
        return cls(name, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Ошибка: Цена должна быть больше нуля.")

    @price.deleter
    def price(self):
        del self.__price
        print("Атрибут 'price' удален.")

