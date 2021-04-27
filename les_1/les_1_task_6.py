# https://drive.google.com/file/d/1T3PWatIZDxm-aY5rxFwYMU5RVtovlatX/view?usp=sharing

DELTA_POSITION = 96
abc_number = int(input('Введите номер буквы алфавита от 1 до 26: '))
if abc_number >= 1 & abc_number <= 26:
    abc_character = chr(abc_number + DELTA_POSITION)
    print(f'Эта буква {abc_character}')
else:
    print('Ввели неверный номер')