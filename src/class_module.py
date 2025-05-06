class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Category:
    name: str
    description: str
    products: list[Product]

    count_category = 0
    count_product = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.count_category += 1 #Счетчик категории
        Category.count_product += len(products) #Счетчик товаров

