# https://drive.google.com/file/d/1T3PWatIZDxm-aY5rxFwYMU5RVtovlatX/view?usp=sharing

import random
print('1. Случайное целое число из диапазона')
first_number_int = int(input('Введите первое число: '))
second_number_int = int(input('Введите второе число: '))
random_number_int = random.randint(first_number_int, second_number_int)
print(f'Случайное целое число {random_number_int}')

print('2. Случайное вещественное число из диапазона')
first_number_float = float(input('Введите первое число: '))
second_number_float = float(input('Введите второе число: '))
random_number_float = random.uniform(first_number_float, second_number_float)
print(f'Случайное вещественное число {random_number_float}')

print('3. Случайный символ из диапазона')
first_character = ord(input('Введите первый символ: '))
second_character = ord(input('Введите второй символ: '))
random_character = random.randint(first_character, second_character)
random_char = chr(random_character)
print(f'Случайный символ {random_char}')
