from __future__ import annotations
from Units.Scout import Scout
from Creators.UnitCreator import UnitCreator


class ScoutCreator(UnitCreator):
    """
    Класс, создающий разведчика и добавляющий его на карту.
    """
    def create(self, game_map, symb, *coords):
        game_map.map[coords[0]][coords[1]] = symb
        # Добавление информации о созданном объекте на карту.
        game_map.info[(coords[0], coords[1])].append(Scout(coords[0], coords[1]))
        return game_map.info[(coords[0], coords[1])][0]

