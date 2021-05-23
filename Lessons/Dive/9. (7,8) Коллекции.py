# Коллекции
# Списки
# Список — это упорядоченный набор объектов, хранящихся в одной переменной.В отличие от массивов в
# других языках, у списков нет никаких ограничений на тип переменных, поэтому в них
# могут храниться разные объекты, в том числе и другие коллекции.

empty_list = []
empty_list = list()

none_list = [None] * 10

collections = ['list', 'tuple', 'dict', 'set']

user_data = [
    ['Elena', 4.4],
    ['Andrey', 4.2]
]
# В питоне не нужно явно указывать размер списка или вручную выделять на него память.Длину списка
# можно узнать с помощью встроенной функции len.Размер списка хранится вструктуре, с помощью которой
# реализован тип список, поэтому длина вычисляется за константное время.

len(collections)
4
# Индексы и срезы Чтобы обратиться к конкретному элементу списка, мы используем тот же механизм, что и
# для строк.Нумерация элементов начинается с нуля.

print(collections)

print(collections[0])
print(collections[-1])
['list', 'tuple', 'dict', 'set']
list
set
# Мы можем использовать доступ по индексу для присваивания.

collections[3] = 'frozenset'
print(collections)
['list', 'tuple', 'dict', 'frozenset']
# Если попробовать обратиться к несуществующему индексу, то возникнет ошибка

collections[10]
# ---------------------------------------------------------------------------
IndexError
# Traceback(most recent call last) < ipython - input - 5 - 218 b950f302f > in < module > () ----> 1
collections[10]

IndexError: list
# index out of
range
# Проверить, содержит ли список некоторый объект, можно с помощью ключевого слова "in"

'tuple' in collections
True
# Срезы в списках работают точно так же, как и в строках.
# Создадим список из 10 элементов с помощью встроенной функции
# range.

range_list = list(range(10))
print(range_list)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range_list[1:3]
# [1, 2]
# range_list[3:]
# [3, 4, 5, 6, 7, 8, 9]
# range_list[:5]
# [0, 1, 2, 3, 4]
# print(range_list)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range_list[::2]
# [0, 2, 4, 6, 8]
# range_list[::-1]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# range_list[1::2]
# [1, 3, 5, 7, 9]
# range_list[5:1:-1]
# [5, 4, 3, 2]
# range_list[:] is range_list
# False
# Итерация
# Списки как и строки поддерживают протокол итерации

collections = ['list', 'tuple', 'dict', 'set']

for collection in collections:
    print('Learning {}...'.format(collection))
# Learning
# list...
# Learning
# tuple...
# Learning
# dict...
# Learning
# set...
# Часто бывает нужно получить индекс текущего элемента при итерации.Для этого можно использовать встроенную функцию
enumerate

for idx, collection in enumerate(collections):
    print('#{} {}'.format(idx, collection))
# 0 list
# 1 tuple
# 2 dict
# 3 set
# Добавление и удаление элементов Списки, в отличие от строк, являются изменяемой структурой данных, а
# значит мы можем добавлять элементы в существующий список.

collections.append('OrderedDict')

print(collections)
['list', 'tuple', 'dict', 'set', 'OrderedDict']
collections.extend(['ponyset', 'unicorndict'])

print(collections)
['list', 'tuple', 'dict', 'set', 'OrderedDict', 'ponyset', 'unicorndict']
collections += [None]

print(collections)
['list', 'tuple', 'dict', 'set', 'OrderedDict', 'ponyset', 'unicorndict', None]
# Для удаление элемента из списка можно использовать ключевое слово del.

del collections[4]

print(collections)
['list', 'tuple', 'dict', 'set', 'ponyset', 'unicorndict', None]
min, max, sum
# Часто нам нужно найти минимальный, максимальный элемент в массиве или посчитать сумму
# всех элементов, сделать это можно с помощью встроенных функций min / max / sum.

numbers = [4, 17, 19, 9, 2, 6, 10, 13]

print(min(numbers))
print(max(numbers))
print(sum(numbers))
2
19
80
str.join
# Часто бывает полезно преобразовать список в строку, для этого можно использовать метод str.join()

tag_list = ['python', 'course', 'coursera']

print(', '.join(tag_list))
# python, course, coursera
# Сортировка
import random

numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 20))

print(numbers)
[13, 9, 10, 1, 1, 13, 14, 1, 16, 4]
# Для сортировки списка в питоне есть два способа: стандартная функция
# sorted, которая возвращает новый список, полученный сортировкой исходного, и метод списка.sort(), который
# сортирует in -place.Для сортирвоки используется алгоритм TimSort.

print(sorted(numbers))
print(numbers)
[1, 1, 1, 4, 9, 10, 13, 13, 14, 16]
[13, 9, 10, 1, 1, 13, 14, 1, 16, 4]
numbers.sort()
print(numbers)
[1, 1, 1, 4, 9, 10, 13, 13, 14, 16]
# Часто бывает нужно отсортировать список в обратном порядке

print(sorted(numbers, reverse=True))
[16, 14, 13, 13, 10, 9, 4, 1, 1, 1]
numbers.sort(reverse=True)
print(numbers)
[16, 14, 13, 13, 10, 9, 4, 1, 1, 1]
print(reversed(numbers))
# < list_reverseiterator
# object
# at
# 0x107067e10 >
print(list(reversed(numbers)))
[1, 1, 1, 4, 9, 10, 13, 13, 14, 16]
# Методы Кроме рассмотренных выше методов у списка есть
# и другие.Об этих методах вы можете почитать в документации или help(list).

# append clear copy count extend index insert pop remove reverse sort
# Кортежи
# Кортеж — по сути это неизменяемый список, который мы можем хэшировать, а значит
# использовать в качестве ключа в словарях, о которых мы поговорим позже.

empty_tuple = ()
empty_tuple = tuple()
immutables = (int, str, tuple)
immutables[0] = float
# ---------------------------------------------------------------------------
# TypeError
# Traceback(most
# recent
# call
# last)
# < ipython - input - 34 - 70298
# ebdccb5 > in < module > ()
# ----> 1
# immutables[0] = float
#
# TypeError: 'tuple'
# object
# does
# not support
# item
# assignment
blink = ([], [])
blink[0].append(0)

print(blink)
([0], [])
hash(tuple())
3527539
one_element_tuple = (1,)
guess_what = (1)

type(guess_what)
int
# Списки
# Упорядоченный изменяемый набор объектов Поддерживают индексы и
# срезы Поддерживают итерацию Встроенные функции и методы Кортежи
# Упорядоченный неизменяемый набор объектов Похожи на списки с поправкой на
# неизменяемость Хэшируемы Словари Словари в питоне хранят данные в виде
# пары ключ - значение.Ключи должны быть хэшируемы и в обычном словаре хранятся без
# гарантии порядка.

empty_dict = {}
empty_dict = dict()

collections_map = {
    'mutable': ['list', 'set', 'dict'],
    'immutable': ['tuple', 'frozenset']
}
# Доступ к значению по ключу осуществляется за константное время, то
# есть не зависит от размера словаря.

print(collections_map['immutable'])
['tuple', 'frozenset']
print(collections_map['irresistible'])
# ---------------------------------------------------------------------------
# KeyError
# Traceback(most
# recent
# call
# last)
# < ipython - input - 40 - fae0f6f2a221 > in < module > ()
# ----> 1
# print(collections_map['irresistible'])
#
# KeyError: 'irresistible'
# Часто бывает полезно попытаться достать значение по ключу
# из словаря, а в случае отсутствия ключа вернуть какое - то стандартное
# значение.

print(collections_map.get('irresistible', 'not found'))
# not found
# Проверка на вхождения ключа в словарь так же осуществляется за
# константное время   выполняется с помощью ключевого слова in

'mutable' in collections_map
True
# Добавление и удаление элементов Словари в питоне являются изменяемой
# структурой данных, а значит мы можем добавлять новые значения и
# удалять не нужные.

beatles_map = {
    'Paul': 'Bass',
    'John': 'Guitar',
    'George': 'Guitar',
}

print(beatles_map)
{'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar'}
beatles_map['Ringo'] = 'Drums'

print(beatles_map)
{'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar', 'Ringo': 'Drums'}
del beatles_map['John']

print(beatles_map)
{'Paul': 'Bass', 'George': 'Guitar', 'Ringo': 'Drums'}
beatles_map.update({
    'John': 'Guitar'
})

