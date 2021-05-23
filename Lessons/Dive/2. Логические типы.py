# Логические типы(bool)
True
True
False
False
result = True
print(type(result))
# <
#
# # class 'bool'>


# Оператор
# "равно":

13 == 13
True
# Оператор
# "не равно":

1 != 2
True
# Операторы
# сравнения:

print(3 > 4)
print(3 <= 3)
print(6 >= 6)
print(6 < 5)
False
True
True
False
x = 2
print(1 < x < 3)
True
# Конвертация типов:

bool(12)
True
bool(0)
False
# Логические выражения
# Логическое "и":

x, y = True, False
print(x and y)
False
# Логическое "или":

x, y = True, False
print(x or y)
True
# Логическое отрицание:

y = False
print(not y)
True
# Составные логические выражения:

x, y, z = True, False, True
result = x and y or z
print(result)
True
x = 12
y = False

print(x or y)
12
x = 12
z = "boom"

print(x and z)
# boom
# Задача: определить високосный год или нет?
#
# Год является високосным если он кратен 4, но  при этом не кратен 100, либо кратен
# 400.

year = 2017
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap)
False
import calendar

print(calendar.isleap(1980))
True
