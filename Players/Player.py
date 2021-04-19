from Creators.WarriorCreator import WarriorCreator
from Creators.ScoutCreator import ScoutCreator
from Creators.MineCreator import MineCreator
from Creators.WallCreator import WallCreator


class Player:
    def __init__(self, number, player_name, scout_symb, warrior_symb, mine_symb, game_map):
        self.money = 3
        self.__number__ = number
        self.player_name = player_name
        self.scout_symb = scout_symb
        self.warrior_symb = warrior_symb
        self.mine_symb = mine_symb
        self.game_map = game_map
        self.units = []

    def buy_unit(self, unit, *coords):
        if self.money >= \
                ShopInterface(self.game_map).buy_unit(unit, self.scout_symb,
                                                      self.warrior_symb, *coords).cost:
            self.units.append(ShopInterface(self.game_map)
                              .buy_unit(unit, self.scout_symb, self.warrior_symb, *coords))
            print(f'Yahoo! A new {unit} in your team!')
        else:
            print('Ooops! You have not enough money :( Try a bit later!')

    def buy_building(self, building, *coords):
        if self.money >= ShopInterface(self.game_map).buy_building(building, self.mine_symb, *coords).cost:
            self.units.append(ShopInterface(self.game_map).buy_building(building, self.mine_symb, *coords))
            print(f'Yahoo! A new {building} in your owning!')
        else:
            print('Ooops! You have not enough money :( Try a bit later!')

    def upgrade_unit(self, unit, coords):
        if self.money >= self.units[unit].upgrade_cost and self.units[unit].lvl < self.units[unit].maxlvl:
            self.units[unit].upgrade()
        elif self.money < self.units[unit].upgrade_cost:
            print('Ooops! You have not enough money :( Try a bit later!')
        elif self.units[unit].lvl == self.units[unit].maxlvl:
            print('Ooops! You have already reached the highest level! Try to upgrade something else:)')


class ShopInterface:
    # тут должы быть координаты
    def __init__(self, game_map):
        self.game_map = game_map

    def buy_unit(self, unit_type, scout_symb, warrior_symb, *coords):
        shop_list = {'scout': (ScoutCreator(), scout_symb), 'warrior': (WarriorCreator(), warrior_symb)}
        return shop_list[unit_type][0].create(self.game_map, shop_list[unit_type][1], *coords)

    #
    def buy_building(self, building_type, mine_symb, *coords):
        shop_list = {'mine': (MineCreator(), mine_symb), 'wall': (WallCreator(), '=')}
        return shop_list[building_type][0].create(self.game_map, shop_list[building_type][1], *coords)

    def upgrade_unit(self):
        pass
