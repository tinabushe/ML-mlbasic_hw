# %%
'''
кейс 1: машина не заправлена, ошибка  LowFuelError --- ОК
'''
from hw_05.car import Car
from hw_05.engine import Engine
from hw_05 import exceptions as ex

def test_drive_negative_LowFuelError():
    # создала машину: вес 1000, топливо 0, расход 10
    my_car = Car(1000, 0, 10)
    print(f'1. Cоздала машину. Толплвиа на старте:  {my_car.fuel} л')

    bad_car_eng = Engine(2.5, 6)
    good_car_eng = Engine(10.5, 20)

    try:
        my_car.set_engine(bad_car_eng)
        print(f'\nПлохой движок с параметрами: {bad_car_eng.volume}, {bad_car_eng.pistons}')

        my_car.set_engine(good_car_eng)
        print(f'Хороший движок с параметрами: {good_car_eng.volume}, {good_car_eng.pistons}\n')

        # зарвожу двигатель
        my_car.start() #--- не завестись, ОТСУТСТВИЕ ТОПЛИВА!!! ---
        print('2. Завеласть, self.started = True')
        
        distance = 7
        my_car.move(distance)
        print(f'3. Прилетела. Остаток топлива: {my_car.fuel} л')
    
    except (ex.LowFuelError, ex.NotEnoughFuel, ex.CargoOverload) as e:
        print(f'Ошибка: {e}')

if __name__ == '__main__':
    test_drive_negative_LowFuelError()

# %%
''' 
кейс 2: не хватит топлива до пункта назначения, ошибка  NotEnoughFuel --- ОК
'''
from hw_05.car import Car
from hw_05.engine import Engine
from hw_05 import exceptions as ex

def test_drive_negative_NotEnoughFuel():
    # создала машину: вес 1000, топливо 100, расход 10
    my_car = Car(1000, 100, 10)
    print(f'1. Cоздала машину. Толплвиа на старте:  {my_car.fuel} л')

    bad_car_eng = Engine(2.5, 6)
    good_car_eng = Engine(10.5, 20)

    try:
        my_car.set_engine(bad_car_eng)
        print(f'\nПлохой движок с параметрами: {bad_car_eng.volume}, {bad_car_eng.pistons}')

        my_car.set_engine(good_car_eng)
        print(f'Хороший движок с параметрами: {good_car_eng.volume}, {good_car_eng.pistons}\n')

        # зарвожу двигатель
        my_car.start()
        print('2. Завеласть, self.started = True')
        
        # хочу проехать 5 км (расстояние * на расход = 40 * 10 => надо 400 топлива)
        distance = 40
        # топлива на поездку: топливо - топливо в полете = 100 - 400 = -300 --- НЕХВАТКА ТОПЛИВА!!! ---
        my_car.move(distance)
        print(f'3. Прилетела. Остаток топлива: {my_car.fuel} л')
    
    except (ex.LowFuelError, ex.NotEnoughFuel, ex.CargoOverload) as e:
        print(f'Ошибка: {e}')

if __name__ == '__main__':
    test_drive_negative_NotEnoughFuel()