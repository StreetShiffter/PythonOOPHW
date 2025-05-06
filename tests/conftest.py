import pytest
from src.class_module import Product

@pytest.fixture
def product_item():
    return Product('Samsung s20', 'Смартфон корейский', 80000, 20)
