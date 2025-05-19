import pytest

from src.class_module import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def product_item() -> Product:
    # Создаем продукт
    return Product("Samsung s20", "Смартфон корейский", 80000, 20)


@pytest.fixture
def smartphone_item() -> Product:
    # Создаем продукт
    return Smartphone("Samsung", "Смартфон корейский", 80000, 20, 11.0, "s20", 8, "green")


@pytest.fixture
def lawngrass_item() -> Product:
    # Создаем продукт
    return LawnGrass("Муравушка", "Газонная трава", 500, 10, "Колумбия", "3 месяца", "Зеленая")


@pytest.fixture
def category_item() -> Category:
    # Создаем список товаров (с одним товаром)
    product1 = Product("Samsung QLED", "4K TV", 50000, 5)
    product2 = Product("Samsung LED", "HD TV", 20000, 20)
    products = [product1, product2]
    return Category("Телевизоры", "Устройство отображения фильмов и тв-передач", products)
