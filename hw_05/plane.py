"""
Создайте класс `Plane`, наследник `Vehicle`
"""
'''
* класс `Plane` должен быть наследником `Vehicle`
* добавьте атрибуты `cargo` и `max_cargo` классу `Plane`
* добавьте `max_cargo` в инициализатор (переопределите родительский)
* объявите метод `load_cargo`, который принимает число, проверяет, что в сумме с текущим `cargo` не будет перегруза, и обновляет значение, в ином случае выкидывает исключение `exceptions.CargoOverload`
* объявите метод `remove_all_cargo`, который обнуляет значение `cargo` и возвращает значение `cargo`, которое было до обнуления
'''

from hw_05.base import Vehicle
from hw_05 import exceptions as ex

class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, load):
        if self.cargo + load > self.max_cargo:
            raise ex.CargoOverload()
        self.cargo += load

    def remove_all_cargo(self):
        cargo_before_removal = self.cargo
        self.cargo = 0
        return cargo_before_removal
