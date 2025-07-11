import pytest

from src.product_and_category import Category, Product


@pytest.fixture(autouse=True)
def reset_counters() -> None:
    # Перед каждым тестом сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product() -> Product:
    return Product("Test Product", "Test Description", 99.99, 10)


@pytest.fixture
def multiple_products() -> list:
    p1 = Product("Product 1", "Desc 1", 50.0, 5)
    p2 = Product("Product 2", "Desc 2", 150.0, 3)
    return [p1, p2]


def test_product_initialization(product: Product) -> None:
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 99.99
    assert product.quantity == 10


def test_category_initialization_single_product(product: Product) -> None:
    category = Category("Test Category", "Test Category Description", [product])
    assert category.name == "Test Category"
    assert category.description == "Test Category Description"
    assert len(category.products) == 1
    assert category.products[0] == product
    # Проверка счетчиков
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_category_initialization_multiple_products(multiple_products: list) -> None:
    category = Category("Multiple Products", "Description", multiple_products)
    assert len(category.products) == 2
    assert all(p in category.products for p in multiple_products)
    # Проверка счетчиков
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_counts_accumulate() -> None:
    p1 = Product("P1", "D1", 10.0, 1)
    p2 = Product("P2", "D2", 20.0, 2)
    cat1 = Category("Cat1", "Desc1", [p1])
    cat2 = Category("Cat2", "Desc2", [p2])
    # После создания двух категорий
    assert Category.category_count == 2
    # Общее количество продуктов
    assert Category.product_count == 2
