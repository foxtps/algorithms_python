import random

N = 25
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)]
print(array)

array_index = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        array_index.append(i)
print(f'Массив индексов чётных элементов: {array_index}')