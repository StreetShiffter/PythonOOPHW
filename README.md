 
<h3 style="background: linear-gradient(1deg, gold, red); -webkit-background-clip: text; color: transparent;">
  Проект "Оболочка интернет - магазина"
</h3> 

# 🔖 Описание проекта:

Данный проект реализует "ядро" будущего интернет - магазина.


# 🔧 Установка компонентов:


1. Создайте проект и установите poetry:


```pip install --user poetry```
2. Клонируйте репозиторий:


```git clone https://github.com/StreetShiffter/PythonOOPHW.git```

3. Установите инструменты для обработки кода


![Black](https://img.shields.io/badge/black-000000?style=flat&logo=python&logoColor=white)

![Mypy](https://img.shields.io/badge/mypy-checked-blue.svg?logo=python&logoColor=green)

![Flake8](https://img.shields.io/badge/flake8-checked-blue.svg?logo=python&logoColor=blue)

![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat&logo=pytest&logoColor=orange)

![Pytest HTML Report](https://img.shields.io/badge/Pytest_HTML_Report-FF6600?style=flat&logo=pytest&logoColor=black)

![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen?logo=pytest)

![JSON](https://img.shields.io/badge/json-5E5C5C?logo=json&logoColor=red)

# ✒️ Использование

Модуль **class_module.py** реализует создание классов продуктов и категории.


![Пример работы классов product и category](./class_product_category.jpg)
   
 
# 🔍 Тестирование:
Реализованы тестирующие модули для модулей приложения.

| Основа          | Тесты         |
|-----------------|---------------|
| class_module.py | test_class.py |
| Фикстуры тестов | conftest.py   |
 

*Для проверки тестирования воспользуйтесь командами в терминале:* 

`pytest`
или
`pytest имя_пакета\имя_модуля`

При успешном тестировании будет получены результаты положительного тестирования:
![Положительный результат тестирования](./test_complete.jpg)

***Модуль conftest.py используется для данных тестирования функций.***

*Для полной работы установите фреймворк pytest через poetry*

`poetry add --group dev pytest`

# 📤 Отчет в HTML:

**Для получения отчетов в формате html, воспользуйтесь командой**
`pytest --cov-report=html`

Для запуска отчета в браузере:
- на ***Windows***: `start htmlcov/index.html`
- на ***macOS***: `open htmlcov/index.html`
- на ***Linux***: `xdg-open htmlcov/index.html`


# 📂 Работа с JSON:
Реализовано преобразование объектов из JSON
````
    def restract_object(path_file: str) -> list[Category]:
    """Функция берет JSON и преобразует объекты"""
    with open(path_file, "r", encoding="utf-8") as file:
        data = json.load(file)

        categories = []
        for category_data in data:
            products = []
            for product_data in category_data["products"]:
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                )
                products.append(product)

            category = Category(
                name=category_data["name"], description=category_data["description"], products=products
            )
            categories.append(category)
        return categories
````
Пример итоговой работы:
![Пример работы](./json_answer.jpg)

# 📝 Документация 

Для получения дополнительной информации обратитесь к [документации](README.md)
