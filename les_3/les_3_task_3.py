import random

N = 5
MIN_ITEM = -25
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)]
print(array)

pos_min = 0
pos_max = len(array)-1
for i in range(len(array)):
    if array[i] < array[pos_min]:
        pos_min = i
    if array[i] > array[pos_max]:
        pos_max = i
print(f'минимальное число = {array[pos_min]}, позиция = {pos_min}'
      f', максимальное число = {array[pos_max]}, позиция = {pos_max}')
array[pos_min], array[pos_max] = array[pos_max], array[pos_min]
print(array)
print(f'минимальное число = {array[pos_max]}, позиция = {pos_max}'
      f', максимальное число = {array[pos_min]}, позиция = {pos_min}')
