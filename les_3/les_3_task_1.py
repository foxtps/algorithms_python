for i in range(2, 9+1):
    amount = 0
    for j in range(2, 99+1):
        if j % i == 0:
            amount += 1
    print(f'{amount} чисел кратных {i}')
