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

    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        return NotImplemented

# Классы-наследники
class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Можно складывать только объекты одного типа")
        # Можно реализовать логику сложения, например, объединение количества
        new_quantity = self.quantity + other.quantity
        # Можно выбрать более высокую цену
        new_price = max(self._price, other._price)
        return Smartphone(
            self.name,
            self.description,
            new_price,
            new_quantity,
            self.efficiency,
            self.model,
            self.memory,
            self.color
        )

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Можно складывать только объекты одного типа")
        new_quantity = self.quantity + other.quantity
        new_price = max(self._price, other._price)
        return LawnGrass(
            self.name,
            self.description,
            new_price,
            new_quantity,
            self.country,
            self.germination_period,
            self.color
        )
def __add__(self, other):
    if type(self) != type(other):
        raise TypeError("Можно складывать только объекты одного типа")

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        self.product_count = len(self.__products)
        Category.category_count += 1
        Category.product_count += self.product_count

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        # Проверка, что объект является наследником Product
        if not issubclass(type(product), Product):
            raise TypeError("Объект должен быть наследником класса Product")
        self.__products.append(product)
        self.product_count += 1

    @property
    def products(self):
        return "\n".join(
            f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт."
            for prod in self.__products
        )

    def __str__(self):
        return f"Категория: {self.name}\nОписание: {self.description}\nТовары:\n{self.products}"