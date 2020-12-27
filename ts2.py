lst = []
while True:
    s = input('Введите элемет списка. <Enter>-закончить ввод:')
    if s == '':
        break
    lst.append(s)
print(lst)
for i in range(0, len(lst) - 1, 2):
    tmp = lst[i]
    lst[i] = lst[i + 1]
    lst[i + 1] = tmp
print(lst)
