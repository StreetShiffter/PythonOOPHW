import os

# Получаем абсолютный путь к директории скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Формируем правильный путь к JSON-файлу
FILE_JSON = os.path.join(script_dir, "./data/products.json")
