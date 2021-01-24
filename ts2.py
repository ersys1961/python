from abc import ABC, abstractmethod


class Dress(ABC):
    @abstractmethod
    def amount_material(self):
        pass


class Coat:
    def __init__(self, title, v):
        self.title = title
        self.v = v

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, v):
        self._v = v

    @property
    def amount_material(self):
        return round(self.v / 6.5 + 0.5, 2)


class Costume:
    def __init__(self, title, h):
        self.title = title
        self.h = h

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        self._h = h

    @property
    def amount_material(self):
        return round(self.h * 2 + 0.3, 2)


l_dress = [Coat('пальто муж, разм 12', 12),
           Coat('пальто жен, разм 11', 11),
           Costume('костюм муж, рост 3', 3),
           Costume('костюм жен, рост 2', 2)]

sum1 = 0
for el in l_dress:
    print(f'{el.title}: {el.amount_material}')
    sum1 += el.amount_material
print(f'всего: {sum1}')
