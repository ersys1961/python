dct = {}
with open('test6.txt', 'r', encoding="utf-8") as f_inp:
    for line in f_inp:
        lst = line.split()
        hours = 0.0
        for i in range(1, 4):
            s = lst[i]
            if s.count('(л)') > 0:
                hours += float(s[:s.index('(л)') ])
            elif s.count('(пр)') > 0:
                hours += float(s[:s.index('(пр)')])
            elif s.count('(лаб)') > 0:
                hours += float(s[:s.index('(лаб)')])
        dct[lst[0][:-1]] = hours
print(dct)
