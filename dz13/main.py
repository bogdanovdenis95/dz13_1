class Category:
    def __init__(self, name, description=''):
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def __str__(self):
        products_info = '\n'.join(
            [f"Product: {product.name}\nPrice: {product.price}\nQuantity: {product.quantity}\n" for product in
             self.products])
        return f"Category: {self.name}\nDescription: {self.description}\nProducts: {products_info}"


class Product:
    def __init__(self, name, price, quantity, category=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    @classmethod
    def create_product(cls, name, price, quantity, category=None):
        return cls(name, price, quantity, category)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be non-negative")
        self._price = value

    def __str__(self):
        return f"Product: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\nCategory: {self.category.name if self.category else None}"


# Пример использования классов
if __name__ == "__main__":
    # Создаем категорию
    electronics_category = Category("Electronics")

    # Создаем продукты
    laptop = Product("Laptop", 1500.0, 10, electronics_category)
    smartphone = Product("Smartphone", 1000.0, 20, electronics_category)

    # Добавляем продукты в категорию
    electronics_category.add_product(laptop)
    electronics_category.add_product(smartphone)

    # Выводим информацию о категории и ее продуктах
    print(electronics_category)
