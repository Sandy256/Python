import sys

steps_num = int(sys.argv[1])

for i in range(1, steps_num + 1,):
    print((" " * (steps_num - i)) + ("#" * i))