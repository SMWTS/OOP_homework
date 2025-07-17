import pytest

from src.product_and_category import Category, Product


@pytest.fixture
def sample_product():
    return Product("Телевизор", "Большой экран", 30000, 5)


@pytest.fixture
def sample_category():
    product1 = Product("Книга", "Учебник по программированию", 1500.50, 10)
    product2 = Product("Ручка", "Гелевая ручка", 50.75, 100)
    return Category("Канцтовары", "Все для учебы и работы", [product1, product2])


def test_add_product(sample_category):
    new_product = Product("Мышь", "Беспроводная мышь", 2000, 15)
    initial_count = sample_category.product_count
    sample_category.add_product(new_product)
    assert sample_category.product_count == initial_count + 1
    products_str = sample_category.products
    # Проверяем наличие названия
    assert "Мышь" in products_str
    # Проверяем наличие цены
    assert "2000" in products_str


def test_products_property_returns_string():
    product1 = Product("Книга", "Учебник", 1500.50, 10)
    product2 = Product("Ручка", "Гелевая ручка", 50.75, 100)
    category = Category("Канцтовары", "Все для учебы", [product1, product2])
    products_str = category.products
    assert isinstance(products_str, str)
    assert "Книга" in products_str
    assert "Ручка" in products_str
    assert "Остаток: 10 шт." in products_str
    assert "Остаток: 100 шт." in products_str


def test_private_products_list_is_protected():
    product1 = Product("Книга", "Учебник", 1500.50, 10)
    category = Category("Канцтовары", "Все для учебы", [product1])
    # Попытка доступа к приватному списку напрямую вызовет AttributeError
    with pytest.raises(AttributeError):
        _ = category.__products


def test_product_count_initial_and_after_add():
    product1 = Product("Книга", "Учебник", 1500.50, 10)
    category = Category("Канцтовары", "Все для учебы", [product1])
    initial_count = category.product_count
    new_product = Product("Ручка", "Гелевая ручка", 50.75, 100)
    category.add_product(new_product)
    assert category.product_count == initial_count + 1


def test_total_counts():
    initial_total_categories = Category.category_count
    initial_total_products = Category.product_count
    p1 = Product("Тетрадь", "В клетку", 30, 50)
    c1 = Category("Канцтовары", "Все для учебы", [p1])
    assert Category.category_count == initial_total_categories + 1