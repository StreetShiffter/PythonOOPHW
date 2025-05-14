from typing import List, Union

class Product:
    """Класс продуктов с подробным описанием"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, products_dict: dict, products_list: List['Product']) -> 'Product':
        """
        Добавляет новый продукт в список или обновляет существующий:
        - Если продукт с таким именем найден, увеличивает quantity, а цену делает максимальной.
        - Если не найден - добавляет новый продукт.
        """
        name = products_dict["name"]
        description = products_dict["description"]
        price = float(products_dict["price"])
        quantity = int(products_dict["quantity"])

        for product in products_list:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product

        new_product = cls(name=name, description=description, price=price, quantity=quantity)
        products_list.append(new_product)
        return new_product

    @property# type: ignore
    def price(self) -> float:
        """Вызов цены в приватном статусе"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Корректор цены приватного статуса"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            answer = input(
                f"Новая цена {new_price} ниже текущей {self.__price}. Подтвердите изменение (y/n): "
            ).lower()
            if answer != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price
        print(f"Цена успешно изменена на {self.__price}")


    def __str__(self) -> str:
        """Метод преобразования атрибутов в строку и вывод в консоль"""
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """Метод складывания суммы товаров на складе"""
        coast_product = self.__price * self.quantity + other.__price * other.quantity
        return coast_product


class Category:
    """Класс категории с описанием и счетчиком продуктов"""

    name: str
    description: str
    products: List[Product]

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1  # Счетчик категории
        Category.product_count += len(products)  # Счетчик товаров


    def add_product(self, product: 'Product') -> None:
        """Метод добавления нового продукта"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property# type: ignore
    def products(self) -> str:
        """Геттер с функцией вывода товаров"""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str


    def __str__(self) -> str:
        """Метод преобразования атрибутов в строку и вывод в консоль"""
        return f'{self.name}, количество продуктов: {len(self.__products)} шт.'
