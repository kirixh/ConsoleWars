from __future__ import annotations
from Units.Products import Scout, Warrior, Mine, Wall
from abc import ABC, abstractmethod


class UnitsCreator(ABC):

    @abstractmethod
    def create(self):
        pass


class BuildingsCreator(ABC):

    @abstractmethod
    def create(self):
        pass


class ScoutCreator(UnitsCreator):
    def create(self):
        return Scout(1, 1)


class WarriorCreator(UnitsCreator):
    def create(self):
        return Warrior(1, 1)


class MineCreator(BuildingsCreator):
    def create(self):
        return Mine(1, 1)


class WallCreator(BuildingsCreator):
    def create(self):
        return Wall(1, 1)
