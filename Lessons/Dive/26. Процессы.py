# Процесс и его характеристики
# Что такое процесс?
# Какие процессы запущены в ОС?
# Как запустить python процесс?
# Что делает процесс во время исполнения?
# Характеристики процесса:
#
# Идентификатор процесса, PID
# Объем оперативной памяти
# Стек
# Список открытых файлов
# Ввод/вывод
# простой Python процесс

import time
import os

pid = os.getpid()

while True:
    print(pid, time.time())
    time.sleep(2)

# > $ python ex1.py
# > 15468 1488521934.518766
# > 15468 1488521936.520758
# > 15468 1488521938.522762
# > ...
# Создание процесса на Python
# Как создать дочерний процесс?
# Как работает системный вызов fork?
# Модуль multiprocessing
# Создание процесса на Python

import time
import os

pid = os.fork()
if pid == 0:
    # дочерний процесс
    while True:
        print("child:", os.getpid())
        time.sleep(5)
else:
    # родительский процесс
    print("parent:", os.getpid())
    os.wait()

# > $ python ex2.py
# > parent: 14689
# > child: 14690
# Память родительского и дочернего процесса

import os

foo = "bar"

if os.fork() == 0:
    # дочерний процесс
    foo = "baz"
    print("child:", foo)
else:
    # родительский процесс
    print("parent:", foo)
    os.wait()

# > $ python ex3.py
# > parent: bar
# > child: baz
# Файлы в родительском и дочернем процессе

# $ cat data.txt
# example string1
# example string2

import os

f = open("data.txt")
foo = f.readline()

if os.fork() == 0:
    # дочерний процесс
    foo = f.readline()
    print("child:", foo)
else:
    # родительский процесс
    foo = f.readline()
    print("parent:", foo)

# > $ python ex4.py
# > parent: example string2
# > child: example string2
# Создание процесса, модуль multiprocessing

from multiprocessing import Process

def f(name):
    print("hello", name)

p = Process(target=f, args=("Bob",))
p.start()
p.join()

# > $ python ex5.py
# > hello Bob
# Создание процесса, модуль multiprocessing

from multiprocessing import Process

class PrintProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("hello", self.name)

p = PrintProcess("Mike")
p.start()
p.join()

# > $ python ex6.py
# > hello Mike


