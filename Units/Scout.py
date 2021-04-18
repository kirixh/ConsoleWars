from Units.Unit import Unit


class Scout(Unit):
    def __init__(self, coord_x, coord_y):
        super().__init__(coord_x, coord_y)
        self.maxlvl = 5
        self.cost = 3
        self.upgrade_cost = 1

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
