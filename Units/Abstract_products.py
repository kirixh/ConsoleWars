from __future__ import annotations
from abc import ABC, abstractmethod


class Units(ABC):
    def __init__(self, x, y):
        self.maxlvl = None
        self.x = x
        self.y = y
        self.lvl = 1

    def move(self, command) -> (int, int):
        steps = {'s': (-1, 0), 'b': (1, 0), 'l': (0, -1), 'r': (0, 1), 'q': (0, 0)}
        # проверить, пуста ли клетка
        self.x += steps[command][0]
        self.y += steps[command][1]
        return self.x, self.y

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
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        # поменять состояние клетки на карте
        pass

