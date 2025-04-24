from abc import ABC, abstractmethod

class ClothingCalculator(ABC):
    """Абстрактный базовый класс для расчета одежды"""
    
    def __init__(self, name):
        self._name = name
        self._history = []
        self._fabric_price = 0
        self._accessories_price = 0
    
    @property
    def name(self):
        return self._name
    
    @property
    def history(self):
        return self._history.copy()
    
    @property
    def fabric_price(self):
        return self._fabric_price
    
    @fabric_price.setter
    def fabric_price(self, value):
        if value < 0:
            raise ValueError("Fabric price cannot be negative")
        self._fabric_price = value
    
    @property
    def accessories_price(self):
        return self._accessories_price
    
    @accessories_price.setter
    def accessories_price(self, value):
        if value < 0:
            raise ValueError("Accessories price cannot be negative")
        self._accessories_price = value
    
    @abstractmethod
    def calculate_fabric(self, size):
        pass
    
    @abstractmethod
    def calculate_cost(self, size):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"
    
    def __repr__(self):
        return f"<{self.__class__.__name__} name='{self.name}'>"