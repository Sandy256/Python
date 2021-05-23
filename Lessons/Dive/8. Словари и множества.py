#Словари хранят данные в виде ключ: значение
dict = {}
empty_dict = dict()

collections_map = {
    'mutable': ['list', 'set', 'dict'],
    'immutable': ['tuple', 'frozenset']
}

#Множества хранят в неупорядоченном виде набор уникальных обьектов
set = set()
number_set = {1, 2, 3, 4, 5}

odd_set = set()
even_set = set()

for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even_set.add(number)

print(odd_set)
print(even_set)

union_set = odd_set | even_set # Обьединение множеств
intersection_set = odd_set & even_set

print(union_set)
print(intersection_set)