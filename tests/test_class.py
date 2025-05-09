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
    assert len(category_item.products) == 1  # Если в фикстуре 1 товар
    assert Category.category_count == 1  # Проверяем, что счетчик увеличился
    assert Category.product_count == 1  # Проверяем, что товар добавлен

def test_category_incorrect(category_item: Category) -> None:
    """Тест некорректных значений категории."""
    assert category_item.name != "Смартфоны"
    assert category_item.description != "Устройство связи"
    assert len(category_item.products) != 0
    assert Category.category_count != 0
    assert Category.product_count != 0