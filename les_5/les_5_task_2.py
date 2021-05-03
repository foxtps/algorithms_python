from collections import deque
'''
# Десятичная система счисления
BAZE = 10
TEN_BAZE = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
HEX_BAZE = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

'''

# Шестнадцатеричная система счисления
BAZE = 16
TEN_BAZE = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
 'D': 13, 'E': 14, 'F': 15}
HEX_BAZE = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def sum_hex(a, b):
    result = deque()
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        b.appendleft('0' * (len_a - len_b))
    if len_b > len_a:
        a.appendleft('0' * (len_b - len_a))

    excess = 0
    for i in range(len(a)):
        res = TEN_BAZE[a.pop()] + TEN_BAZE[b.pop()] + excess
        if res >= BAZE:
            excess = 1
            res = res - BAZE
        else:
            excess = 0
        result.appendleft(HEX_BAZE[res])
    if excess == 1:
        result.appendleft('1')

    return result


num1 = deque(input('Введите первое число: ').upper())
num2 = deque(input('Введите второе число: ').upper())
print(f'{num1=}')
print(f'{num2=}')
print(f'Сумма: {sum_hex(num1, num2)}')
