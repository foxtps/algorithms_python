import random


def trend(t1, t2, reverse=False):
    if reverse:
        return t1 < t2
    else:
        return t1 > t2


def sort_bubble(a, reverse=False):
    n = 1
    k = 1
    while n < len(a):
        transposition = False
        for i in range(len(a) - k):
            if trend(a[i], a[i + 1], reverse):
                a[i], a[i + 1] = a[i + 1], a[i]
                transposition = True
        if transposition:
            k += 1
        else:
            break
        n += 1
        print(a)
    return a


N = 10
ITEM = 100

array = [random.randrange(-ITEM, ITEM) for _ in range(N)]
# array = [1, 8, 4, 9, 0, 3, 2, 5, 7, 6]
print(array)
print(sort_bubble(array, True))
