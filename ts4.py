def my_power(x, n):
    return x**n


def my_power1(x, n):
    res = 1
    for i in range(-n):
        res = res / x
    return res


print(my_power(4, -4))
print(my_power1(4, -4))

