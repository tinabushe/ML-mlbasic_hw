'''
Доработайте базовый класс `base.Vehicle`:<br>
* добавьте атрибуты `weight`, `started`, `fuel`, `fuel_consumption` со значениями по умолчанию
* добавьте инициализатор для установки `weight`, `fuel`, `fuel_consumption`
* добавьте метод `start`. При вызове этого метода необходимо проверить состояние `started`. И если не `started`, то нужно проверить, что топлива больше нуля, и обновить состояние `started`, иначе нужно выкинуть исключение `exceptions.LowFuelError`
* добавьте метод `move`, который проверяет, что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода), и изменяет количество оставшегося топлива, иначе выкидывает исключение `exceptions.NotEnoughFuel`
'''
# %%
# base.py 
from abc import ABC
from hw_05 import exceptions as ex

class Vehicle(ABC):
        '''
        Нюанс с Vehicle(ABC): Поскольку вы оставили Vehicle наследником ABC, но не добавили в него абсолютно ни одного абстрактного метода (с декоратором @abstractmethod), 
        Python все равно позволит вам создать объект car_info = Vehicle(...). 
        Это нормально для данной стадии ДЗ, но знайте, что "настоящий" абстрактный класс обычно запрещает создание экземпляров.
        '''
        weight = 3
        fuel = 100
        fuel_consumption = 5
        started = False

        def __init__(self, weight, fuel, fuel_consumption):
            self.weight = weight
            self.fuel = fuel
            self.fuel_consumption = fuel_consumption

        def start(self):
            if not self.started:
                if self.fuel <= 0:
                    raise ex.LowFuelError()
                self.started = True

        def move(self, distance):
            dist_fuel = self.fuel_consumption * distance

            if self.fuel < dist_fuel:
                raise ex.NotEnoughFuel()
            
            self.fuel -= dist_fuel