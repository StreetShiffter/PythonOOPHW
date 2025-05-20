import json

from config import FILE_JSON
from src.class_module import Category, Product


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
    for category in categories:
        print(f"\nКатегория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Количество товаров: {len(category.product_list)}")

        for product in category.product_list:  # <-- исправлено здесь
            print(f" Товар: {product.name}")
            print("-" * 50)
            print(f"    Описание: {product.description}")
            print("-" * 30)
            print(f"    Цена: {product.price}")
            print("-" * 30)
            print(f"    Количество: {product.quantity}")
