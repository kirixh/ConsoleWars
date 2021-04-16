from __future__ import annotations
from Units.Scout import Scout
from Creators.UnitCreator import UnitCreator


class ScoutCreator(UnitCreator):
    def create(self):
        return Scout(1, 1)
