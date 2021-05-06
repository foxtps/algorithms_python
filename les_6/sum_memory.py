import sys


def size_obj(obj):
    sum_size = sys.getsizeof(obj)
    return sum_size


def size_items(obj):
    sum_size_items = 0
    if isinstance(obj, list) or isinstance(obj, set):
        for item in obj:
            sum_size_items += size_obj(item)
    return sum_size_items


def size_dict_k_v(obj):
    sum_size_k_v = 0
    if isinstance(obj, dict):
        k_set = set()
        v_set = set()
        for k, v in obj.items():
            k_set.add(k)
            v_set.add(v)
        sum_size_k_v = size_items(v_set) + size_items(k_set - v_set)
    return sum_size_k_v


def sum_size_obj(obj):
    return size_obj(obj) + size_items(obj) + size_dict_k_v(obj)


def sum_size_objs(*objs):
    sum_ = 0
    for obj_ in objs:
        sum_ += sum_size_obj(obj_)
    return sum_
