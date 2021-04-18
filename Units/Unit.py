from __future__ import annotations
from abc import ABC, abstractmethod
from Map import Map


class Unit(ABC):
    def __init__(self, coord_x, coord_y):
        self.maxlvl = None
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.lvl = 1
        self.number = 0

    def move(self, command, _map: Map) -> (int, int):
        steps = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1), 'stay': (0, 0)}
        if Map.get_information(_map, self.coord_x + steps[command][0], self.coord_y + steps[command][1]) == 'X':
            self.coord_x += steps[command][0]
            self.coord_y += steps[command][1]
        else:
            # если выходим из армии или вступаем в армию - self.in_army = True; Army.add/remove
            print("Sorry, the cell is not available for step")

    def is_in_army(self):
        pass

    @abstractmethod
    def attack(self, coord_x, coord_y):
        pass

    def upgrade(self):
        self.lvl += 1

    def __del__(self):
        # поменять состояние клетки на карте
        pass
