# С использованием списка
import random
import sum_memory

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

print('*'*15)
print('Занимаемая память: ')
print(sum_memory.sum_size_objs(i, array) +
      sum_memory.size_obj(array_index) +
      sum_memory.size_items([item for item in array_index if item not in array]))


