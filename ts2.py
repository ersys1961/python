cnt = 0
with open('test2.txt', 'r') as f_inp:
    for line in f_inp:
        cnt += 1
        print(f'В строке {cnt} строк {len(line.split())}')
print(f'Всего строк: {cnt}')


