from Map import Map
from Players.Player import Player


print("ConsoleWars game has started!\n ")
map_size = int(input("Input the size of the map (size > 20): "))
while map_size <= 20:
    map_size = int(input("Size > 20!!! "))
game_map = Map(map_size)

player1 = Player(1, input("Input first player's name: "), '@', '$', '#', game_map)
player2 = Player(2, input("Input second player's name: "), '&', '*', '+', game_map)
warrior_number = 1
game_map.show_map()


def maingame(player):
    """
    Функция в которой происходит процесс игры.
    :param player: Игрок
    """
    print(f"{player.player_name}, it's your turn!\n"
          f"Here is list of commands:\n"
          f"\tbuy_unit <unit_type> <coord_x> <coord_y>\n"
          f"\tbuy_building <building_type> <coord_x> <coord_y>\n"
          f"\tupgrade_unit <> <coord_x> <coord_y>\n"
          f"\tend (end the turn)")
    while True:
        try:
            global warrior_number
            command = input().split()
            if command[0] == "buy_unit":
                player.buy_unit(command[1], warrior_number, int(command[2]), int(command[3]))
                warrior_number += 1
            elif command[0] == "buy_building":
                player.buy_building(command[1], int(command[2]), int(command[3]))
            elif command[0] == "upgrade_unit":
                # player1.upgrade_unit()
                pass
            elif command[0] == "end":
                print("*" * game_map.size)
                break
            else:
                print("wrong command, try again!")
        except (KeyError, IndexError):
            print("wrong type of purchase, try again!")


def army_setter(map_game):
    """
    Функция которая анализирует карту после каждого и обновляет информацию об армиях.
    :param map_game: Игровая карта карта
    """
    armies = map_game.search_armies()
    player1.armies = []
    player2.armies = []
    for army in armies:
        if army[0] == player1.warrior_symb:
            player1.armies.append(army[1])
        elif army[0] == player2.warrior_symb:
            player2.armies.append(army[1])


while True:
    maingame(player1)
    maingame(player2)
    game_map.show_map()
    army_setter(game_map)
