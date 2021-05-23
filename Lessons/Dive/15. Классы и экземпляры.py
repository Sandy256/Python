class Human:
    pass
class Robot:
    """Данный класс позволяет создовать роботов"""


class Planet:

    count = 0

    # Инициализирует атрибут name для экземпляра класса Planet
    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1

    # Позволяет определить то как будет печататься объект,
    # в данном случае будет печатать атрибут name имя
    def __str__(self):
        return self.name

    #Переопределяет как будет отображаться внутреннее представление
    #обьекта
    def __repr__(self):
        return  f"Planet {self.name}"

solar_system = []
planet_names = ["Mercury", "Venus", "Earth", "Mars",
                "Jupiter", "Saturn", "Uranus", "Neptune"]
for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)

earth = Planet('Earth')
# Можно присваивать атрибутам экземпляра новые значения экземляр.атрибут

mars = Planet("Mars")
print(mars)

#Coursera


# isinstance(num, int)
# True
# numbers = {}
# isinstance(numbers, dict)
# True
# Объявление класса
class Human:
    pass
class Robot:
    """Данный класс позволяет создавать роботов"""
print(Robot)
# <class '__main__.Robot'>
print(dir(Robot))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# Создание экземпляра (объекта) класса
class Planet:
    pass
planet = Planet()
print(planet)
# <__main__.Planet object at 0x10e8722b0>
solar_system = []
for i in range(8):
    planet = Planet()
    solar_system.append(planet)

print(solar_system)
# [<__main__.Planet object at 0x10e872780>, <__main__.Planet object at 0x10e8722b0>,
# <__main__.Planet object at 0x10e8727f0>, <__main__.Planet object at 0x10e872828>,
# <__main__.Planet object at 0x10e872860>, <__main__.Planet object at 0x10e872898>, <__main__.Planet object at 0x10e8728d0>, <__main__.Planet object at 0x10e872908>]
solar_system = {}
for i in range(8):
    planet = Planet()
    solar_system[planet] = True

print(solar_system)
# {<__main__.Planet object at 0x10e872978>: True, <__main__.Planet object at 0x10e872908>: True,
# <__main__.Planet object at 0x10e8727f0>: True, <__main__.Planet object at 0x10e872828>: True,
# <__main__.Planet object at 0x10e872860>: True, <__main__.Planet object at 0x10e872898>: True,
# <__main__.Planet object at 0x10e8729e8>: True, <__main__.Planet object at 0x10e872940>: True}
# Инициализация экземпляра
class Planet:

    def __init__(self, name):
        self.name = name
earth = Planet("Earth")
print(earth.name)
print(earth)
# Earth
# <__main__.Planet object at 0x10e8796d8>
class Planet:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


earth = Planet("Earth")
print(earth)
# Earth
solar_system = []

planet_names = [
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune"
]

for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)
# [<__main__.Planet object at 0x10477f160>,
# <__main__.Planet object at 0x10477f278>,
# <__main__.Planet object at 0x10477f198>,
# <__main__.Planet object at 0x10477f1d0>,
# <__main__.Planet object at 0x10477f208>,
# <__main__.Planet object at 0x10477f240>, <__main__.Planet object at 0x1048637b8>, <__main__.Planet object at 0x1048637f0>]
class Planet:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Planet {self.name}"
solar_system = []

planet_names = [
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune"
]

for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)
# [Planet Mercury, Planet Venus, Planet Earth, Planet Mars, Planet Jupiter, Planet Saturn, Planet Uranus, Planet Neptune]
# Работа с атрибутами экземпляра
mars = Planet("Mars")
print(mars)
# Planet Mars
mars.name
'Mars'
mars.name = "Second Earth?"
mars.name
'Second Earth?'
mars.mass
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-7-3c1085af8f48> in <module>()
# ----> 1 mars.mass
#
# AttributeError: 'Planet' object has no attribute 'mass'
# del mars.name
# mars.name
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-9-202092835a22> in <module>()
# ----> 1 mars.name
#
# AttributeError: 'Planet' object has no attribute 'name'
# Мы с вами:

# Посмотрели как объявлять классы
# Научились создавать экземпляры (объекты) классов
# Рассмотрели как инициализировать экземпляр класса
# Научились работать с атрибутами экземпляра класса

# Атрибуты класса
class Planet:

    count = 0

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1
earth = Planet("Earth")
mars = Planet("Mars")

print(Planet.count)
2
mars.count
2
# Деструктор экземпляра класса
class Human:

    def __del__(self):
        print("Goodbye!")
human = Human()
# в данном случае деструктор отработает - но все же
# лучше создать метод и вызывать его явно
del human
# Goodbye!
# Словарь экземпляра и класса
class Planet:
    """This class describes planets"""

    count = 1

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []


planet = Planet("Earth")
planet.__dict__
{'name': 'Earth', 'population': []}
planet.mass = 5.97e24
planet.__dict__
{'mass': 5.97e+24, 'name': 'Earth', 'population': []}
Planet.__dict__
# mappingproxy({'__dict__': <attribute '__dict__' of 'Planet' objects>,
#               '__doc__': 'This class describes planets',
#               '__init__': <function __main__.Planet.__init__>,
#               '__module__': '__main__',
#               '__weakref__': <attribute '__weakref__' of 'Planet' objects>,
#               'count': 1})
Planet.__doc__
'This class describes planets'
planet.__doc__
'This class describes planets'
print(dir(planet))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'count', 'mass', 'name', 'population']
planet.__class__
# __main__.Planet
# Конструктор экземпляра класса
class Planet:

    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        print("__init__ called")
        self.name = name
earth = Planet("Earth")
# __new__ called
# __init__ called
# То есть при вызове Planet("Earth") произошло примерно следующее:

planet = Planet.__new__(Planet, "Earth")

if isinstance(planet, Planet):
    Planet.__init__(planet, "Earth")
# Мы с вами:

# узнали, что такое атрибут класса
# посмотрели на деструктор и конструктор экземпляра
# поговорили о поиске атрибутов в словаре экземпляра и класса
### Атрибуты класса

class Planet:

    count = 0

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1

earth = Planet("Earth")
mars = Planet("Mars")

print(Planet.count)

mars.count

### Деструктор экземпляра класса

class Human:

    def __del__(self):
        print("Goodbye!")

human = Human()
# в данном случае деструктор отработает - но все же
# лучше создать метод и вызывать его явно
del human

### Словарь экземпляра и класса

class Planet:
    """This class describes planets"""

    count = 1

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []


planet = Planet("Earth")

planet.__dict__

planet.mass = 5.97e24

planet.__dict__

Planet.__dict__

Planet.__doc__

planet.__doc__

print(dir(planet))

planet.__class__

### Конструктор экземпляра класса

class Planet:

    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        print("__init__ called")
        self.name = name

earth = Planet("Earth")

# То есть при вызове `Planet("Earth")` произошло примерно следующее:

# <pre>
planet = Planet.__new__(Planet, "Earth")

if isinstance(planet, Planet):
    Planet.__init__(planet, "Earth")
# </pre>

# Мы с вами:
# * узнали, что такое атрибут класса
# * посмотрели на деструктор и конструктор экземпляра
# * поговорили о поиске атрибутов в словаре экземпляра и класса




