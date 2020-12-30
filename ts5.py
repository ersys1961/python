def get_sum(s1):
    lst = s1.split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return sum(lst)


i_sum = 0
qt = False

while True:
    s = input('Введите числа через пробед. q-конец работы:')
    if s == 'q':
        break
    if s.count('q') > 0:
        qt = True
        s = s[:s.index('q')]

    i_sum += get_sum(s)
    print(i_sum)
    if qt:
        break

