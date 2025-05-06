import pytest

from src.class_module import Category, Product


@pytest.fixture
def product_item() -> Product:
    # Создаем продукт
    return Product("Samsung s20", "Смартфон корейский", 80000, 20)


@pytest.fixture
def category_item() -> Category:
    # Создаем список товаров (с одним товаром)
    products = [Product("Samsung QLED", "4K TV", 50000, 5)]
    return Category("Телевизоры", "Устройство отображения фильмов и тв-передач", products)
