from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный клас для общих методов"""
    @abstractmethod
    def __add__(self, other) -> float | int:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class FormationProduct(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass