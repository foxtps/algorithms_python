# https://drive.google.com/file/d/1T3PWatIZDxm-aY5rxFwYMU5RVtovlatX/view?usp=sharing
three_number = int(input('Введите натуральное трёхзначное число: '))
str_three_number = str(three_number)
len_three_number = len(str_three_number)
if len_three_number == 3:
    three_number_1 = three_number//100
    three_number_2 = three_number%100//10
    three_number_3 = three_number%10
    sum_three_number = three_number_1 + three_number_2 + three_number_3
    multi_three_number = three_number_1 * three_number_2 * three_number_3
    print(f'Сумма цифр трёхзначного числа: {sum_three_number}')
    print(f'Произведение цифр трёхзначного числа: {multi_three_number}')
else:
    print(f'Неправильно ввели число')
