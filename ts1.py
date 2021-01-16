lines = []
while True:
    line = input('Введите строку.<ENTER> - завершить:')
    if line == '':
        break
    lines.append(line + '\n')
try:  ## так и не смог добиться чтобы сработало исключение как написал. Выводит свою трассировку
    f_out = open('test1.txt', 'w')
    f_out.writelines(lines)
    f_out.close()
except RuntimeError as e:
    print('Ошибка записи в файл text1.txt ' + e)
