import json
from config import FILE_JSON


class Product:
    """Класс продуктов с подробным описанием"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    # Специальный вывод преобразования ссылки в строки для чтения
    def __str__(self) -> str:  # type: ignore
        return (
            f"{self.name} | "
            f"Цена: {self.price}₽ | "
            f"Остаток: {self.quantity} шт. | "
            f"Описание: {self.description}"
        )


class Category:
    """Класс категории с описанием и счетчиком продуктов"""

    name: str
    description: str
    products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list["Product"]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1  # Счетчик категории
        Category.product_count += len(products)  # Счетчик товаров

    # @property
    # def add_product(self,):
