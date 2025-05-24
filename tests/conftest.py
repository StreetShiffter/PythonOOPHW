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

@pytest.fixture
def sample_category():
    product1 = Product("Телевизор", "4K телевизор", 30000.0, 10)
    smartphone1 = Smartphone("iPhone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    lawn_grass1 = LawnGrass("Газонная трава Элит", "Высококачественная трава", 500.0, 20, "Россия", "30 дней", "Зеленый")

    products = [product1, smartphone1, lawn_grass1]
    category = Category("Электроника", "Различные электронные устройства", products)
    return category
