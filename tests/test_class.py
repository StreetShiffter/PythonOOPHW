def test_product_correct(product_item):
    assert product_item.name == 'Samsung s20'
    assert product_item.description == 'Смартфон корейский'
    assert product_item.price == 80000
    assert product_item.quantity == 20

def test_product_incorrect(product_item):
    assert not product_item.name == 'Xiaomi mi9'
    assert not product_item.description == 'Смартфон китайский'
    assert not product_item.price == 20000
    assert not product_item.quantity == 110