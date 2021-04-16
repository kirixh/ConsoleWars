from Creators.WarriorCreator import WarriorCreator
from Creators.ScoutCreator import ScoutCreator
from Creators.MineCreator import MineCreator
from Creators.WallCreator import WallCreator


class Map:
    def __init__(self, size):
        self.map = [['X'] * size for _ in range(size)]
        self.size = size

    def getinformation(self, coord_x, coord_y):
        return self.map[coord_y][coord_x]

    def show_map(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.map[i][j], end='')
            print()


class ShopInterface:

    def buy_unit(self, unit_type):
        shop_list = {'scout': ScoutCreator(), 'warrior': WarriorCreator()}
        return shop_list[unit_type].create()

    def buy_building(self, building_type):
        shop_list = {'mine': MineCreator(), 'wall': WallCreator()}
        return shop_list[building_type].create()

    def upgrade_unit(self):
        pass
