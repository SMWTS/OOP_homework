import pytest

from src.product_and_category import Category, Product


@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra", "Флагманский смартфон", 79999.0, 5)


@pytest.fixture
def product2():
    return Product("Iphone 15", "Новый айфон", 99999.0, 3)


@pytest.fixture
def product3():
    return Product("Xiaomi Redmi Note 11", "Бюджетный смартфон", 15000.0, 20)


@pytest.fixture
def category1(product1, product2, product3):
    cat = Category("Смартфоны", "Все виды смартфонов", [product1, product2, product3])
    return cat


def test_product_str(product1, product2, product3):
    s1 = str(product1)
    s2 = str(product2)
    s3 = str(product3)
    assert "Samsung Galaxy S23 Ultra" in s1
    assert "Iphone 15" in s2
    assert "Xiaomi Redmi Note 11" in s3


def test_category_str(category1):
    s = str(category1)
    assert "Смартфоны" in s
    # Проверка, что список товаров содержит название одного из продуктов
    assert "Samsung Galaxy S23 Ultra" in category1.products
    assert "Iphone 15" in category1.products
    assert "Xiaomi Redmi Note 11" in category1.products


def test_products_property(category1):
    products_str = category1.products
    assert "Samsung Galaxy S23 Ultra" in products_str
    assert "Iphone 15" in products_str
    assert "Xiaomi Redmi Note 11" in products_str


def test_add_product(category1, product1):
    new_product = Product("OnePlus 11", "8GB RAM, 256GB Storage", 65000.0, 10)
    initial_count = category1.product_count
    category1.add_product(new_product)
    assert category1.product_count == initial_count + 1
    products_str = category1.products
    assert "OnePlus 11" in products_str


def test_product_plus(product1, product2):
    sum_price = product1 + product2
    expected = product1.price * product1.quantity + product2.price * product2.quantity
    assert sum_price == expected


def test_protected_products(category1):
    with pytest.raises(AttributeError):
        _ = category1.__products


def test_product_add_with_non_product():
    p = Product("Товар", "Описание", 100, 2)
    result = p.__add__(123)
    assert result is NotImplemented
