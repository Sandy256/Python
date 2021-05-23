empty_list = []
empty_list = list()

none_list = [None] * 10

collections = ['list', 'tuple', 'dict', 'set']

user_data = [
    ['Elena', 4.4],
    ['Andrey', 4.2]
]

# Узнать количество элементов в списке
len(collections)

print(collections[0])  # обращение к элемену списка по индексу
collections[3] = 'frozenset'  # Присваивание нового значения элементу списка через индекс

# Проверить есть ли элемент в списке оператор in
'tuple' in collections

range_list = list(range(10))
print(range_list)

range_list[1:3]

# Списки потдерживают срезы [::], при использовании среза создается новый список

collection = ['list', 'tuple', 'dict', 'set']

for i in collection:
    print('type {}...'.format(i))

for idx, collection in enumerate(collections):
    print('#{} {}'.format(idx, collection))

# Для добавления элемента в список используется метод append
collection.append('OrderDict')
print(collection)
# Метод extend передает список1 в конец списка2
collection.extend(['ponyset', 'unidict'])
# Так же можно использовать перегруженый оператор +=
collection += [None]
# Что бы удалить элемент списка используется оператор del
del collection[4]
# Полезные встроенные функции min max sum
numbers = [4, 14, 19, 654, 2]
print(min(numbers))
print(max(numbers))
print(sum(numbers))
# Метод str.join позволяет форматировать строку, добавляет разделитель
tag_list = ['python', 'course', 'era']
print(', '.join(tag_list))
# Сортировка спиcка
import random

numbers = []
for i in range(10):  # for i in range() аналог цыкла for в с#
    print(i)
    numbers.append(random.randint(1, 20))
print(numbers)

# Метод sort и sorted
print(sorted(numbers))
print(numbers)
numbers.sort()
print(numbers)

# Кортежи. в отличие от списков неизменяемые
empty_tuple = ()
empty_tuple = tuple()

kortej = (int, str, tuple)  # Кортеж
kortej[0] = 1

# За то элементы кортежа можно изменять
blink = ([], [])
blink[0].append(0)
print(blink)

children = ['arbuzov_2000', 'ivanov_2011', 'petrov_2010', 'Bubnov_2015']


def by_year(name):
    return name.split('_')[-1]
    # Делит список по символу _ на списки
    # и берет последний элемент

s_children = sorted(children, key=by_year)
print(s_children)
