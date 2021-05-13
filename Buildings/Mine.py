from Buildings.Building import Building


class Mine(Building):
    """
    Класс шахта.
    При создании объекта на карту ставится символ шахты.
    """
    def __init__(self, coord_x, coord_y):
        super().__init__(coord_x, coord_y)

    def farm(self):
        # money += 1
        pass
