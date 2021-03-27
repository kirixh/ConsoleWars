from Creators import *


class Map:
    def __init__(self, size):
        self.map = [['X'] * size for _ in range(size)]

    def getinformation(self, x, y):
        pass


class ShopInterface:
    shop_list = {'scout': ScoutCreator(), 'warrior': WallCreator(), 'mine': MineCreator(), 'wall': WallCreator()}

    def buy_unit(self, unit_type):
        nonlocal shop_list
        return shop_list[unit_type]

    def buy_building(self, building_type):
        nonlocal shop_list
        return shop_list[building_type]

    def upgrade_unit(self):
        pass
