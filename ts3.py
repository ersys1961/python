class OrganicCell:
    def __init__(self, cell):
        self.cell = cell

    @property
    def cell(self):
        return self._cell

    @cell.setter
    def cell(self, cell):
        self._cell = cell

    def __add__(self, other):
        return OrganicCell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell > other.cell:
            return OrganicCell(self.cell - other.cell)
        else:
            raise Exception('SUB: arg2 > arg1')

    def __mul__(self, other):
        return OrganicCell(self.cell * other.cell)

    def __truediv__(self, other):
        return OrganicCell(self.cell // other.cell)

    def make_order(self, row_size):
        rows = self.cell // row_size
        rest = self.cell % row_size
        s = ('*' * row_size + '\n') * rows
        if rest > 0:
            s += '*' * rest
        return s


os1 = OrganicCell(10)
os2 = OrganicCell(15)
os3 = os2 * os1
os4 = os2 / os1
print(os1.cell)
print(os2.cell)
print(os3.cell)
print(os4.cell)
print('4----------')
print(os1.make_order(4))
print(os2.make_order(4))
print(os3.make_order(4))
print(os4.make_order(4))
print('10----------')
print(os1.make_order(10))
print(os2.make_order(10))
print(os3.make_order(10))
print(os4.make_order(10))
