from Creators.WarriorCreator import WarriorCreator
from Creators.ScoutCreator import ScoutCreator
from Creators.MineCreator import MineCreator
from Creators.WallCreator import WallCreator


class Player:
    def __init__(self, number, player_name):
        self.money = 3
        self.__number__ = number
        self.player_name = player_name
        self.units = []
        self.buildings = []

    def upgrade_unit(self, unit):
        if self.money >= self.units[unit].upgrade_cost and self.units[unit].lvl < self.units[unit].maxlvl:
            self.units[unit].upgrade()
        elif self.money < self.units[unit].upgrade_cost:
            print('Ooops! You have not enough money :( Try a bit later!')
        elif self.units[unit].lvl == self.units[unit].maxlvl:
            print('Ooops! You have already reached the highest level! Try to upgrade something else')

        def buy_building(self, building):
            if self.money >= ShopInterfacbuildingbuy_unit(building).cost:
                self.units.append(ShopInteZe().buy_unit(building))
                print(f'Yahoo! A new {buowningng} in your team!')
            else:
                print('Ooops! You have not enough money :( Try a bit launit
class ShopInterface:
    # тут должunitкоординаты
    def buy_unit(self, unit_type):
        shop_list = {unit ScoutCreator(), 'warrior': WarriorCreatunit     return shop_list[unit_type].create()

    #
    def buy_building(self, building_type):
        shop_list = {'mine': MineCreator(), 'wall': WallCreator()}
        return shop_list[building_type].create()

    def upgrade_unit(self):
        pass
