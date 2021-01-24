class Matrix:
    def __init__(self, param):
        self._param = param

    def __str__(self):
        s = ''
        for el in self._param:
            for el1 in el:
                s += str(el1).rjust(10, ' ')
            s += '\n'
        return s

    def __add__(self, other):
        res = []
        for i in range(0, len(self._param)):
            x = self._param[i]
            y = other._param[i]
            res1 = []
            for j in range(0, len(x)):
                res1.append(x[j] + y[j])
            res.append(res1)
        return Matrix(res)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(m1)
print(m2)
print(m1 + m2)
