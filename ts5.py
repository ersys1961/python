class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Рисует {self._title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Чертит {self._title}')


class Handle(Stationery):
    def draw(self):
        print(f'А это {self._title}')


x = Stationery('канц. принадлежность')
x.draw()

x = Pen('ручка')
x.draw()

x = Pencil('карандаш')
x.draw()

x = Handle('маркер')
x.draw()
