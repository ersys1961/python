l_prod = []
t_num = 0
while True:
    t_name = input('Введите название,<Enter> -выход:')
    if t_name == '':
        break
    t_num += 1
    try:
        t_price = float(input('Введите цену:'))
    except ValueError:
        t_price = 0
    try:
        t_qnt = float(input('Введите кол-во:'))
    except ValueError:
        t_qnt = 0
    t_unit = input('Введите ед.измерения:')
    l_prod.append((t_num, {'название': t_name, 'цена': t_price, 'количество': t_qnt, 'ед': t_unit}))
print(l_prod)
l_prod_a = {}
for el in l_prod:
    for key, value in el[1].items():
        if not(key in l_prod_a):
            l_prod_a[key] = []
        ed = l_prod_a.setdefault(key)
        ed.append(value)
print(l_prod_a)
