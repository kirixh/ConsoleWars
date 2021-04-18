from __future__ import annotations
from Units.Warrior import Warrior
from Creators.UnitCreator import UnitCreator


class WarriorCreator(UnitCreator):
    def create(self):
        return Warrior(1, 1, 1)
