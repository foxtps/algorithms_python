import random

N = 5
MIN_ITEM = 0
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)]
print(array)

num = None
frequency = 1
for i in array:
    spam = 0
    for j in array:
        if i == j:
            spam += 1
    if spam > frequency:
        num = i
        frequency = spam
if frequency > 1:
    print(f'Чаще всего встречается число {num}, {frequency} раз(а)')
else:
    print(f'Все числа втречаются только 1 раз')
