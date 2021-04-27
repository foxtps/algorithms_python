#https://drive.google.com/file/d/1KcYCD6cHMvxzB9i7XrnoOqvJCCrx-Ay-/view?usp=sharing
DIGIT = 10
number = int(input('Введите целое цисло: '))
number_new = 0
while number > 0:
    # Находим остаток от деления
    number_digit = number % DIGIT
    # Увеличиваем разряд и прибавляем остаток от деления
    number_new = number_new * DIGIT + number_digit
    # Отбрасываем последнию цифру в числе
    number = number // DIGIT
print(f'Обратное по порядку: {number_new}')
