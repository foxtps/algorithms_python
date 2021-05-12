import random


def trend(t1, t2, reverse=False):
    if reverse:
        return t1 < t2
    else:
        return t1 > t2


def sort_merge(a, reverse=False):
    if len(a) <= 1:
        return a
    if len(a) == 2:
        if trend(a[0], a[1], reverse):
            a[0], a[1] = a[1], a[0]
        return a
    a_left = sort_merge(a[:len(a)//2], reverse)
    a_right = sort_merge(a[len(a)//2:], reverse)

    i = j = 0
    while i < len(a_left) and j < len(a_right):
        if trend(a_left[i], a_right[j], reverse):
            a[i + j] = a_right[j]
            j += 1
        elif trend(a_right[j], a_left[i], reverse):
            a[i + j] = a_left[i]
            i += 1

    while i < len(a_left):
        a[i + j] = a_left[i]
        i += 1

    while j < len(a_right):
        a[i + j] = a_right[j]
        j += 1

    return a


N = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(N)]
# array = [4, 2, 8, 6, 0, 5, 1, 7, 3, 9]
print(array)
print(sort_merge(array, False))
