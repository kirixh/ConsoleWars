from __future__ import annotations
from Buildings.Mine import Mine
from Creators.BuildingCreator import BuildingCreator


class MineCreator(BuildingCreator):
    """
    Класс, создающий шахту и добавляющий ее на карту.
    """
    def create(self, game_map, symb, *coords):
        game_map.map[coords[0]][coords[1]] = symb
        # Добавление информации о созданном объекте на карту.
        game_map.info[(coords[0], coords[1])].append(Mine(coords[0], coords[1]))
        return game_map.info[(coords[0], coords[1])][0]
