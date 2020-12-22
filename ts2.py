import datetime

while (True):
    s = input('Введите время(сек):')
    if s == '':
        s = '0'
    s = float(s)
    if s < 0.001:
        break
    dt = datetime.timedelta(seconds=s)
#    print(f'{dt:"%h.%m.%s"}')
    print(f'{dt}')