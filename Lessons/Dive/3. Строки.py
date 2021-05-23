# Строки (str)
# Строка – это неизменяемая последовательность юникодных символов

example_string = "Курс про Python на Coursera"
print(example_string)
# Курс про Python на Coursera
print(type(example_string))
# <class 'str'>
example_string = 'Курс про "Python" на "Coursera"'
print(example_string)
# Курс про "Python" на "Coursera"
example_string = "Курс про \"Python\" на \"Coursera\""
print(example_string)
# Курс про "Python" на "Coursera"
# "Cырые" (r-строки):

example_string = "Файл на диске c:\\\\"
print(example_string)

example_string = r"Файл на диске c:\\"
print(example_string)
# Файл на диске c:\\
# Файл на диске c:\\
# Как разбить объявление длинной строки:

example_string = "Perl — это тот язык, который одинаково " \
                 "выглядит как до, так и после RSA шифрования." \
                 "(Keith Bostic)"
print(example_string)
# Perl — это тот язык, который одинаково выглядит как до, так и после RSA шифрования.(Keith Bostic)
example_string = """
Есть всего два типа языков программирования: те, на которые 
люди всё время ругаются, и те, которые никто не использует.

Bjarne Stroustrup
"""
print(example_string)
# Есть всего два типа языков программирования:
# те, на которые люди всё время ругаются, и те,
# которые никто не использует.

# Bjarne Stroustrup
#
# Как объединить 2 строки в одну?

"Можно" + " просто " + "складывать" + " строки"
'Можно просто складывать строки'
"Даже умножать!" * 3
'Даже умножать!Даже умножать!Даже умножать!'
# Строки неизменяемые!
example_string = "Привет"
print(id(example_string))

example_string += ", Мир!"
print(id(example_string))
4379064296
4379064192
# Срезы строк [start:stop:step]
example_string = "Курс про Python на Coursera"
example_string[9:]
'Python на Coursera'
example_string = "Курс про Python на Coursera"
example_string[9:15]
'Python'
example_string = "Курс про Python на Coursera"
example_string[-8:]
'Coursera'
# Использование step:

example_string = "0123456789"
example_string[::2]
'02468'
example_string = "Москва"
example_string[::-1]
'авксоМ'
# У строк есть методы:

quote = """Болтовня ничего не стоит. Покажите мне код.

Linus Torvalds
"""
quote.count("о")
6
"москва".capitalize()
'Москва'
"2017".isdigit()
True
# Оператор in позволяет проверить наличие подстроки в строке:

"3.14" in "Число Пи = 3.1415926"
True
"Алексей" in "Александр Пушкин"
False
# Выражение for .. in позволяет итерироваться по строке:

example_string = "Привет"
for letter in example_string:
    print("Буква", letter)
# Буква П
# Буква р
# Буква и
# Буква в
# Буква е
# Буква т
# Конвертация типов:

num = 999.01

num_string = str(num)

print(type(num_string))
num_string
# <class 'str'>
'999.01'
bool("Непустая строка")
True
bool("")
False
name = ""

if not name:
    print("Имя не заполнено!")
# Имя не заполнено!
# Форматирование строк
# 1-ый способ форматирования:

template = "%s — главное достоинство программиста. (%s)"
template % ("Лень", "Larry Wall")
'Лень — главное достоинство программиста. (Larry Wall)'
# https://docs.python.org/3/library/string.html#format-specification-mini-language
#
# 2-ой способ:

"{} не лгут, но {} пользуются формулами. ({})".format(
    "Цифры", "лжецы", "Robert A. Heinlein"
)
'Цифры не лгут, но лжецы пользуются формулами. (Robert A. Heinlein)'
# Еще способ:

"{num} Кб должно хватить для любых задач. ({author})".format(
    num=640, author="Bill Gates"
)
'640 Кб должно хватить для любых задач. (Bill Gates)'
# И еще f-строки, Python >= 3.6:

subject = "оптимизация"
author = "Donald Knuth"

f"Преждевременная {subject} — корень всех зол. ({author})"
'Преждевременная оптимизация — корень всех зол. (Donald Knuth)'
# Модификаторы форматирования:

num = 8
f"Binary: {num:#b}"
'Binary: 0b1000'
num = 2 / 3
print(num)

print(f"{num:.3f}")
0.6666666666666666
0.667
# Больше описания и примеров в документации:
#
# https://docs.python.org/3/library/string.html
#
# Встроенная функция input()
# Позволяет получить ввод пользователя в виде строки

name = input("Введи свое имя: ")

f"Привет, {name}!"
# Введи свое имя: Александр
# 'Привет, Александр!'
# Байтовые строки (bytes)
# Байт - минимальная единица хранения и обработки цифровой информации. Последовательность байт представляет собой какую-либо информацию (текст, картинку, мелодию...)
#
# Байтовая строка – это неизменяемая последовательность чисел от 0 до 255.
#
# b-литерал для объявления байтовой строки:

example_bytes = b"hello"
print(type(example_bytes))
# <class 'bytes'>
for element in example_bytes:
    print(element)
104
101
108
108
111
# example_bytes = b"привет"
#   File "<ipython-input-48-f10cf569d599>", line 1
#     example_bytes = b"привет"
#                    ^
# SyntaxError: bytes can only contain ASCII literal characters.
# Bytes literals are always prefixed with 'b' or 'B'; they produce an instance of the bytes type instead of the str type. They may only contain ASCII characters; bytes with a numeric value of 128 or greater must be expressed with escapes.

example_string = "привет"
print(type(example_string))
print(example_string)
# <class 'str'>
# привет
encoded_string = example_string.encode(encoding="utf-8")
print(encoded_string)
print(type(encoded_string))
b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
# <class 'bytes'>
# Буква	Кодировка	hex	dec (bytes)	dec	binary
# п	UTF-8	D0 BF	208 191	53439	11010000 10111111
# буква п - https://unicode-table.com/ru/043F/

# Декодируем байты обратно в строку:

decoded_string = encoded_string.decode()
print(decoded_string)
# привет

name = "Taxi"
number = 100
# pattern = "{movie} - {raiting}"
# result = pattern.format(movie=name, raiting=number)
result = f'{name} - {number}'

print(result)

def mov_raiting(name, number):
    result = f'Movie:"{name}", rating: {number}'
    return result
