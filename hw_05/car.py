"""
Создайте класс `Car`, наследник `Vehicle`
"""

'''
* класс `Car` должен быть наследником `Vehicle`
* добавьте атрибут `engine` классу `Car`
* объявите метод `set_engine`, который принимает в себя экземпляр объекта `Engine` и устанавливает на текущий экземпляр `Car`
'''
from hw_05.base import Vehicle
from hw_05.engine import Engine

class Car(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None #добавьте атрибут `engine` классу `Car`

    def set_engine(self, engine: Engine):
        self.engine = engine
