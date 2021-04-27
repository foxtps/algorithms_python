# https://drive.google.com/file/d/1T3PWatIZDxm-aY5rxFwYMU5RVtovlatX/view?usp=sharing
"""
&  = and - И
| = or - ИЛИ
^ = xor - исключающее ИЛИ
~ - НЕТ
>> - сдвиг вправо
<< - сдвиг влево
"""
a = 5
b = 6

print('Битовый оператор "И"')
print(f'{a} and {b} = {bin(a & b)}')

print('Битовый оператор "ИЛИ"')
print(f'{a} or {b} = {bin(a | b)}')

print('Битовый оператор "Исключащее ИЛИ"')
print(f'{a} xor {b} = {bin(a ^ b)}')

print('Битовый оператор "НЕТ"')
print(f'НЕ {a} = {bin(~a)}')
print(f'НЕ {b} = {bin(~b)}')

print('Сдвиг вправо на 2 знака')
print(f'{a} >> 2 = {bin(a >> 2)}')

print('Сдвиг влево на 2 знака')
print(f'{a} << 2 = {bin(a << 2)}')
