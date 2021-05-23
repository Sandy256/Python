#Работа с файлами

f = open('filename')

text_modes = ['r', 'w', 'a', 'r+'] # read write append 
binary_modes = ['br', 'bw', 'ba', 'br+']
f = open('filename', 'w') #открытие с модом
f.write('The world is changed. \n I taste') #запись
f.close() #Закрытие
f.read() #Прочитать
f.tell() #Где указатель
f.seek(0) #Переместить указатель в начало
f.readline() #Прочитать конкретную строку

#Работа с файлами через контекстный менеджер

with open('filename') as f:
    print(f.read())

# Файлы
f = open('filename')
text_modes = ['r', 'w', 'a', 'r+']
binary_modes = ['br', 'bw', 'ba', 'br+']
f = open('filename', 'w')
f.write('The world is changed.\nI taste it in the water.\n')
47
f.close()
f = open('filename', 'r+')
f.read()
'The world is changed.\nI taste it in the water.\n'
f.tell()
47
f.read()
''
f.seek(0)
f.tell()
0
print(f.read())
f.close()
# The world is changed.
# I taste it in the water.

f = open('filename', 'r+')
f.readline()
f.close()
'The world is changed.\n'
f = open('filename', 'r+')
f.readlines()
['The world is changed.\n', 'I taste it in the water.\n']
f.close()
f.read()
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-83-94b03372b7c6> in <module>()
#       1 f.close()
# ----> 2 f.read()
#
# ValueError: I/O operation on closed file.
with open('filename') as f:
    print(f.read())

#В питоне существует только три типа IO text, binary, raw


