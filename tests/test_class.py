from unittest.mock import patch
import pytest
import unittest
from src.class_module import Category, Iterator, LawnGrass, Product, Smartphone, Order

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
    assert len(category_item._Category__products) == 2  # type: ignore
    assert Category.category_count == 1  # Проверяем, что счетчик увеличился
    assert Category.product_count == 2  # Проверяем, что товар добавлен


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

    assert len(category_item._Category__products) == 3  # type: ignore
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
    expected = "Samsung QLED, 50000 руб. Остаток: 5 шт.\n" "Samsung LED, 20000 руб. Остаток: 20 шт."
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


def test_init_rise() -> None:
        product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        with pytest.raises(TypeError):
            Category("Смартфоны", "Высокопроизводительные смартфоны", [product, 321])


def test_add_product_raises_error_when_adding_wrong_type():
    # Создаём начальный продукт
    smartphone = Smartphone("iPhone",
                            "Смартфон Apple",
                            100000.0,
                            10,
                            11,
                            "15 Pro",
                            8,
                            "grey")

    # Создаём категорию с ним
    category = Category("Смартфоны", "Высокопроизводительные смартфоны", [smartphone])

    # Пробуем добавить продукт другого типа
    trava = LawnGrass("Красная кружка",
                      "Удобная кружка для кофе",
                      500.0,
                      100,
                      "Russia",
                      "1 week",
                      "Green")

    # Ожидаем TypeError
    with pytest.raises(TypeError) as exc_info:
        category.add_product(trava)

    # Проверяем текст ошибки
    expected_message = f"В эту категорию можно добавлять только товары типа {type(smartphone).__name__}"
    assert str(exc_info.value) == expected_message


def test_getter_product() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Высокопроизводительные смартфоны", [product1, product2])
    assert category.product_list


def test_check_list_product() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Высокопроизводительные смартфоны", [product1, product2])
    assert category.product_list


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

    # Получаем продукты через итератор
    result = []
    for product in iterator:
        result.append(product)

    # Проверяем количество и наличие всех продуктов
    assert len(result) == 3
    assert product1 in result
    assert product2 in result
    assert product3 in result


def test_iterator_raises_stopiteration_after_end() -> None:
    """Проверяет, что после окончания итерации выбрасывается StopIteration"""
    product = Product("Товар", "Описание", 100.0, 5)
    category = Category("Тест", "Категория для теста", [product])
    iterator = Iterator(category)

    next(iterator)  # Получаем первый (и единственный) элемент

    # Проверяем, что следующее обращение вызывает StopIteration
    with pytest.raises(StopIteration):
        next(iterator)


def test_iterator_in_category_loop() -> None:
    """Проверяем, что можно использовать for product in Iterator(...)"""
    products = [
        Product("Молоко", "Пастеризованное", 80.0, 20),
        Product("Хлеб", "Ржаной", 30.0, 50),
        Product("Сыр", "Твёрдый", 250.0, 10),
    ]

    category = Category("Продукты", "Основные продукты питания", products)
    count = 0
    seen_products = []

    # Итерируемся через for-in
    for product in Iterator(category):
        seen_products.append(product)
        count += 1

    # Проверяем, что прошли по всем продуктам
    assert count == len(products)
    assert all(p in seen_products for p in products)


# Новые тесты 16.1


def test_smartfone_check(smartphone_item: Smartphone) -> None:
    """Тест корректного отображения объекта класса 'Smartphone'"""
    assert smartphone_item.name == "Samsung"
    assert smartphone_item.description == "Смартфон корейский"
    assert smartphone_item.price == 80000
    assert smartphone_item.efficiency == 11.0
    assert smartphone_item.model == "s20"
    assert smartphone_item.memory == 8
    assert smartphone_item.color == "green"


def test_lawngrass_item_check(lawngrass_item: LawnGrass) -> None:
    """Тест корректного отображения объекта класса 'LawnGrass'"""
    assert lawngrass_item.name == "Муравушка"
    assert lawngrass_item.description == "Газонная трава"
    assert lawngrass_item.price == 500
    assert lawngrass_item.quantity == 10
    assert lawngrass_item.country == "Колумбия"
    assert lawngrass_item.germination_period == "3 месяца"
    assert lawngrass_item.color == "Зеленая"


def test_add_method_smartphone(smartphone_item: Smartphone) -> None:
    """Тест корректного сложения объектов класса 'Smartphone'"""
    smartphone_new = Smartphone("Iphone", "512GB, Красный цвет, 150MP камера", 300000.0, 4, 19.0, "16Pro", 32, "Red")
    smartphone_sum = smartphone_new + smartphone_item
    assert smartphone_sum


def test_add_method_smartphone_rise() -> None:
    """Тест не корректного сложения объектов класса 'Smartphone'"""
    with pytest.raises(TypeError):
        smartphone1 = Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 11.0, "s20", 8, "green"
        )
        smartphone2 = "ТИЛИФОН"
        smartphone_sum = smartphone1 + smartphone2
        assert smartphone_sum


