class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # приватный атрибут
        self.quantity = quantity

    @classmethod
    def new_product(cls, data: dict, existing_products: list = None):
        """
        Создает новый объект Product из словаря данных.
        Если товар с таким именем уже есть, увеличивает его количество,
        а при конфликте цен выбирает более высокую.
        """
        existing_products = existing_products or []
        for prod in existing_products:
            if prod.name == data.get("name"):
                # Обновляем количество
                prod.quantity += data.get("quantity", 0)
                # Выбираем более высокую цену
                if data.get("price", 0) > prod._price:
                    prod._price = data.get("price")
                return prod
        # Создаем новый товар, если дубликат не найден
        return cls(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            quantity=data.get("quantity"),
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        """
        Устанавливает цену товара.
        Если цена <= 0, выводит сообщение и не меняет цену.
        В случае понижения цены, запрашивает подтверждение у пользователя.
        """
        if value <= 0:
            print("Цена не должна быть нулевой или отрицательной")
        else:
            # Проверка на понижение цены
            if hasattr(self, "_price") and value < self.__price:
                confirm = input(f"Вы хотите понизить цену с {self._price} до {value}. Подтвердите (y/n): ")
                if confirm.lower() == "y":
                    self.__price = value
                else:
                    print("Понижение цены отменено.")
            else:
                self.__price = value


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []  # приватный список товаров
        self.product_count = len(self.__products)  # количество товаров в категории
        Category.category_count += 1
        Category.product_count += self.product_count

    def add_product(self, product):
        """
        Добавляет объект Product в категорию.
        Обновляет счетчик товаров.
        """
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        """
        Возвращает строку со списком товаров в формате:
        "Название, цена руб. Остаток: количество шт."
        """
        return "\n".join(f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт." for prod in self.__products)

    @property
    def products_list(self):
        # возвращает список товаров
        return self.__products
