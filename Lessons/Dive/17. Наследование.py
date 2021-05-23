#Наследование
# 1 - изменение поведения класса
# 2 - расширение функционала класса

class Pet:
    def __init__(self, name=None):
        self.name = name
#Новый класс созданный при помощи наследования, наследует все атрибуты и методы
#родительского класса
class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)# функция super() вызывает метод __init__ из родиельского класса
        self.breed = breed

    def say(self):
        return "{0}: waw".format(self.name)

dog = Dog('Шарик', 'Доберман')
print(dog.name)
print(dog.say())

#Множественное наследование

import json

class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": self.breed
        })

class ExDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        #вызов метода MRO
        super().__init__(name, breed)
        # super(ExDog, self).__init__(name)

class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        # явное указание метода конкретного класса
        super(Dog, self).__init__(name)
        self.breed = "Шерстяная собака породы {0}".format(breed)

dog = ExDog("Белка", breed="Дворняга")
print(dog.to_json())

issubclass()
isinstance()

# Наследование в Python
# наследование классов
# множественное наследование
# вызов super()
# name mangling
# композиция vs наследование
# Зачем нужно наследование классов?
# изменение поведения класса
# расширение функционала класса
# Класс Pet, домашний питомец
# class Pet:
#     def __init__(self, name=None):
#         self.name = name
# Наследование, класс Dog
class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return "{0}: waw".format(self.name)

# >>> dog = Dog("Шарик", "Доберман")
# >>> print(dog.name)
# Шарик
# >>> print(dog.say())
# Шарик: waw!
# >>>
# Множественное наследование
import json

class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": self.breed
        })

class ExDog(Dog, ExportJSON):
    pass

# >>> dog = ExDog("Белка", breed="Дворняжка")
# >>> print(dog.to_json())
{"name": "\u0411\u0435\u043b\u043a\u0430", "breed": "\u0414\u0432\u043e\u0440\u043d\u044f\u0436\u043a\u0430"}
# Любой класс является потомком object
# >>> issubclass(int, object)
# True
# >>> issubclass(Dog, object)
# True
# >>> issubclass(Dog, Pet)
# True
# >>> issubclass(Dog, int)
# False
# Объект является экземляром класса?
# >>> isinstance(dog, Dog)
# True
# >>> isinstance(dog, Pet)
# True
# >>> isinstance(dog, object)
# True
# Поиск атрибутов и методов объекта, линеаризация класса
#     object
#     /   \
#    /     \
#  Pet    ExportJSON
#   |      /
#  Dog    /
#    \   /
#    ExDog

# Method Resolution Order
# >>> ExDog.__mro__
# (<class '__main__.ExDog'>, <class '__main__.Dog'>,
#  <class '__main__.Pet'>, <class '__main__.ExportJSON'>,
#  <class 'object'>)
# >>>
# Использование super()
# >>> ExDog.__mro__
# (<class '__main__.ExDog'>, <class '__main__.Dog'>,
#  <class '__main__.Pet'>, <class '__main__.ExportJSON'>,
#  <class 'object'>)

class ExDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        # вызов метода по MRO
        super().__init__(name, breed)
        # super(ExDog, self).__init__(name)

class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        # явное указание метода конкретного класса
        super(Dog, self).__init__(name)
        self.breed = "Шерстяная собака породы {0}".format(breed)

# >>> dog = WoolenDog("Жучка", breed="Такса")
# >>> print(dog.breed)
# Шерстяная собака породы Такса
# Разрешение конфликта имен, name mangling
class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.__breed = breed

    def say(self):
        return "{0}: waw!".format(self.name)

    def get_breed(self):
        return self.__breed

class ExDog(Dog, ExportJSON):
    def get_breed(self):
        return "порода: {0} - {1}".format(self.name, self.__breed)

# >>> dog = ExDog("Фокс", "Мопс")
# >>> dog.__dict__
{'name': 'Фокс', '_Dog__breed': 'Мопс'}
# >>> dog.get_breed()