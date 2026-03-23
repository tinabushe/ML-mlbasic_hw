"""
Создайте dataclass `Engine`
"""
'''
* добавьте атрибуты `volume` и `pistons`<br>

Пример простейшего датакласса:

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str = "Неизвестно"  # значение по умолчанию
'''

from dataclasses import dataclass

@dataclass
class Engine():
    volume: float
    pistons: int