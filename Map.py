from Creators.WarriorCreator import WarriorCreator
from Creators.ScoutCreator import ScoutCreator
from Creators.MineCreator import MineCreator
from Creators.WallCreator import WallCreator


class Map:
    def __init__(self, size):
        self.map = [['X'] * size for _ in range(size)]
        self.size = size

    def get_information(self, coord_x, coord_y):
        return self.map[coord_y][coord_x]

    def show_map(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.map[i][j], end='')
            print()

    def search_armies(self):
        def __bfs__(coords, tmp_map, size, symbol):
            queue = [coords]
            tmp_map[coords[0]][coords[1]] = 'X'
            l_border = size
            r_border = 0
            top_border = size
            bot_border = 0
            while queue:
                cell = queue.pop(0)
                if tmp_map[cell[0]][cell[1] + 1] == symbol:
                    next_cell = [cell[0], cell[1]+1]
                    tmp_map[next_cell[0]][next_cell[1]] = 'X'
                    queue.append(next_cell)
                    if next_cell[1] > r_border:
                        r_border = next_cell[1]

                if tmp_map[cell[0] + 1][cell[1]] == symbol:
                    next_cell = [cell[0]+1, cell[1]]
                    tmp_map[next_cell[0]][next_cell[1]] = 'X'
                    queue.append(next_cell)
                    if next_cell[0] > bot_border:
                        bot_border = next_cell[0]

                if tmp_map[cell[0] - 1][cell[1]] == symbol:
                    next_cell = [cell[0]-1, cell[1]]
                    tmp_map[next_cell[0]][next_cell[1]] = 'X'
                    queue.append(next_cell)
                    if next_cell[0] < top_border:
                        top_border = next_cell[0]

                if tmp_map[cell[0]][cell[1] - 1] == symbol:
                    next_cell = [cell[0], cell[1]-1]
                    if next_cell[1] < l_border:
                        l_border = next_cell[1]
                    tmp_map[next_cell[0]][next_cell[1]] = 'X'
                    queue.append(next_cell)
            return symbol, l_border, r_border, top_border, bot_border

        temp_map = self.map
        armies = set()
        for i in range(self.size):
            for j in range(self.size):
                if temp_map[i][j] == '$' or temp_map[i][j] == '*':
                    armies.add(__bfs__([i, j], temp_map, self.size, temp_map[i][j]))

# @ - Scout of the first team
# $ - Warrior of the first team
# & - Scout of the second team
# * - Warrior of the second team
# # - Mine of the first team
# + - Mine of the second team
# = - Wall


class ShopInterface:

    def buy_unit(self, unit_type):
        shop_list = {'scout': ScoutCreator(), 'warrior': WarriorCreator()}
        return shop_list[unit_type].create()

    def buy_building(self, building_type):
        shop_list = {'mine': MineCreator(), 'wall': WallCreator()}
        return shop_list[building_type].create()

    def upgrade_unit(self):
        pass
