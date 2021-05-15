from __future__ import annotations
from Units.Warrior import Warrior
from Creators.UnitCreator import UnitCreator


class WarriorCreator(UnitCreator):
    """
    Класс, создающий воина и добавляющий его на карту.
    """
    def __init__(self, war_num):
        self.war_number = war_num

    def create(self, game_map, symb, *coords):
        game_map.map[coords[0]][coords[1]] = symb
        # Добавление информации о созданном объекте на карту.
        game_map.info[(coords[0], coords[1])].append(Warrior(coords[0], coords[1], self.war_number))
        return game_map.info[(coords[0], coords[1])][0]

