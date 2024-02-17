import unittest
from main import Category, Product

class TestCategory(unittest.TestCase):
    def test_category_initialization(self):
        category = Category("Electronics")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, '')
        self.assertEqual(category.products, [])

    def test_category_add_product(self):
        category = Category("Electronics")
        product = Product("Laptop", 1500.0, 10)
        category.add_product(product)
        self.assertIn(product, category.products)

if __name__ == '__main__':
    unittest.main()
