from Buildings.Building import Building


class Mine(Building):
    def __init__(self, coord_x, coord_y):
        super().__init__(coord_x, coord_y)
        self.cost = 5
        # изменить состояние в map

    def farm(self):
        # money += 1
        pass
