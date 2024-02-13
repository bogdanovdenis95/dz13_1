class Category:
    total_categories = 0
    total_unique_products = set()

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

    def add_product(self, product):
        self.products.append(product)
        Category.total_unique_products.add(product.name)


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity



category1 = Category("Electronics", "Electronic devices")
category2 = Category("Clothing", "Clothing items")

product1 = Product("Laptop", "High-performance laptop", 1500.0, 10)
product2 = Product("T-shirt", "Cotton T-shirt", 20.0, 100)

category1.add_product(product1)
category2.add_product(product2)


print("Total categories:", Category.total_categories)
print("Total unique products:", len(Category.total_unique_products))
