from pprint import pprint
import inspect
class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('Я существую!')

ivan = Human('Иван', 33)


def introspection_info(obj):
    info = {}
    info['КЛАСС'] = type(obj)
    info['АТРИБУТЫ И МЕТОДЫ'] = dir(obj)
    info['МОДУЛЬ'] = inspect.getmodule(obj)
    return info

pprint(introspection_info(ivan))


