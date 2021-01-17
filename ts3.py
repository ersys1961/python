class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {}

    def set_income(self, wage, bonus):
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


p = Position('Иванов', 'Петр', 'программист')
p.set_income(200000, 100000)
print(f'name {p.name}')
print(f'_income {p._income}')
print(f'{p.get_full_name()}  {p.get_total_income()}')
p1 = Position('Петров', 'Иван', 'тестеровщик')
p1.set_income(100000, 50000)
print(f'{p1.get_full_name()}  {p1.get_total_income()}')
