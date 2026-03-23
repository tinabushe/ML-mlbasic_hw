'''В модуле `exceptions` объявите следующие исключения:
* LowFuelError
* NotEnoughFuel
* CargoOverload
'''

class LowFuelError(Exception):
    def __str__(self):
        return 'Топливо отсусвует, нужно заправиться'

class NotEnoughFuel(Exception):
    def __str__(self):
        return 'Топлива не хватит до пункта назначения'

class CargoOverload(Exception):
    def __str__(self):
        return 'Перегрузка, не взлетим'