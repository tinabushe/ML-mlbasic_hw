''' 
ТЕСТЫ НЕГАТИВНЫХ СЦЕНАРИЕВ НА САМОЛЕТЕ
'''
# %%
'''
кейс 1: самолет не заправлен, ошибка  LowFuelError --- ОК
'''
from hw_05.plane import Plane
from hw_05 import exceptions as ex

def test_flight_negative_LowFuelError():
    # создала самолет: вес 10000, топливо 0, расход 50, макс. груз 2000
    my_plane = Plane(10000, 0, 50, 2000)
    print(f'1. Cоздала самолет, не грузилась. Толплвиа на старте:  {my_plane.fuel} л, вес груза: {my_plane.cargo} кг')

    try:

        # хагружаю самолет на 1500 кг груза
        my_plane.load_cargo(1500)
        print(f'2. Загрузилась. Вес груза: {my_plane.cargo} кг')

        # зарвожу двигатель
        my_plane.start() #--- не завестись, ОТСУТСТВИЕ ТОПЛИВА!!! ---
        print('3. Завеласть, self.started = True')

        distance = 50
        my_plane.move(distance)
        print(f'4. Прилетела. Остаток топлива: {my_plane.fuel} л')

        # разгружаюсь по прибытии
        removed_cargo = my_plane.remove_all_cargo()
        print(f'5. Разгрузилась. Выгружено: {removed_cargo} кг. На борту осталось груза на: {my_plane.cargo} кг')

    except (ex.LowFuelError, ex.NotEnoughFuel, ex.CargoOverload) as e:
        print(f'Ошибка: {e}')

if __name__ == '__main__':
    test_flight_negative_LowFuelError()

# %%
''' 
кейс 2: не хватит топлива до пункта назначения, ошибка  NotEnoughFuel --- ОК
'''
from hw_05.plane import Plane
from hw_05 import exceptions as ex

def test_flight_negative_NotEnoughFuel():
    # создала самолет: вес 10000, топливо 2000, расход 50, макс. груз 2000
    my_plane = Plane(10000, 2000, 50, 2000)
    print(f'1. Cоздала самолет, не грузилась. Толплвиа на старте:  {my_plane.fuel} л, вес груза: {my_plane.cargo} кг')

    try:

        # хагружаю самолет на 1500 кг груза
        my_plane.load_cargo(1500)
        print(f'2. Загрузилась. Вес груза: {my_plane.cargo} кг')

        # зарвожу двигатель
        my_plane.start()
        print('3. Завеласть, self.started = True')

        # хочу пролететь 50 км (расстояние * на расход = 50 * 50 => надо 2500 топлива)
        distance = 50
        # топлива на полет: топливо - топливо в полете = 2000 - 2500 = -500 --- НЕХВАТКА ТОПЛИВА!!! ---
        my_plane.move(distance)
        print(f'4. Прилетела. Остаток топлива: {my_plane.fuel} л')

        removed_cargo = my_plane.remove_all_cargo()
        print(f'5. Разгрузилась. Выгружено: {removed_cargo} кг. На борту осталось груза на: {my_plane.cargo} кг')

    except (ex.LowFuelError, ex.NotEnoughFuel, ex.CargoOverload) as e:
        print(f'Ошибка: {e}')

if __name__ == '__main__':
    test_flight_negative_NotEnoughFuel()

# %%
''' 
кейс 3: перегрузка, ошибка  CargoOverload --- ОК
'''

from hw_05.plane import Plane
from hw_05 import exceptions as ex

def test_flight_negative_CargoOverload():
    # создала самолет: вес 10000, топливо 3000, расход 50, макс. груз 2000
    my_plane = Plane(10000, 3000, 50, 2000)
    print(f'1. Cоздала самолет, не грузилась. Толплвиа на старте:  {my_plane.fuel} л, вес груза: {my_plane.cargo} кг')

    try:

        # хагружаю самолет на 3500 кг груза
        my_plane.load_cargo(3500) # --- ПЕРЕГРУЗ 500 КГ!!! ---
        print(f'2. Загрузилась. Вес груза: {my_plane.cargo} кг')

        # зарвожу двигатель
        my_plane.start()
        print('3. Завеласть, self.started = True')

        distance = 50
        my_plane.move(distance)
        print(f'4. Прилетела. Остаток топлива: {my_plane.fuel} л')

        removed_cargo = my_plane.remove_all_cargo()
        print(f'5. Разгрузилась. Выгружено: {removed_cargo} кг. На борту осталось груза на: {my_plane.cargo} кг')

    except (ex.LowFuelError, ex.NotEnoughFuel, ex.CargoOverload) as e:
        print(f'Ошибка: {e}')

if __name__ == '__main__':
    test_flight_negative_CargoOverload()