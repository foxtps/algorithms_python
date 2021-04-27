# https://drive.google.com/file/d/1T3PWatIZDxm-aY5rxFwYMU5RVtovlatX/view?usp=sharing

DELTA_POSITION = 96
first_character = input('Введите первую букву: ')
second_character = input('Введите вторую букву: ')
first_character_position = ord(first_character) - DELTA_POSITION
second_character_position = ord(second_character) - DELTA_POSITION
if second_character_position > first_character_position:
    number_character_between = second_character_position - 1 - first_character_position
elif second_character_position < first_character_position:
    number_character_between = first_character_position - 1 - second_character_position
else:
    number_character_between = 0
print(f'Место первой буквы в алфавите: {first_character_position}')
print(f'Место второй буквы в алфавите: {second_character_position}')
print(f'Колличество символов между буквами: {number_character_between}')