class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} поехал.')

    def stop(self):
        print(f'Автомобиль {self.name} остановился.')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул {direction}.')

    def show_speed(self):
        print(f'Автомобиль {self.name} скорость {self.speed} км/ч.')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print('Превышена скорость 60 км/ч.')
        super().show_speed()


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print('Превышена скорость 40 км/ч.')
        super().show_speed()


sc = SportCar(200, 'Красный', 'BMW')
pc = PoliceCar(250, 'Желтый',  'Гранта')
tc = TownCar(90, 'Зеленый', 'Vesta')
wc = WorkCar(60, 'Белый', 'Камаз')

sc.go()
sc.turn('налево')
sc.show_speed()
sc.stop()

pc.go()
pc.turn('направо')
pc.show_speed()
pc.stop()

tc.go()
tc.turn('направо')
tc.show_speed()
tc.stop()

wc.go()
wc.turn('назад')
wc.show_speed()
wc.stop()
