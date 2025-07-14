class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data: dict, existing_products: list = None):
        existing_products = existing_products or []
        for prod in existing_products:
            if prod.name == data.get('name'):
                prod.quantity += data.get('quantity', 0)
                if data.get('price') > prod._price:
                    prod._price = data.get('price')
                return prod
        return cls(
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price'),
            quantity=data.get('quantity')
        )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевой или отрицательной")
        else:
            if hasattr(self, '_price') and value < self._price:
                confirm = input(f"Вы хотите понизить цену с {self._price} до {value}. Подтвердите (y/n): ")
                if confirm.lower() == 'y':
                    self._price = value
                else:
                    print("Понижение цены отменено.")
            else:
                self._price = value


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        self.product_count = len(self.__products)  # добавляем атрибут для количества товаров
        Category.total_categories += 1
        Category.total_products += self.product_count

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1
            Category.total_products += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")


    @property
    def products(self):
        return "\n".join(
            f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт."
            for prod in self.__products
        )
