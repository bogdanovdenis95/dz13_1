import unittest
from main import Category, Product


class TestCategory(unittest.TestCase):
    def test_category_initialization_without_description(self):

        category = Category("Electronics", "Description")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, "Description")

class TestProduct(unittest.TestCase):
    def test_create_product_class_method(self):
        category = Category("Электроника", "Товары электроники")
        product = Product.create_product("Планшет", 1000.0, 5, category)
        self.assertIsInstance(product, Product)


    def test_product_initialization(self):

        category = Category("Electronics", "Description")

        product = Product("Laptop", 1500.0, 10, category)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 1500.0)
        self.assertEqual(product.quantity, 10)

if __name__ == '__main__':
    unittest.main()
