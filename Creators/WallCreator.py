from Creators.BuildingCreator import BuildingCreator
from Buildings.Wall import Wall


class WallCreator(BuildingCreator):
    def create(self):
        return Wall(1, 1)
