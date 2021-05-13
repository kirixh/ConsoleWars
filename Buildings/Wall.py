from Buildings.Building import Building


class Wall(Building):
    """
        Класс стена.
        При создании объекта на карту ставится символ стены.
        """
    def __init__(self, coord_x, coord_y):
        super().__init__(coord_x, coord_y)
