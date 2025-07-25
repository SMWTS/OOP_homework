import pytest

from src.product_and_category import Category, Smartphone, LawnGrass

def test_smartphone_addition():
    s1 = Smartphone("iPhone", "Apple", 100000, 2, "Высокая", "iPhone 13", "128GB", "Black")
    s2 = Smartphone("Samsung", "Samsung", 90000, 3, "Средняя", "Galaxy S21", "256GB", "White")
    s3 = Smartphone("Nokia", "Nokia", 30000, 1, "Низкая", "Nokia 3310", "N/A", "Blue")
    combined = s1 + s2
    assert isinstance(combined, Smartphone)
    assert combined.quantity == 5
    assert combined.price == max(s1.price, s2.price)

def test_lawngras_addition():
    lawn1 = LawnGrass("Газон 1", "Газон для дачи", 200, 10, "Россия", 14, "Зеленый")
    lawn2 = LawnGrass("Газон 2", "Газон для парка", 250, 5, "Россия", 10, "Зеленый")
    combined = lawn1 + lawn2
    assert isinstance(combined, LawnGrass)
    assert combined.quantity == 15
    assert combined.price == max(lawn1.price, lawn2.price)

def test_type_error_on_mixed_add():
    s = Smartphone("iPhone", "Apple", 100000, 2, "Высокая", "iPhone 13", "128GB", "Black")
    lawn = LawnGrass("Газон", "Газон для дачи", 200, 10, "Россия", 14, "Зеленый")
    with pytest.raises(TypeError):
        _ = s + lawn

def test_add_product_type_check():
    category = Category("Техника", "Все для техники")
    with pytest.raises(TypeError):
        category.add_product("не продукт")
    with pytest.raises(TypeError):
        category.add_product(123)
