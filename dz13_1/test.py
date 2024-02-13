import unittest
from main import Category, Product

class TestCategoryAndProduct(unittest.TestCase):
    def setUp(self):

        Category.total_categories = 0
        Category.total_unique_products = set()

    def test_category_initialization(self):
        category = Category("Electronics", "Electronic devices")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, "Electronic devices")
        self.assertEqual(category.products, [])
        self.assertEqual(Category.total_categories, 1)

    def test_product_initialization(self):
        product = Product("Laptop", "High-performance laptop", 1500.0, 10)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.description, "High-performance laptop")
        self.assertEqual(product.price, 1500.0)
        self.assertEqual(product.quantity, 10)

    def test_count_products_and_categories(self):
        category1 = Category("Electronics", "Electronic devices")
        category2 = Category("Clothing", "Clothing items")

        product1 = Product("Laptop", "High-performance laptop", 1500.0, 10)
        product2 = Product("T-shirt", "Cotton T-shirt", 20.0, 100)

        category1.add_product(product1)
        category2.add_product(product2)

        self.assertEqual(Category.total_categories, 2)
        self.assertEqual(len(Category.total_unique_products), 2)

if __name__ == '__main__':
    unittest.main()
