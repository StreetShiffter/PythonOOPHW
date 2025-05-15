import pytest

from src.class_module import Category, Iterator, Product


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

    assert len(category_item._Category__products) == 2  # type: ignore
    assert Category.product_count == initial_count + 1


def test_add_product_correctly_adds(category_item: Category) -> None:
    """Тест, что add_product корректно добавляет продукт"""
    new_product = Product("Смартфон", "Android", 80000, 10)

    category_item.add_product(new_product)

    assert category_item._Category__products[-1] == new_product  # type: ignore


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
        category_item.add_product("Это не продукт")  # type: ignore


def test_new_product_merges_duplicates() -> None:
    """Тест, что new_product объединяет дубликаты"""
    products_list: list = []
    product_data1 = {"name": "Телефон", "description": "Смартфон", "price": "50000", "quantity": "10"}
    product1 = Product.new_product(product_data1, products_list)

    product_data2 = {"name": "Телефон", "description": "Смартфон", "price": "55000", "quantity": "5"}
    product2 = Product.new_product(product_data2, products_list)

    assert product1 == product2  # Должен вернуться тот же объект
    assert product1.quantity == 15  # Количество суммируется
    assert product1.price == 55000  # Цена берется максимальная


def test_new_product_creates_new_if_no_duplicate() -> None:
    """Тест, что new_product создает новый продукт, если дубликата нет"""
    products_list: list = []
    product_data = {"name": "Ноутбук", "description": "Игровой", "price": "100000", "quantity": "3"}
    product = Product.new_product(product_data, products_list)

    assert product in products_list  # Продукт должен быть добавлен в список
    assert len(products_list) == 1


# Новые тесты 15.1
def test_add_method() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    assert (product1 + product2) == 2580000.0
    assert (product1 + product3) == 1334000.0
    assert (product2 + product3) == 2114000.0


def test_str_method() -> None:
    product = Product("Яблоко", "Это фрукты", 5, 10)
    result = "Яблоко, 5 руб. Остаток: 10 шт."
    assert str(product) == result


def test_iterator_returns_all_products() -> None:
    """Проверяет, что итератор возвращает все товары"""
    product1 = Product("Яблоко", "Сладкое", 50.0, 10)
    product2 = Product("Банан", "Экзотический", 30.0, 15)
    product3 = Product("Апельсин", "Цитрус", 40.0, 20)

    category = Category("Фрукты", "Все фрукты", [product1, product2, product3])
    iterator = Iterator(category)

    result = list(iterator)

    assert len(result) == 3
    assert result[0].name == "Яблоко"
    assert result[1].name == "Банан"
    assert result[2].name == "Апельсин"


def test_iterator_raises_stopiteration_after_end() -> None:
    """Проверяет, что после окончания итерации выбрасывается StopIteration"""
    product1 = Product("Товар 1", "Описание", 100.0, 5)
    product2 = Product("Товар 2", "Описание", 200.0, 3)

    category = Category("Тестовая категория", "Категория для теста", [product1, product2])
    iterator = Iterator(category)

    # Получаем все элементы
    for _ in iterator:
        pass

    try:
        next(iterator)
        assert False, "Ожидалась ошибка StopIteration"
    except StopIteration:
        assert True


def test_iterator_in_category_loop() -> None:
    """Проверяем, что можно использовать for product in Iterator(...)"""
    product1 = Product("Молоко", "Пастеризованное", 80.0, 20)
    product2 = Product("Хлеб", "Ржаной", 30.0, 50)
    product3 = Product("Сыр", "Твёрдый", 250.0, 10)

    category = Category("Продукты", "Основные продукты питания", [product1, product2, product3])
    iterator = Iterator(category)

    count = 0
    for product in iterator:
        count += 1

    assert count == 3
