import unittest
from main import Category, Product

class TestCategory(unittest.TestCase):
    def test_category_initialization(self):
        category = Category("Electronics", "Category for electronic devices")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, "Category for electronic devices")
        self.assertEqual(category.products, [])

    def test_category_add_product(self):
        category = Category("Electronics", "Category for electronic devices")
        product = Product("Laptop", 1500.0, 10)
        category.add_product(product)
        self.assertIn(product, category.products)

class TestProduct(unittest.TestCase):
    def test_product_initialization(self):
        product = Product("Laptop", 1500.0, 10)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 1500.0)
        self.assertEqual(product.quantity, 10)
        self.assertIsNone(product.category)

    def test_create_product_class_method(self):
        product_data = {
            "name": "Tablet",
            "price": 1000.0,
            "quantity": 5,
            "category": "Electronics"
        }
        product = Product.create_product(**product_data)
        self.assertEqual(product.name, "Tablet")
        self.assertEqual(product.price, 1000.0)
        self.assertEqual(product.quantity, 5)
        self.assertEqual(product.category, "Electronics")

if __name__ == '__main__':
    unittest.main()
