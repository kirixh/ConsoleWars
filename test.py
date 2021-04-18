import unittest
from Map import ShopInterface
from Units.Scout import Scout
from Units.Warrior import Warrior
from Buildings.Wall import Wall
from Buildings.Mine import Mine


class Checkpoint1Test(unittest.TestCase):

    def setUp(self):
        self.interface = ShopInterface()

    def test_buy_scout(self):
        self.assertTrue(isinstance(self.interface.buy_unit("scout"), Scout))

    def test_buy_warrior(self):
        self.assertTrue(isinstance(self.interface.buy_unit("warrior"), Warrior))

    def test_buy_wall(self):
        self.assertTrue(isinstance(self.interface.buy_building("wall"), Wall))

    def test_buy_mine(self):
        self.assertTrue(isinstance(self.interface.buy_building("mine"), Mine))

    def test_move_unit(self):
        pass

#class Checkpoint2Test(unittest.TestCase):




if __name__ == "__main__":
    unittest.main()
