def my_divide(arg1, arg2):
    try:
        res = arg1 / arg2
    except ZeroDivisionError:
        res = None
    return res


print(100 / 20)
print(100 / 0)
