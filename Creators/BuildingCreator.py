from __future__ import annotations
from abc import ABC, abstractmethod


class BuildingCreator(ABC):

    @abstractmethod
    def create(self):
        pass