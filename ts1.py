import time
from itertools import cycle


class TrafficLights:
    # атрибуты класса

    # методы класса
    def __init__(self):
        self._color = 0

    def _send_state(self):
        msg = {1: "красный", 2: "желтый", 3: "зеленый"}
        print(f'Горит: {msg[self._color]}')

    def run(self):
        states = [[1, 7], [2, 2], [3, 5]]
        for el in cycle(states):
            self._color = el[0]
            self._send_state()
            time.sleep(el[1])


tl = TrafficLights()
tl.run()
