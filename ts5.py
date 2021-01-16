f_out = open('test5_1.txt', 'w', encoding="utf-8")
sum1 = 0.0
while True:
    s = input('Введите строки через пробел. <Enter> - выход:')
    if s == '':
        break
    f_out.write(s)
    lst = s.split()
    for str1 in lst:
        sum1 += float(str1)
    print(f'СУММА= {sum1}')
f_out.close()
