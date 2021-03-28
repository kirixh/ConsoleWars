from Creators import *


class Map:
    def __init__(self, size):
        self.map = [['X'] * size for _ in range(size)]
        self.size = size

    def getinformation(self, coord_x, coord_y):
        pass

    def show_map(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.map[i][j], end='')
            print()


class ShopInterface:

    def buy_unit(self, unit_type):
        shop_list = {'scout': ScoutCreator(), 'warrior': WarriorCreator()}
        return shop_list[unit_type]

    def buy_building(self, building_type):
        shop_list = {'mine': MineCreator(), 'wall': WallCreator()}
        return shop_list[building_type]

    def upgrade_unit(self):
        pass
