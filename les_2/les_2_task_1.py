#https://drive.google.com/file/d/1KcYCD6cHMvxzB9i7XrnoOqvJCCrx-Ay-/view?usp=sharing
while True:
    print('Введите знак операции "+", "-", "*", "/"\n или "0" для выхода из программы')
    sign_operation = input('Знак: ')
    if sign_operation == '0':
        break
    if sign_operation == '+' or sign_operation == '-' or sign_operation == '*' or sign_operation == '/':
        first_number = float(input('Введите первое число: '))
        second_number = float(input('Введите второе число: '))
        if sign_operation == '+':
            rezult = first_number + second_number
            print(f'{first_number} {sign_operation} {second_number} = {rezult}')
        elif sign_operation == '-':
            rezult = first_number - second_number
            print(f'{first_number} {sign_operation} {second_number} = {rezult}')
        elif sign_operation == '*':
            rezult = first_number * second_number
            print(f'{first_number} {sign_operation} {second_number} = {rezult}')
        elif sign_operation == '/':
            if second_number != 0:
                rezult = first_number / second_number
                print(f'{first_number} {sign_operation} {second_number} = {rezult}')
            else:
                print('Делить на ноль нельзя!')
    else:
        print('Ввели неправильный знак!')
