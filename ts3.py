class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


lst = []
while True:
    inp = input("Введите данные. <stop> - завершение ввода:")
    if inp == 'stop':
        break
    try:
        f1 = float(inp)
        if inp is str:
            raise OwnError("Вы введи строку")
    except ValueError:
        print("Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        lst.append(f1)

print(lst)
