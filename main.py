from Map import Map
from Players.Player import Player, ShopInterface
print("ConsoleWars game has started!\n ")
game_map = Map(int(input("Input the size of the map: ")))
shop = ShopInterface()
player1 = Player(1, input("Input first player's name: "))
player2 = Player(2, input("Input second player's name: "))

game_map.show_map()
while True:
    print(f"{player1.player_name}, it's your turn!"
          f"Here is list of commands: "
          f"buy_unit <unit_type>"
          f"buy_building <building_type>"
          f"upgrade_unit <>")
    try:
        command = input().split()
        if command[0] == "buy_unit":
            pass



