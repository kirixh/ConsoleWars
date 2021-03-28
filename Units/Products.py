from Abstract_products import Units, Buildings


class Scout(Units):
    def __init__(self, coord_x, coord_y):
        super().__init__(coord_x, coord_y)
        self.maxlvl = 5

    def attack(self, coord_x, coord_y):
        if abs(coord_x - self.coord_x) + abs(coord_y - self.coord_y) != 1:
            print("wrong attack coords ")
            # перезапуск
        else:
            pass
            # сравнить уровни и классы юнитов
            # map.getinformation
            # map.delete_unit()

    def jump(self, coord_x, coord_y):
        # если стена - то move
        pass


class Warrior(Units):
    def __init__(self, coord_x, coord_y):
        super().__init__(coord_x, coord_y)
        self.maxlvl = 7

    def attack(self, coord_x, coord_y):
        if abs(coord_x - self.coord_x) + abs(coord_y - self.coord_y) != 1:
            print("wrong attack coords ")
            # перезапуск
        else:
            pass
            # сравнить уровни и классы юнитов
            # map.getinformation
            # map.delete_unit()


class Mine(Buildings):
    def __init__(self, coord_x, coord_y):
        super().__init__(coord_x, coord_y)
        # изменить состояние в map

    def farm(self):
        # money += 1
        pass


class Wall(Buildings):
    def __init__(self, coord_x, coord_y):
        super().__init__(coord_x, coord_y)
        # изменить состояние в map
