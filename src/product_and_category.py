from abc import ABC, abstractmethod


# Абстрактный базовый класс для продуктов
class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self):
        pass


# Миксин для печати информации о создании объекта
class CreationInfoMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект класса {self.__class__.__name__} с параметрами: {args}")


# Класс Product, наследует от BaseProduct и миксина
class Product(BaseProduct, CreationInfoMixin):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description)
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data: dict, existing_products: list = None):
        existing_products = existing_products or []
        for prod in existing_products:
            if prod.name == data.get("name"):
                prod.quantity += data.get("quantity", 0)
                if data.get("price") > prod._price:
                    prod._price = data.get("price")
                return prod
        return cls(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            quantity=data.get("quantity"),
        )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевой или отрицательной")
        else:
            if hasattr(self, "_price") and value < self._price:
                confirm = input(f"Вы хотите понизить цену с {self._price} до {value}. Подтвердите (y/n): ")
                if confirm.lower() == "y":
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


# Классы Smartphone и LawnGrass наследуют от Product
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
        new_quantity = self.quantity + other.quantity
        new_price = max(self._price, other.price)
        return Smartphone(
            self.name, self.description, new_price, new_quantity, self.efficiency, self.model, self.memory, self.color
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
        new_price = max(self._price, other.price)
        return LawnGrass(
            self.name, self.description, new_price, new_quantity, self.country, self.germination_period, self.color
        )


from abc import ABC, abstractmethod


class BaseEntity(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class Category(BaseEntity):
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        super().__init__(name, description)
        self.__products = products if products is not None else []
        self.product_count = len(self.__products)
        Category.category_count += 1
        Category.product_count += self.product_count

    def middle_price(self):
        if not self.__products:
            return 0  # или None, если товаров нет
        total_price = sum(prod.price for prod in self.__products)
        return total_price / len(self.__products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        self.product_count += 1

    @property
    def products(self):
        return "\n".join(f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт." for prod in self.__products)

    def __str__(self):
        return f"Категория: {self.name}\nОписание: {self.description}\nТовары:\n{self.products}"

    def average_price(self):
        try:
            if not self.__products:
                raise ZeroDivisionError("Нет товаров для подсчета средней цены")
            total_price = sum(prod.price for prod in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0


class ZeroQuantityError(Exception):
    def __init__(self, message="Добавляемый товар имеет нулевое количество"):
        super().__init__(message)


# Метод добавления с проверкой
def add_product_with_check(self, product):
    try:
        if product.quantity == 0:
            raise ZeroQuantityError()
        self.__products.append(product)
        self.product_count += 1
        print("Товар успешно добавлен.")
    except ZeroQuantityError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Обработка добавления товара завершена.")
