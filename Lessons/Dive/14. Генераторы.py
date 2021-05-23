#Генератор это функция содержащая yield, то есть возврат без прекращения
def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2

for number in even_range(0, 10):
    print(number)

def list_generator(list_obj):
    for item in list_obj:
        yield item
        print('After yielding {}'.format(item))

def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

# Генераторы
def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2
for number in even_range(0, 10):
    print(number)
0
2
4
6
8
ranger = even_range(0, 4)
next(ranger)
0
next(ranger)
2
next(ranger)
# ---------------------------------------------------------------------------
# StopIteration                             Traceback (most recent call last)
# <ipython-input-6-9065b0f81b55> in <module>()
# ----> 1 next(ranger)

# StopIteration:
def list_generator(list_obj):
    for item in list_obj:
        yield item
        print('After yielding {}'.format(item))


generator = list_generator([1, 2])
next(generator)
1
next(generator)
# After yielding 1
# 2
# next(generator)
# After yielding 2
# ---------------------------------------------------------------------------
# StopIteration                             Traceback (most recent call last)
# <ipython-input-10-1d0a8ea12077> in <module>()
# ----> 1 next(generator)

# StopIteration:
def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)
1
1
2
3
5
8
13
21
34
55
def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value: break
        total += value

generator = accumulator()
next(generator)
0
print('Accumulated: {}'.format(generator.send(1)))
Got: 1
Accumulated: 1
print('Accumulated: {}'.format(generator.send(1)))
Got: 1
Accumulated: 2
print('Accumulated: {}'.format(generator.send(1)))
Got: 1
Accumulated: 3
next(generator)
Got: None
# ---------------------------------------------------------------------------
# StopIteration                             Traceback (most recent call last)
# <ipython-input-18-1d0a8ea12077> in <module>()
# ----> 1 next(generator)
#
# StopIteration: