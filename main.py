from src.class_module import Category, Product, LawnGrass, Smartphone

if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    # prod_dict = {
    #     "name": "Samsung Galaxy C23 Ultra",
    #     "description": "256GB, Серый цвет, 200MP камера",
    #     "price": 210000.0,
    #     "quantity": 5
    #   }
    # prod_list1 = [product1, product2]
    # prod_list2 = [smartphone1, smartphone2]

    # total = product1 + product2
    # print(total)
    # total2 = grass1 + grass2
    # print(total2)
    # total3 = smartphone1 + smartphone2
    # print(total3)
    # print(product2.price)
    # print(smartphone1.price)
    # print(grass1.price)
    # print(product2)
    # print(smartphone1)
    # print(grass1)
    # print(Product.new_product(prod_dict, prod_list1))
    # print(Smartphone.new_product(prod_dict, prod_list2))

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)
    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)