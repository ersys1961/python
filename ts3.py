def my_func(v1, v2, v3):
    if v1 <= v2 and v1 <= v3:
        res = v2 + v3
    else:
        if v2 <= v1 and v2 <= v3:
            res = v1 + v3
        else:
            res = v1 + v2
    return res


print(my_func(1, 2, 3))
print(my_func(1, 1, 1))
print(my_func(3, 2, 5))
print(my_func(5, 6, 1))

