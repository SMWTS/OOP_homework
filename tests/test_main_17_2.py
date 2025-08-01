import pytest

from src.product_and_category import Category, Product


def test_average_price_with_no_products():
    category = Category("Пустая категория", "Нет товаров")
    assert category.average_price() == 0


def test_average_price_with_products():
    p1 = Product("Товар1", "Описание", 100, 10)
    p2 = Product("Товар2", "Описание", 200, 5)
    category = Category("Категория", "Описание", [p1, p2])
    assert category.average_price() == 150


def test_create_product_with_zero_quantity():
    with pytest.raises(ValueError):
        Product("Товар", "Описание", 100, 0)