def test_add_method_lawngrass(lawngrass_item: LawnGrass) -> None:
    """Тест корректного сложения объектов класса 'LawnGrass'"""
    lawngrass_new = LawnGrass("Летняя", "Газонная трава", 1000, 30, "Россия", "2 месяца", "Зеленая")

    lawngrass_sum = lawngrass_new + lawngrass_item
    assert lawngrass_sum


def test_add_method_lawngrass_rise() -> None:
    """Тест не корректного сложения объектов класса 'LawnGrass'"""
    with pytest.raises(TypeError):
        lawngrass1 = LawnGrass("Травинушка", "Газонная трава", 700, 2, "Казахстан", "1 неделя", "Синяя")
        lawngrass2 = 1
        lawngrass_sum = lawngrass1 + lawngrass2
        assert lawngrass_sum


def test_add_method_rise(smartphone_item, lawngrass_item, product_item) -> None:
    """Тест ошибки сложения разных типов объектов"""
    with pytest.raises(TypeError):
        product1 = smartphone_item
        product2 = lawngrass_item
        product3 = product_item

        assert product1 + product2
        assert product3 + "Smartphone"


def test_add_with_non_product_raises_typeerror() -> None:
    """Тест что сложение с не-Product объектом вызывает TypeError"""
    product = Product("Груша", "Фрукты", 8, 9)
    with pytest.raises(TypeError):
        assert product + 100  # попытка сложить с числом
    with pytest.raises(TypeError):
        assert product + "строка"  # попытка сложить со строкой


@patch("src.class_module.input")
def test_price_with_confirmation_approved(mock_input) -> None:
    """Тест перехвата положительного ответа пользователя"""

    # Настраиваем mock input возвращать 'y' при вызове
    mock_input.return_value = "y"

    product = Product("Samsung QLED", "4K TV", 50000, 5)
    original_price = product.price  # Сохраняем оригинальную цену
    new_price = 40000  # Меньше текущей цены

    # Пытаемся установить новую цену
    product.price = new_price

    # Проверяем, что input был вызван с правильным сообщением
    # (сравниваем с оригинальной ценой, а не новой)
    mock_input.assert_called_once_with(
        f"Новая цена {new_price} ниже текущей {original_price}. Подтвердите изменение (y/n): "
    )

    # Проверяем, что цена действительно изменилась
    assert product.price == new_price


@patch("src.class_module.input")
def test_price_with_confirmation__not_approved(mock_input) -> None:
    """Тест перехвата отрицательного ответа пользователя"""
    # Настраиваем mock input возвращать 'n' при вызове
    mock_input.return_value = "n"
    new_price = 40000  # Меньше текущей цены

    product = Product("Samsung QLED", "4K TV", 50000, 5)
    original_price = product.price  # Сохраняем оригинальную цену

    # Пытаемся установить новую цену
    product.price = new_price

    # Проверяем, что input был вызван с правильным сообщением
    # (сравниваем с оригинальной ценой, а не новой)
    mock_input.assert_called_once_with(
        f"Новая цена {new_price} ниже текущей {original_price}. Подтвердите изменение (y/n): "
    )

    # Проверяем, что цена действительно изменилась
    assert product.price != new_price

def test_order_valid(product_item: Product) -> None:
    """Тест класса заказа при валидных данных"""
    total_order = Order(product_item, 20)
    assert total_order

def test_order_str() -> None:
    """Тест класса заказа при валидных данных и вывод строки в консоль"""
    product = Product("Телевизор", "4K телевизор", 30000.0, 10)
    order = Order(product=product, quantity=2)
    expected_str = 'Телевизор, 30000.0 руб. Остаток: 10 шт., 2, 60000.0'
    assert str(order) == expected_str

def test_order_invalid(product_item: Product) -> None:
    """Тест класса заказа при невалидных данных"""
    with pytest.raises(ValueError) as text_error:
        total_order = Order(product_item, 25)
        assert text_error == total_order

def test_products_info(sample_category) -> None:
    """Проверка вывода информации категории"""
    expected = (
        "Телевизор, 30000.0 руб. Остаток: 10 шт.\n"
        "iPhone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Газонная трава Элит, 500.0 руб. Остаток: 20 шт."
    )
    assert sample_category.products_info() == expected


def test_str_method_category(sample_category) -> None:
    """Проверка вывода информации категории в виде строчного вывода"""
    expected = "Электроника, количество продуктов: 38 шт."
    assert str(sample_category) == expected


def test_len_method_category(sample_category):
    """Проверка вывода информации длины категории"""
    assert len(sample_category) == 3

def test_product_check_list(sample_category, capsys) -> None:
    """
    Проверяет, что метод product_check_list() корректно выводит типы продуктов.
    """
    expected_output = (
        "[Обычный товар] Телевизор\n"
        "[Смартфон] iPhone 15\n"
        "[Газонная трава] Газонная трава Элит\n"
    )

    sample_category.product_check_list()

    # Получаем вывод stdout
    captured = capsys.readouterr()
    assert captured.out == expected_output