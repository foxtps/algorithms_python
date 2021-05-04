import timeit
import cProfile

def prime_number(n):
    lst = []
    k = 0
    for num in range(2, n):
        for i in range(2, num):
            if num % i == 0:
                k += 1
            if k > 0:
                break
        if k == 0:
            lst.append(num)
        else:
            k = 0
    return lst


result = prime_number(1000)
#print(result)

print(timeit.timeit('prime_number(10)', number=1000, globals=globals()))        # 0.006380903000000007
print(timeit.timeit('prime_number(100)', number=1000, globals=globals()))       # 0.18948142099999998
print(timeit.timeit('prime_number(1_000)', number=1000, globals=globals()))     # 11.034482357
print(timeit.timeit('prime_number(10_000)', number=1000, globals=globals()))    # 868.599012646

cProfile.run('prime_number(10_000)')

"""
1233 function calls in 0.894 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.894    0.894 <string>:1(<module>)
        1    0.893    0.893    0.894    0.894 les_4_task_2_2.py:4(prime_number)
        1    0.000    0.000    0.894    0.894 {built-in method builtins.exec}
     1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
"""
При тестировании видно не линейную зависимость, при увеличении диапазона в 10 раз, 
увеличивается и время выполнение в 100 раз, а при увеличении диапазона в 100 раз 
увеличилось время выполнения в 10_000 раз.
Проседание происходит при многократном вызове метода 'append'
Не самая лучшая идея использовать метод 'append' при большом диапазоне.
"""