#https://drive.google.com/file/d/1KcYCD6cHMvxzB9i7XrnoOqvJCCrx-Ay-/view?usp=sharing
def summa_items(n, first_item=1.0):
    if n == 1:
        return first_item
    first_item = first_item / -2
    return first_item + summa_items(n - 1, first_item)


count_item = int(input('Введите количество элементов: '))
rezult = summa_items(count_item)
print(f'Сумма = {rezult}')