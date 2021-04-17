from Map import ShopInterface


class Player:
    def __init__(self, number, player_name):
        self.money = 3
        self.__number__ = number
        self.player_name = player_name
        self.units = []

    def buy_unit(self, unit):
        if self.money >= ShopInterface().buy_unit(unit).cost:
            self.units.append(ShopInterface().buy_unit(unit))
            print(f'Yahoo! A new {unit} in your team!')
        else:
            print('Ooops! You have not enough money :( Try a bit later!')

    def upgrade_unit(self, unit):
        if self.money >= self.units[unit].upgrade_cost and self.units[unit].lvl < self.units[unit].maxlvl:
            self.units[unit].upgrade()
        elif self.money < self.units[unit].upgrade_cost:
            print('Ooops! You have not enough money :( Try a bit later!')
        elif self.units[unit].lvl == self.units[unit].maxlvl:
            print('Ooops! You have already reached the highest level! Try to upgrade something else:)')
