import random
import timeit
import cProfile

def index_even_elements(N):
    array = [random.randint(2, N*100) for _ in range(N)]
    array_index = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            array_index.append(i)
    return array_index


result = index_even_elements(10000)
#print(f'Массив индексов чётных элементов: {result}')

print(timeit.timeit('index_even_elements(10)', number=1000, globals=globals()))        # 0.018507626
print(timeit.timeit('index_even_elements(100)', number=1000, globals=globals()))       # 0.17636715
print(timeit.timeit('index_even_elements(1_000)', number=1000, globals=globals()))     # 1.739942552
print(timeit.timeit('index_even_elements(10_000)', number=1000, globals=globals()))    # 17.384308986

cProfile.run('index_even_elements(1_000_000)')

"""
          5841570 function calls in 3.378 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.048    0.048    3.378    3.378 <string>:1(<module>)
        1    0.245    0.245    3.330    3.330 les_4_task_1_1.py:5(index_even_elements)
        1    0.515    0.515    3.012    3.012 les_4_task_1_1.py:6(<listcomp>)
  1000000    0.984    0.000    1.987    0.000 random.py:200(randrange)
  1000000    0.509    0.000    2.496    0.000 random.py:244(randint)
  1000000    0.689    0.000    1.003    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    3.378    3.378 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   500197    0.073    0.000    0.073    0.000 {method 'append' of 'list' objects}
  1000000    0.119    0.000    0.119    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1341367    0.195    0.000    0.195    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

"""
При тестировании видно линейную зависимость, при увеличении диапазона в 10 раз увеличивается время выполнения в 10 раз.
Провисание происходит при генерации списка, и немного при методе 'append'
"""