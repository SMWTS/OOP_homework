class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0  # Атрибут класса для подсчета категорий
    product_count = 0  # Атрибут класса для подсчета товаров

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products  # список объектов Product

        # Обновляем счетчики при создании нового объекта
        Category.category_count += 1
        Category.product_count += len(products)
