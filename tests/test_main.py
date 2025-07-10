import pytest
class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Category:
    category_count = 0  # Атрибут класса для подсчета категорий
    product_count = 0    # Атрибут класса для подсчета товаров

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products  # список объектов Product

        # Обновляем счетчики при создании нового объекта
        Category.category_count += 1
        Category.product_count += len(products)

# Фикстуры для тестирования
@pytest.fixture
def sample_product():
    return Product("Книга", "Учебник по программированию", 1500.50, 10)

@pytest.fixture
def sample_category():
    product1 = Product("Книга", "Учебник по программированию", 1500.50, 10)
    product2 = Product("Ручка", "Гелевая ручка", 50.75, 100)
    return Category("Канцтовары", "Все для учебы и работы", [product1, product2])

def test_product_initialization(sample_product):
    assert sample_product.name == "Книга"
    assert sample_product.description == "Учебник по программированию"
    assert sample_product.price == 1500.50
    assert sample_product.quantity == 10

def test_category_initialization(sample_category):
    assert sample_category.name == "Канцтовары"
    assert sample_category.description == "Все для учебы и работы"
    assert len(sample_category.products) == 2

def test_counts_after_creation():
    # Перед созданием новых объектов
    initial_categories = Category.category_count
    initial_products = Category.product_count

    p1 = Product("Тетрадь", "Тетрадь в клетку", 30.0, 50)
    c1 = Category("Канцтовары", "Все для учебы", [p1])

    assert Category.category_count == initial_categories + 1
    assert Category.product_count == initial_products + 1
