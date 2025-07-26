import pytest

from src.product_and_category import Category, Product


@pytest.fixture
def sample_products():
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    p3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return p1, p2, p3


@pytest.fixture
def sample_category(sample_products):
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        list(sample_products),
    )
    return category


def test_add_product_increases_count(sample_category):
    new_product = Product("Новый телефон", "Описание", 50000, 3)
    initial_count = sample_category.product_count
    sample_category.add_product(new_product)
    assert sample_category.product_count == initial_count + 1
    # Проверка, что товар добавился в строку
    products_str = sample_category.products
    assert "Новый телефон" in products_str


def test_products_property_returns_string(sample_category):
    output = sample_category.products
    # Проверка, что возвращается строка
    assert isinstance(output, str)
    # Проверка, что в строке есть название и цена
    for prod in sample_category._Category__products:
        assert prod.name in output
        assert str(prod.price) in output


def test_private_products_list_is_protected():
    category = Category("Test", "desc")
    with pytest.raises(AttributeError):
        _ = category.__products


def test_create_product_from_dict():
    data = {"name": "Test Phone", "description": "Test description", "price": 99999.0, "quantity": 10}
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Test Phone"
    assert product.price == 99999.0
    assert product.quantity == 10


def test_create_duplicate_product_increases_quantity():
    existing_products = [Product("Test Phone", "desc", 100000.0, 5)]
    data = {"name": "Test Phone", "description": "desc", "price": 95000.0, "quantity": 3}
    # Создаем или обновляем товар
    product = Product.new_product(data, existing_products)
    # Проверяем, что товар обновился
    assert product.quantity == 8  # 5 + 3
    # Цена должна остаться высокой
    assert product._price == 100000.0


def test_price_setter_rejects_zero_or_negative():
    product = Product("Test", "desc", 1000, 5)
    # Попытка установить отрицательную цену
    product.price = -10
    # Цена не должна измениться
    assert product.price == 1000
    # Попытка установить нулевую цену
    product.price = 0
    assert product.price == 1000


def test_price_setter_accepts_positive_and_confirm():
    product = Product("Test", "desc", 1000, 5)
    # Для теста замокаем input
    import builtins

    input_backup = builtins.input
    builtins.input = lambda prompt="": "y"
    product.price = 900  # понизить цену с подтверждением
    builtins.input = lambda prompt="": "n"
    product.price = 800  # отмена понижения
    builtins.input = input_backup
    # Проверяем, что цена изменилась только при подтверждении
    # В данном случае, цена должна быть 900, так как подтверждение было 'y'
    assert product.price == 900
