from Units.Army import Army
from copy import deepcopy


class Map:
    """
    Класс игровой карты.
    Методы класса считывают информацию о юнитах и постройках.
    """
    def __init__(self, size):
        self.map = [['X'] * size for _ in range(size)]
        self.size = size
        self.info = dict()
        for i in range(size):
            for j in range(size):
                self.info[(i, j)] = []

    def get_symbol(self, coord_x, coord_y):
        """
        Получить символ по координатам.
        """
        return self.map[coord_x][coord_y]

    def get_info(self, coord_x, coord_y):
        """
        Получить информацию о клетке по координатам.
        """
        return self.info[(coord_x, coord_y)]

    def show_map(self):
        """
        Выводит карту.
        """
        for i in range(self.size):
            for j in range(self.size):
                print(self.map[i][j], end='')
            print()

    def search_armies(self):
        """
        Ищет армии на карте.
        :return: список армий на карте
        """
        def add_next_cell(next_cell, army, queue, tmp_map):
            """
            Добавляет в очередь BFS следующую клетку.
            """
            army.add(self.info[(next_cell[0], next_cell[1])][0])
            tmp_map[next_cell[0]][next_cell[1]] = 'X'
            queue.append(next_cell)

        def __bfs__(coords, tmp_map, symbol):
            """
            Находит всех юнитов, которые образуют армию.
            :param coords: координаты точки старта алгоритма.
            :param tmp_map: копия игровой карты, она изменяется в процессе работы.
            :param symbol: армию какого игрока ищем.
            :return: список из символа воинов и найденной армии.
            """
            queue = [coords]
            tmp_map[coords[0]][coords[1]] = 'X'
            army = Army(coords[0], coords[1])

            while queue:
                # Ищем всех соседей клетки
                cell = queue.pop(0)
                if tmp_map[cell[0]][cell[1] + 1] == symbol:
                    next_cell = [cell[0], cell[1] + 1]
                    add_next_cell(next_cell, army, queue, tmp_map)

                if tmp_map[cell[0] + 1][cell[1]] == symbol:
                    next_cell = [cell[0] + 1, cell[1]]
                    add_next_cell(next_cell, army, queue, tmp_map)

                if tmp_map[cell[0] - 1][cell[1]] == symbol:
                    next_cell = [cell[0] - 1, cell[1]]
                    add_next_cell(next_cell, army, queue, tmp_map)

                if tmp_map[cell[0]][cell[1] - 1] == symbol:
                    next_cell = [cell[0], cell[1] - 1]
                    add_next_cell(next_cell, army, queue, tmp_map)
            return symbol, army

        temp_map = deepcopy(self.map)
        armies = []
        for i in range(self.size):  # Проходим по всей карте
            for j in range(self.size):
                if temp_map[i][j] == '$' or temp_map[i][j] == '*':
                    armies.append(__bfs__([i, j], temp_map, temp_map[i][j]))
        return armies

    def change_map(self, coord_x, coord_y, game_entity):
        """
        Изменение клетки по заданным координатам.
        """
        self.map[coord_x][coord_y] = game_entity

# @ - Scout of the first team
# $ - Warrior of the first team
# & - Scout of the second team
# * - Warrior of the second team
# # - Mine of the first team
# + - Mine of the second team
# = - Wall
