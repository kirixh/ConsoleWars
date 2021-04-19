from Creators.BuildingCreator import BuildingCreator
from Buildings.Wall import Wall


class WallCreator(BuildingCreator):
    def create(self, game_map, symb, *coords):
        game_map.map[coords[0]][coords[1]] = symb
        return Wall(coords[0], coords[1])
