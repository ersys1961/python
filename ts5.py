rt = [7, 5, 3, 3, 2]
print(rt.index(3))
print(' '.join(str(rt)))
while True:
    s = input('Введите рейтинг.<Enter> - завершить:')
    if s == '':
        break
    irt = int(s)
    cnt = rt.count(irt)
    if cnt > 0:
        pos = rt.index(irt)
        rt.insert(pos + cnt, irt)
    else:
        for i in range(len(rt)):
            inserted = False
            if irt > rt[i]:
                rt.insert(i, irt)
                inserted = True
                break
        if not inserted:
            rt.insert(len(rt), irt)
    print(' '.join(str(rt)))


