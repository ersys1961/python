class Road:
    _on1sm = 25

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def get_mass(self, thickness):
        mass = self._width * self._length * Road._on1sm * thickness
        print(f'При толщине покрытия {thickness} необходимая масса асфальта: {mass}')


print('\nДорога 1')
r = Road(15, 1000)
r.get_mass(5)
print(f'Тест: {15*1000*25*5}')
r.get_mass(4)
print('\nДорога 2')
r = Road(20, 3000)
r.get_mass(10)
r.get_mass(4)
