r = float(input('Введите выручку:'))
e = float(input('Введите затраты:'))
p = r - e
if p > 0:
    print('Прибыль = ', p)
    rent = p/r * 100
    print(f'Рентабельность(%) = {rent:.1f}')
    workers = float(input('Введите численность работников:'))
    if workers > 0:
        print(f'Прибыль на работника = {p / workers}')
else:
    print('Убыток = ', -p)
