from Creators.BuildingCreator import BuildingCreator
from Buildings.Wall import Wall


class WallCreator(BuildingCreator):
    """
    Класс, создающий стену и добавляющий ее на карту.
    """
    def create(self, game_map, symb, *coords):
        game_map.map[coords[0]][coords[1]] = symb
        # Добавление информации о созданном объекте на карту.
        game_map.info[(coords[0], coords[1])].append(Wall(coords[0], coords[1]))
        return game_map.info[(coords[0], coords[1])][0]
