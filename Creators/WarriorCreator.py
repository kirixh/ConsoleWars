from __future__ import annotations
from Units.Warrior import Warrior
from Creators.UnitCreator import UnitCreator


class WarriorCreator(UnitCreator):
    def create(self, game_map, symb, *coords):
        game_map.map[coords[0]][coords[1]] = symb
        return Warrior(coords[0], coords[1], 1)
