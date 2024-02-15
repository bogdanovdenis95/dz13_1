import unittest
from main import Category, Product

class TestCategoryAndProduct(unittest.TestCase):
    def setUp(self):
        self.electronics = Category("Электроника")

    def test_count_products_and_categories(self):
        laptop = Product("Ноутбук", 1500, 10, self.electronics)  # Передаем аргумент 'category'
        self.assertEqual(Category.total_categories, 1, "Неправильное количество категорий после добавления продукта")

    def test_product_addition_with_same_name(self):
        laptop1 = Product("Ноутбук", 1500, 10, self.electronics)  # Передаем аргумент 'category'
        self.assertEqual(len(self.electronics.get_products()), 1, "Неправильное количество продуктов после добавления двух продуктов с одинаковым именем")

if __name__ == '__main__':
    unittest.main()
