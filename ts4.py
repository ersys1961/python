s = input('Введите строку:')
lst = s.split()
for i in range(len(lst)):
    print(f'{i + 1} : {lst[i][:10]}')
