class Complex:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"{self.__x} + i*{self.__y}"

    def __add__(self, other):
        return Complex(self.__x + other.__x, self.__y + other.__y)

    def __mul__(self, other):
        return Complex(self.__x * other.__x - self.__y * other.__y, self.__y * other.__x + self.__x * other.__y)


x1 = Complex(1, 8)
x2 = Complex(2, 9)
y = x1 + x2
print(f'{x1} + {x2} = {y}')

x1 = Complex(0, 1)
x2 = Complex(0, 1)
y = x1 * x2

print(f'{x1} x {x2} = {y}')
