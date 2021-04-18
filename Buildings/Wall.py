from Buildings.Building import Building


class Wall(Building):
    def __init__(self, coord_x, coord_y):
        super().__init__(coord_x, coord_y)
        # изменить состояние в map
