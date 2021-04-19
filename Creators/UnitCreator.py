from __future__ import annotations
from abc import ABC, abstractmethod


class UnitCreator(ABC):
    @abstractmethod
    def create(self, game_map, symb, *coords):
        pass
