#https://drive.google.com/file/d/1KcYCD6cHMvxzB9i7XrnoOqvJCCrx-Ay-/view?usp=sharing
number = int(input('Введите целое число: '))
summa_even = 0
summa_odd = 0
while number > 0:
    if number % 2 == 0:
        summa_even = summa_even + 1
    else:
        summa_odd = summa_odd + 1
    number = number // 10
print(f'Количество четных - {summa_even} и нечетных - {summa_odd}')