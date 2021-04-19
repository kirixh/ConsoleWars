import unittest
from Players.Player import ShopInterface
from Units.Scout import Scout
from Units.Warrior import Warrior
from Buildings.Wall import Wall
from Buildings.Mine import Mine
from Units.Unit import Unit
from Map import Map


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

# class Checkpoint2Test(unittest.TestCase):


if __name__ == "__main__":
    unittest.main()
