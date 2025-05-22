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

    @abstractmethod
    def __str__(self) -> str:
        pass

