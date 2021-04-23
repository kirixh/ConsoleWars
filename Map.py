"""sc1 = Scout(0,0)
sc2 = Scout(1,0)
move(1,0)
self.info(1,0) -> sc2
sc2.move()
"""
from Units.Army import Army
from copy import deepcopy


class Map:
    def __init__(self, size):
        self.map = [['X'] * size for _ in range(size)]
        self.size = size
        self.info = dict()
        for i in range(size):
            for j in range(size):
                self.info[(i, j)] = []

    def get_symbol(self, coord_x, coord_y):
        return self.map[coord_x][coord_y]

    def get_info(self, coord_x, coord_y):
        return self.info[(coord_x, coord_y)]

    def show_map(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.map[i][j], end='')
            print()

    def search_armies(self):
        def __bfs__(coords, tmp_map, symbol):
            queue = [coords]
            tmp_map[coords[0]][coords[1]] = 'X'
            army = Army(coords[0], coords[1])

            while queue:
                cell = queue.pop(0)
                if tmp_map[cell[0]][cell[1] + 1] == symbol:
                    next_cell = [cell[0], cell[1] + 1]
                    army.add(self.info[(next_cell[0], next_cell[1])][0])
                    tmp_map[next_cell[0]][next_cell[1]] = 'X'
                    queue.append(next_cell)

                if tmp_map[cell[0] + 1][cell[1]] == symbol:
                    next_cell = [cell[0] + 1, cell[1]]
                    army.add(self.info[(next_cell[0], next_cell[1])][0])
                    tmp_map[next_cell[0]][next_cell[1]] = 'X'
                    queue.append(next_cell)

                if tmp_map[cell[0] - 1][cell[1]] == symbol:
                    next_cell = [cell[0] - 1, cell[1]]
                    army.add(self.info[(next_cell[0], next_cell[1])][0])
                    tmp_map[next_cell[0]][next_cell[1]] = 'X'
                    queue.append(next_cell)

                if tmp_map[cell[0]][cell[1] - 1] == symbol:
                    next_cell = [cell[0], cell[1] - 1]
                    army.add(self.info[(next_cell[0], next_cell[1])][0])
                    tmp_map[next_cell[0]][next_cell[1]] = 'X'
                    queue.append(next_cell)
            return symbol, army

        temp_map = deepcopy(self.map)
        armies = []
        for i in range(self.size):
            for j in range(self.size):
                if temp_map[i][j] == '$' or temp_map[i][j] == '*':
                    armies.append(__bfs__([i, j], temp_map, temp_map[i][j]))
        return armies

    def change_map(self, coord_x, coord_y, game_entity):
        self.map[coord_x][coord_y] = game_entity

# @ - Scout of the first team
# $ - Warrior of the first team
# & - Scout of the second team
# * - Warrior of the second team
# # - Mine of the first team
# + - Mine of the second team
# = - Wall
