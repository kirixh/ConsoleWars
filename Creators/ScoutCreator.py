from __future__ import annotations
from Units.Scout import Scout
from Creators.UnitCreator import UnitCreator


class ScoutCreator(UnitCreator):

    def create(self, game_map, symb, *coords):
        game_map.map[coords[0]][coords[1]] = symb
        return Scout(coords[0], coords[1])
