class UndefinedObject(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Ошибка определения"

    def __str__(self):
        return self.message