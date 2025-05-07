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
        self.products = products

        Category.category_count += 1  # Счетчик категории
        Category.product_count += len(products)  # Счетчик товаров


def restract_object(path_file: str) -> list[Category]:
    """Функция берет JSON и преобразует объекты"""
    with open(path_file, "r", encoding="utf-8") as file:
        data = json.load(file)

        categories = []
        for category_data in data:
            products = []
            for product_data in category_data["products"]:
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                )
                products.append(product)

            category = Category(
                name=category_data["name"], description=category_data["description"], products=products
            )
            categories.append(category)
        return categories


if __name__ == "__main__":
    # 1. Загружаем данные
    categories = restract_object(FILE_JSON)  # Получаем список категорий

    # 2. Выводим общую информацию
    print(f"\nВсего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")

    # 3. Выводим подробную информацию по каждой категории
    for category in categories:  # Теперь categories определена
        print(f"\nКатегория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Количество товаров: {len(category.products)}")

        # Выводим все товары в категории
        for product in category.products:
            print(f"  {product}")
