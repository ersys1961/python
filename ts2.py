class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp1 = input("Введите делимое:")
inp2 = input("Введите делитель:")

try:
    f1 = float(inp1)
    f2 = float(inp2)
    if f2 == 0.0:
        raise OwnError("Деление на 0!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Результат: {f1 / f2}")
