from __future__ import annotations
from Buildings.Mine import Mine
from Creators.BuildingCreator import BuildingCreator


class MineCreator(BuildingCreator):
    def create(self, game_map, symb, *coords):
        game_map.map[coords[0]][coords[1]] = symb
        game_map.info[(coords[0], coords[1])].append(Mine(coords[0], coords[1]))
        return game_map.info[(coords[0], coords[1])][0]
