from __future__ import annotations
from abc import ABC, abstractmethod


class Unit(ABC):
    """
    Абстрактный класс Юнит.
    Имеет общие для всех наследников методы move, is_in_army, upgrade.
    Метод attack будет переопределяться у дочерних классов.
    """
    def __init__(self, coord_x, coord_y):
        self.maxlvl = None
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.lvl = 1

    def move(self, command, _map) -> (int, int):
        """
        Перемещает объект класса Unit по карте.
        :param command: направление движения.
        :param _map: карта, на которой происходят изменения.
        """
        steps = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1), 'stay': (0, 0)}
        if _map.get_symbol(self.coord_x + steps[command][0], self.coord_y + steps[command][1]) == 'X':

            _map.change_map(self.coord_x + steps[command][0], self.coord_y + steps[command][1],
                            _map.get_symbol(self.coord_x, self.coord_y))
            _map.change_map(self.coord_x, self.coord_y, 'X')
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
