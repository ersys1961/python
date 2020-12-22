a = float(input('Введите начальную дистанцию A:'))
b = float(input('Введите конечную дистанцию B:'))
nd = 1
a1 = a
while a1 < b:
    nd += 1
    a1 = a1 * 1.1
#    print(nd, a1)
print(nd)