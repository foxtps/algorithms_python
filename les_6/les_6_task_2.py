# С использованием множества
import random
import sum_memory


N = 25
MIN_ITEM = 0
MAX_ITEM = 100
array = {random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)}
print(array)

array_index = set()
i = 0
for num in array:
    if num % 2 == 0:
        array_index.add(i)
        i += 1
print(f'Массив индексов чётных элементов: {array_index}')

print('*'*15)
print('Занимаемая память: ')
print(sum_memory.sum_size_objs(i, num, array) +
      sum_memory.size_obj(array_index) +
      sum_memory.size_items(array_index - array))




