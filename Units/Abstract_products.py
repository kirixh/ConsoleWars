from __future__ import annotations
from abc import ABC, abstractmethod


class Units(ABC):
    def __init__(self, coord_x, coord_y):
        self.maxlvl = None
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.lvl = 1

    def move(self, command) -> (int, int):
        steps = {'s': (-1, 0), 'b': (1, 0), 'l': (0, -1), 'r': (0, 1), 'q': (0, 0)}
        # проверить, пуста ли клетка
        self.coord_x += steps[command][0]
        self.coord_y += steps[command][1]
        return self.coord_x, self.coord_y

    @abstractmethod
    def attack(self, coord_x, coord_y):
        pass

    def upgrade(self):
        if self.lvl < self.maxlvl:
            self.lvl += 1
            # снять деньги с игрока
        else:
            print("Can't upgrade unit - maxlevel reached. ")

    def __del__(self):
        # поменять состояние клетки на карте
        pass


class Buildings(ABC):
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __del__(self):
        # поменять состояние клетки на карте
        pass
