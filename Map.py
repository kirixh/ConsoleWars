

"""sc1 = Scout(0,0)
sc2 = Scout(1,0)
move(1,0)
self.info(1,0) -> sc2
sc2.move()
"""


class Map:
    def __init__(self, size):
        self.map = [['X'] * size for _ in range(size)]
        self.size = size
        # self.info = {(0, 0): [Scout(1, 1), '$', lvl, num]}

    def get_information(self, coord_x, coord_y):
        return self.map[coord_x][coord_y]

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
                    next_cell = [cell[0], cell[1] + 1]
                    tmp_map[next_cell[0]][next_cell[1]] = 'X'
                    queue.append(next_cell)
                    if next_cell[1] > r_border:
                        r_border = next_cell[1]

                if tmp_map[cell[0] + 1][cell[1]] == symbol:
                    next_cell = [cell[0] + 1, cell[1]]
                    tmp_map[next_cell[0]][next_cell[1]] = 'X'
                    queue.append(next_cell)
                    if next_cell[0] > bot_border:
                        bot_border = next_cell[0]

                if tmp_map[cell[0] - 1][cell[1]] == symbol:
                    next_cell = [cell[0] - 1, cell[1]]
                    tmp_map[next_cell[0]][next_cell[1]] = 'X'
                    queue.append(next_cell)
                    if next_cell[0] < top_border:
                        top_border = next_cell[0]

                if tmp_map[cell[0]][cell[1] - 1] == symbol:
                    next_cell = [cell[0], cell[1] - 1]
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
        return armies


# @ - Scout of the first team
# $ - Warrior of the first team
# & - Scout of the second team
# * - Warrior of the second team
# # - Mine of the first team
# + - Mine of the second team
# = - Wall



