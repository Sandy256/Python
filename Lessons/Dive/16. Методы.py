class Human:

    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    def __str__(self):
        return self._name

    def _say(self, text):
        print(text)

    def say_name(self):
        self._say(f"Hello, I am {self._name}")

    def say_how_old(self):
        self._say(f"I am {self._age} years old")

class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    def add_human(self, human):
        print(f"Welcome to {self.name}, {human.name}")
        self.population.append(human)

mars = Planet("Mars")
bob = Human("Bob", age=29)
mars.add_human(bob)

#Метод класса @classmethod
from datetime import date

def extract_description(user_string):
    return "Chempionship"
def extract_date(user_string):
    return date(2018, 6, 14)

class Event:

    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description, date)

#Статический метод класса @staticmathod

class Human2:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 110

# можно обращаться от имени класса
Human2.is_age_valid(35)
# или от экземпляра
human = Human2("Old Bobby")
human.is_age_valid(120)

#Вычисляемые свойства класса property

# class Robot: без property()
#     def __init__(self, power):
#         self.power = power
#
#     def set_power(self, power):
#         if power < 0:
#             self.power = 0
#         else:
#             self.power = power

class Robot:
    def __init__(self, power):
        self._power = power

    power = property()

    # .setter Метод который будет выполняться когда мы будем
    # менять атрибут power экземпляра
    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value
    # .getter Метод который будет выполняться когда мы будем
    # читать атрибут power экземпляра
    @power.getter #
    def power(self):
        return self._power
    # .deleter Метод который будет выполняться когда мы будем
    # удалять атрибут power экземпляра
    @power.deleter #
    def power(self):
        print("make robot useless")
        del self._power
#Короткий способ чтобы модифицировать только чтение
    @property
    def power2(self):
        return self._power


walle = Robot(100)
walle.power = 200
print(walle.power)

#Coursera

# Работа с методами экземпляра
class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age


class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    def add_human(self, human):
        print(f"Welcome to {self.name}, {human.name}!")
        self.population.append(human)
mars = Planet("Mars")

bob = Human("Bob")

# mars.add_human(bob)
# Welcome to Mars, Bob!
# print(mars.population)
# [<__main__.Human object at 0x10e416780>]
# Вызов методов из методов
class Human:
    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    def _say(self, text):
        print(text)

    def say_name(self):
        self._say(f"Hello, I am {self._name}")

    def say_how_old(self):
        self._say(f"I am {self._age} years old")
bob = Human("Bob", age=29)
bob.say_name()
bob.say_how_old()
# Hello, I am Bob
# I am 29 years old
# не рекомендуется!
print(bob._name)

# не рекомендуется!
bob._say("Whatever we want")
# Bob
# Whatever we want
# Метод класса (@classmethod)
class Event:

    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"
from datetime import date

event_description = "Рассказать, что такое @classmethod"
event_date = date.today()

event = Event(event_description, event_date)
print(event)
# Event "Рассказать, что такое @classmethod" at 2017-07-09
def extract_description(user_string):
    return "открытие чемпионата мира по футболу"


def extract_date(user_string):
    return date(2018, 6, 14)


class Event:

    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description, date)
event = Event.from_string("добавить в мой календарь открытие чемпионата мира по футболу на 14 июня 2018 года")
print(event)
# Event "открытие чемпионата мира по футболу" at 2018-06-14
dict.fromkeys("12345")
{'1': None, '2': None, '3': None, '4': None, '5': None}
# В этом видео:

# Научились объявлять и вызывать методы экземпляров
# Посмотрели на метод класса (@classmethod)
#
# Статический метод класса (@staticmethod)
class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150
# можно обращаться от имени класса
Human.is_age_valid(35)
True
# или от экземпляра:
human = Human("Old Bobby")
human.is_age_valid(234)
False
# Вычисляемые свойства класса (property)
class Robot:

    def __init__(self, power):
        self.power = power
wall_e = Robot(100)
wall_e.power = 200
print(wall_e.power)
200
wall_e.power = -20
class Robot:

    def __init__(self, power):
        self.power = power

    def set_power(self, power):
        if power < 0:
            self.power = 0
        else:
            self.power = power
wall_e = Robot(100)
wall_e.set_power(-20)
print(wall_e.power)
0
class Robot:

    def __init__(self, power):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print("make robot useless")
        del self._power
wall_e = Robot(100)
wall_e.power = -20
print(wall_e.power)
0
del wall_e.power
# make robot useless
class Robot:
    def __init__(self, power):
        self._power = power

    @property
    def power(self):
        # здесь могут быть любые полезные вычисления
        return self._power
wall_e = Robot(200)
wall_e.power
200
# В этом видео:

# Узнали, что такое статический метод (@staticmethod)
# Узнали, что такое свойство класса (@property)
