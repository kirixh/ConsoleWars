from Units.Unit import Unit


class Warrior(Unit):
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
