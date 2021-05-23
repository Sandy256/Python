def num_to_str(num_list):
    for i in num_list:
        i = str(i)
    return num_list

def num_to_str(a):
    return str(a)

list(map(num_to_str, range(5)))

list(map(lambda x: x**2, range(5)))

#Списочные выражения

list2 = [number ** 2 for number in range(10)]
print(list2)

even_list = [num for num in range(10) if num % 2 ==0]
print(even_list)

#так же работает для словарей

# Функциональное программирование


def caller(func, params):
    return func(*params)


def printer(name, origin):
    print('I\'m {} of {}!'.format(name, origin))


caller(printer, ['Moana', 'Motunui'])
# I'm Moana of Motunui!


def get_multiplier():
    def inner(a, b):
        return a * b

    return inner


multiplier = get_multiplier()
multiplier(10, 11)
110
print(multiplier.__name__)
# inner


def get_multiplier(number):
    def inner(a):
        return a * number

    return inner


multiplier_by_2 = get_multiplier(2)
multiplier_by_2(10)
20
 # map, filter, lambda

def squarify(a):
    return a ** 2

list(map(squarify, range(5)))
[0, 1, 4, 9, 16]
squared_list = []

for number in range(5):
    squared_list.append(squarify(number))

print(squared_list)
[0, 1, 4, 9, 16]


def is_positive(a):
    return a > 0


list(filter(is_positive, range(-2, 3)))
[1, 2]
positive_list = []

for number in range(-2, 3):
    if is_positive(number):
        positive_list.append(number)

print(positive_list)
[1, 2]
list(map(lambda x: x ** 2, range(5)))
[0, 1, 4, 9, 16]
type(lambda x: x ** 2)
# function
list(filter(lambda x: x > 0, range(-2, 3)))
[1, 2]
# Написать функцию, которая превращает список чисел в список строк


def stringify_list(num_list):
    return list(map(str, num_list))


stringify_list(range(10))
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# functools
from functools import reduce


def multiply(a, b):
    return a * b


reduce(multiply, [1, 2, 3, 4, 5])
120
reduce(lambda x, y: x * y, range(1, 5))
24
from functools import partial


def greeter(person, greeting):
    return '{}, {}!'.format(greeting, person)


hier = partial(greeter, greeting='Hi')
helloer = partial(greeter, greeting='Hello')

print(hier('brother'))
print(helloer('sir'))
# Hi, brother!
# Hello, sir!

# Списочные выражения До этого момента мы с вами определяли списки стандартным
# способом, однако в питоне существует более красивая и лаконичная конструкция
# для создания списков и других коллекций.

square_list = []
for number in range(10):
    square_list.append(number ** 2)

print(square_list)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
square_list = [number ** 2 for number in range(10)]
print(square_list)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_list = []
for number in range(10):
    if number % 2 == 0:
        even_list.append(number)

print(even_list)
[0, 2, 4, 6, 8]
even_list = [num for num in range(10) if num % 2 == 0]

print(even_list)
[0, 2, 4, 6, 8]
square_map = {number: number ** 2 for number in range(5)}

print(square_map)
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
reminders_set = {num % 10 for num in range(100)}

print(reminders_set)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(type(number ** 2 for number in range(5)))


# class 'generator'>


num_list = range(7)
squared_list = [x ** 2 for x in num_list]

list(zip(num_list, squared_list))
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]

# Функциональное программирование
# Функции — объекты первого класса
# map, filter, reduce, partial
# lambda — анонимные функции
#        Списочные выражения