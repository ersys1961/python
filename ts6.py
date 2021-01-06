from itertools import count
from itertools import cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)
print('-'*10)
lst1 = [4, 'привет', False, 99.9]
с = 0
for el in cycle(lst1):
    if с > 9:
        break
    print(el)
    с += 1
