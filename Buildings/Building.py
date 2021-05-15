from __future__ import annotations
from abc import ABC


class Building(ABC):
    """
    Абстрактный класс построек
    """
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __del__(self):
        # поменять состояние клетки на карте
        pass
