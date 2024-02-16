class Category:
    total_categories = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.total_categories += 1

    def add_product(self, product):
        self.__products.append(product)

    @property
    def products(self):
        return self.__products



class Product:
    total_unique_products = 0

    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        Product.total_unique_products += 1

    @classmethod
    def create_product(cls, name, price, quantity, category):
        return cls(name, price, quantity, category)




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

