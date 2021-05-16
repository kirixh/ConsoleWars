import unittest
from unittest.mock import patch
from Players.Player import ShopInterface
from Units.Scout import Scout
from Units.Warrior import Warrior
from Buildings.Wall import Wall
from Buildings.Mine import Mine
from Players.Player import Player
from Map import Map
from Units.Army import Army


class Checkpoint1Test(unittest.TestCase):

    def setUp(self):
        self.game_map = Map(22)
        self.interface = ShopInterface(self.game_map)

    def test_buy_scout(self):
        self.assertTrue(isinstance(self.interface.buy_unit("scout", '@', '#', 1, 1), Scout))

    def test_buy_warrior(self):
        self.assertTrue(isinstance(self.interface.buy_unit("warrior", '@', '#', 2, 2), Warrior))

    def test_buy_wall(self):
        self.assertTrue(isinstance(self.interface.buy_building("wall", '=', 3, 2), Wall))

    def test_buy_mine(self):
        self.assertTrue(isinstance(self.interface.buy_building("mine", '#', 4, 4), Mine))


class Checkpoint2Test(unittest.TestCase):
    def setUp(self):
        self.game_map = Map(22)
        self.player = Player(1, "Kir", '@', '$', '#', self.game_map)

    def test_player_buy_unit(self):
        self.player.buy_unit("warrior", 1, 5, 5)
        self.assertTrue(isinstance(self.player.units[0], Warrior))
        self.assertTrue(self.game_map.get_symbol(5, 5) == '$')
        self.assertTrue(isinstance(self.game_map.get_info(5, 5)[0], Warrior))

    def test_search_armies(self):
        self.player.buy_unit("warrior", 1, 5, 5)
        self.player.buy_unit("warrior", 1, 5, 6)
        self.assertTrue(isinstance(self.game_map.search_armies()[0][1], Army))

    @patch('Map.Map.search_armies', return_value=[['$', Army(1, 1)]])
    def test_mock_search_armies(self, search_armies):
        self.assertTrue(isinstance(search_armies()[0][1], Army))


if __name__ == "__main__":
    unittest.main()
