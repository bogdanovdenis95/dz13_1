
class Category:
    def __init__(self, name, description='', products=None):
        self.name = name
        self.description = description
        self._products = products or []

    def add_product(self, product):
        self._products.append(product)

    @property
    def products(self):
        return self._products

    def __str__(self):
        product_names = [product.name for product in self.products]
        products_info = "\n".join(product_names)
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
        return f"Product: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}"


if __name__ == "__main__":
    electronics_category = Category("Electronics", "Category for electronic devices")
    laptop = Product("Laptop", 1500.0, 10, electronics_category)
    smartphone = Product("Smartphone", 1000.0, 20, electronics_category)

    print(electronics_category)
    print(laptop)
    print(smartphone)
