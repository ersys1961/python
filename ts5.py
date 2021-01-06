from functools import reduce


def my_mul(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


sum1 = reduce(my_mul, [i for i in range(100, 1001) if i % 2 == 0])
print(sum1)
