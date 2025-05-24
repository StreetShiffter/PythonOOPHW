from src.class_module import Product

def test_print_mixin(capsys):
    """Тест миксин, который выводит информацию в консоль"""
    Product("Iphone 16PRO", "Smartphone", 107990, 2)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Iphone 16PRO, Smartphone, 107990, 2)"
