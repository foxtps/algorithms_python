import timeit
import cProfile

HOLE = 0

def prime_number(n):
    sieve = [i for i in range(n)]
    sieve[1] = HOLE
    for i in range(2, n):
        if sieve[i] != HOLE:
            j = i + i
            while j < n:
                sieve[j] = HOLE
                j += i
    res = [item for item in sieve if item != HOLE]
    return res


#print(prime_number(1000))

print(timeit.timeit('prime_number(10)', number=1000, globals=globals()))        # 0.005356492000000004
print(timeit.timeit('prime_number(100)', number=1000, globals=globals()))       # 0.043577238
print(timeit.timeit('prime_number(1_000)', number=1000, globals=globals()))     # 0.539059062
print(timeit.timeit('prime_number(10_000)', number=1000, globals=globals()))    # 5.83234487

cProfile.run('prime_number(100_000)')

"""
         6 function calls in 0.072 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.072    0.072 <string>:1(<module>)
        1    0.006    0.006    0.006    0.006 les_4_task_2_1.py:15(<listcomp>)
        1    0.058    0.058    0.071    0.071 les_4_task_2_1.py:6(prime_number)
        1    0.007    0.007    0.007    0.007 les_4_task_2_1.py:7(<listcomp>)
        1    0.000    0.000    0.072    0.072 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
При тестировании видно линейную зависимость, при увеличении диапазона в 10 раз, 
увеличивается и время выполнение в 10 раз.
"""