print(beatles_map)
{'Paul': 'Bass', 'George': 'Guitar', 'Ringo': 'Drums', 'John': 'Guitar'}
print(beatles_map.pop('Ringo'))

print(beatles_map)
# Drums
{'Paul': 'Bass', 'George': 'Guitar', 'John': 'Guitar'}
unknown_dict = {}

print(unknown_dict.setdefault('key', 'default'))
# default
print(unknown_dict)
{'key': 'default'}
print(unknown_dict.setdefault('key', 'new_default'))
# default
# Итерация
# Словари как и другие коллекции поддерживает протокол
# итерации и по умолчанию итерация идет по ключам.

print(collections_map)

for key in collections_map:
    print(key)
{'mutable': ['list', 'set', 'dict'], 'immutable': ['tuple', 'frozenset']}
# mutable
# immutable
# Для итерации по ключам и значениям одновременно используется
# метод словаря.items().

for key, value in collections_map.items():
    print('{} — {}'.format(key, value))
# mutable — ['list', 'set', 'dict']
# immutable — ['tuple', 'frozenset']
for value in collections_map.values():
    print(value)
['list', 'set', 'dict']
['tuple', 'frozenset']
# OrderedDict
from collections import OrderedDict

ordered = OrderedDict()

for number in range(10):
    ordered[number] = str(number)

for key in ordered:
    print(key)
0
1
2
3
4
5
6
7
8
9
# Словари Изменяемый неупорядоченный набор пар ключ - значение
# Быстрый доступ к значению по ключу
# Быстрая проверка на вхождение ключа в словарь

# Множества
# Множество в питоне — это неупорядоченный набор уникальных объектов.
# Множества изменяемы и чаще всего используются для удаление дубликатов
# и всевозможных проверок на вхождение.

empty_set = set()
number_set = {1, 2, 3, 3, 4, 5}

print(number_set)
{1, 2, 3, 4, 5}

# Чтобы проверить, содержится ли объект в
# множестве, используется уже знакомое   ключевое слово in.Проверка
# выполняется за константное время, время .выполнения операции
# не зависит от размера множества.Это достигается засчет хэширования
# каждого элемента структуры по аналогии со словарями.По полученному от
# хэш - функции ключу и происходит поиск объекта.Таким образом во
# множествах могут содержаться только хэшируемые объекты.

print(2 in number_set)
True
# Чтобы добавить элемент в множество, используется метод add.\
# Так же множества в питоне стандартные операции на множествами, такие как
# объединение, разность, пересечение и симметрическая разность.

odd_set = set()
even_set = set()

for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even_set.add(number)

print(odd_set)
print(even_set)
{1, 3, 5, 7, 9}
{0, 2, 4, 6, 8}
union_set = odd_set | even_set
union_set = odd_set.union(even_set)

print(union_set)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
intersection_set = odd_set & even_set
intersection_set = odd_set.intersection(even_set)

print(intersection_set)
set()
difference_set = odd_set - even_set
difference_set = odd_set.difference(even_set)

print(difference_set)
{1, 3, 5, 7, 9}
symmetric_difference_set = odd_set ^ even_set
symmetric_difference_set = odd_set.symmetric_difference(even_set)

print(symmetric_difference_set)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# Для удаления конкретного элемента существует метод remove, для
# удаления любого можно использовать pop.\
# Остальные методы можно посмотреть в help или документации.

even_set.remove(2)
print(even_set)
{0, 4, 6, 8}
even_set.pop()
0
# Также в питоне существует тип frozenset, который является неизменяемым
# множеством.

frozen = frozenset(['Anna', 'Elsa', 'Kristoff'])

frozen.add('Olaf')
# ---------------------------------------------------------------------------
# AttributeError
# Traceback(most
# recent
# call
# last)
# < ipython - input - 64 - 962
# f221e1321 > in < module > ()
# 1
# frozen = frozenset(['Anna', 'Elsa', 'Kristoff'])
# 2
# ----> 3
frozen.add('Olaf')

AttributeError: 'frozenset'
object
# has no attribute 'add' Множества Изменяемый неупорядоченный
# набор уникальных объектов Быстрая проверка на вхождение
# Математические операции над множествами