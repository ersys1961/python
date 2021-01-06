def fact(n):
    if n == 1:
        yield 1
    else:
        for el1 in fact(n-1):
            yield n * el1


for i in range(1, 6):
    for el in fact(i):
        print(el)
