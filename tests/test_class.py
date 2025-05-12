import pytest

from src.class_module import Category, Product


def test_product_correct(product_item: Product) -> None:
    """Тест корректных значений продукта."""
    assert product_item.name == "Samsung s20"
    assert product_item.description == "Смартфон корейский"
    assert product_item.price == 80000
    assert product_item.quantity == 20


def test_product_incorrect(product_item: Product) -> None:
    """Тест некорректных значений продукта."""
    assert product_item.name != "Xiaomi mi9"
    assert product_item.description != "Смартфон китайский"
    assert product_item.price != 20000
    assert product_item.quantity != 110


def test_category_correct(category_item: Category) -> None:
    """Тест корректных значений категории."""
    assert category_item.name == "Телевизоры"
    assert category_item.description == "Устройство отображения фильмов и тв-передач"
    # Если в фикстуре 1 товар
    assert len(category_item._Category__products) == 1  # type: ignore
    assert Category.category_count == 1  # Проверяем, что счетчик увеличился
    assert Category.product_count == 1  # Проверяем, что товар добавлен


def test_category_incorrect(category_item: Category) -> None:
    """Тест некорректных значений категории."""
    assert category_item.name != "Смартфоны"
    assert category_item.description != "Устройство связи"
    assert len(category_item.products) != 0
    assert Category.category_count != 0
    assert Category.product_count != 0


def test_add_product_increases_count(category_item: Category) -> None:
    """Тест, что add_product увеличивает счетчик товаров"""
    initial_count = Category.product_count
    new_product = Product("Ноутбук", "Игровой", 150000, 5)

    category_item.add_product(new_product)

    assert len(category_item._Category__products) == 2 # type: ignore
    assert Category.product_count == initial_count + 1


def test_add_product_correctly_adds(category_item: Category) -> None:
    """Тест, что add_product корректно добавляет продукт"""
    new_product = Product("Смартфон", "Android", 80000, 10)

    category_item.add_product(new_product)

    assert category_item._Category__products[-1] == new_product # type: ignore


def test_products_property_returns_string(category_item: Category) -> None:
    """Тест, что свойство products возвращает строку"""
    assert isinstance(category_item.products, str)


def test_products_property_format(category_item: Category) -> None:
    """Тест формата возвращаемой строки"""
    result = category_item.products
    expected = "Samsung QLED, 50000 руб. Остаток: 5 шт.\n"
    assert result == expected


# Новые тесты 14.2


def test_product_price_setter_negative() -> None:
    """Тест, что цена не может быть отрицательной"""
    product = Product("Тест", "Тест", 100, 1)
    product.price = -50  # Попытка установить отрицательную цену
    assert product.price == 100  # Цена не должна измениться



def test_add_non_product_to_category(category_item: Category) -> None:
    """Тест, что нельзя добавить не-Product в категорию"""
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
        category_item.add_product("Это не продукт") # type: ignore


def test_new_product_merges_duplicates() -> None:
    """Тест, что new_product объединяет дубликаты"""
    products_list = []
    product_data1 = {"name": "Телефон", "description": "Смартфон", "price": "50000", "quantity": "10"}
    product1 = Product.new_product(product_data1, products_list)

    product_data2 = {"name": "Телефон", "description": "Смартфон", "price": "55000", "quantity": "5"}
    product2 = Product.new_product(product_data2, products_list)

    assert product1 == product2  # Должен вернуться тот же объект
    assert product1.quantity == 15  # Количество суммируется
    assert product1.price == 55000  # Цена берется максимальная


def test_new_product_creates_new_if_no_duplicate() -> None:
    """Тест, что new_product создает новый продукт, если дубликата нет"""
    products_list = []
    product_data = {"name": "Ноутбук", "description": "Игровой", "price": "100000", "quantity": "3"}
    product = Product.new_product(product_data, products_list)

    assert product in products_list  # Продукт должен быть добавлен в список
    assert len(products_list) == 1
