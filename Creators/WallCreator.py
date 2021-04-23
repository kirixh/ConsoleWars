from Creators.BuildingCreator import BuildingCreator
from Buildings.Wall import Wall


class WallCreator(BuildingCreator):
    def create(self, game_map, symb, *coords):
        game_map.map[coords[0]][coords[1]] = symb
        game_map.info[(coords[0], coords[1])].append(Wall(coords[0], coords[1]))
        return game_map.info[(coords[0], coords[1])][0]
