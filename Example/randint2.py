import random

randomset = set()

while True:
    new_number = random.randint(1, 10)
    if new_number in randomset:
        break

    randomset.add(new_number)

print(len(randomset)+1)