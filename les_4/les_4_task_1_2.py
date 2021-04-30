import random
import timeit
import cProfile

def index_even_elements(N):
    array = [random.randint(1, N*100) for _ in range(N)]
    array_index = [False for _ in range(N)]
    for i, num in enumerate(array):
        if num % 2 == 0:
            array_index[i] = True
    res = [j for j, evnum in enumerate(array_index) if evnum == True]
    return res


result = index_even_elements(10000)
#print(f'Массив индексов чётных элементов: {result}')

print(timeit.timeit('index_even_elements(10)', number=1000, globals=globals()))        # 0.022073015999999987
print(timeit.timeit('index_even_elements(100)', number=1000, globals=globals()))       # 0.19790823500000002
print(timeit.timeit('index_even_elements(1_000)', number=1000, globals=globals()))     # 1.95380062
print(timeit.timeit('index_even_elements(10_000)', number=1000, globals=globals()))    # 19.138882054

cProfile.run('index_even_elements(1_000_000)')

"""
        5342082 function calls in 3.457 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.046    0.046    3.457    3.457 <string>:1(<module>)
        1    0.154    0.154    0.154    0.154 les_4_task_1_2.py:11(<listcomp>)
        1    0.171    0.171    3.411    3.411 les_4_task_1_2.py:5(index_even_elements)
        1    0.513    0.513    2.978    2.978 les_4_task_1_2.py:6(<listcomp>)
        1    0.108    0.108    0.108    0.108 les_4_task_1_2.py:7(<listcomp>)
  1000000    0.973    0.000    1.959    0.000 random.py:200(randrange)
  1000000    0.505    0.000    2.464    0.000 random.py:244(randint)
  1000000    0.678    0.000    0.986    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    3.457    3.457 {built-in method builtins.exec}
  1000000    0.116    0.000    0.116    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1342075    0.192    0.000    0.192    0.000 {method 'getrandbits' of '_random.Random' objects}

"""

"""
При тестировании видно линейную зависимость, при увеличении диапазона в 10 раз увеличивается время выполнения в 10 раз.
Провисание происходит при генерации списков.

Время выполнения увеличилось на 0.1 от предыдущего метода.
"""