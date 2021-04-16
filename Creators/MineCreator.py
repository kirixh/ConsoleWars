from __future__ import annotations
from Buildings.Mine import Mine
from Creators.BuildingCreator import BuildingCreator


class MineCreator(BuildingCreator):
    def create(self):
        return Mine(1, 1)
