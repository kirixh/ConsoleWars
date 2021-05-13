from __future__ import annotations
from abc import ABC, abstractmethod


class BuildingCreator(ABC):
    """
    Абстрактный класс, создающий объект постройки.
    """
    @abstractmethod
    def create(self, game_map, symb, *coords):
        pass
