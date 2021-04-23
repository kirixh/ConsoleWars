from Units.Unit import Unit


class Army(Unit):
    def __init__(self, coord_x, coord_y) -> None:
        super().__init__(coord_x, coord_y)
        self._children = []
        self.coords = []

    def add(self, unit) -> None:
        self._children.append(unit)
        unit.parent = self

    def remove(self, unit) -> None:
        self._children.remove(unit)
        unit.parent = None

    def move(self, command, _map) -> (int, int):
        for unit in self._children:
            unit.move(self, command, _map)
        pass

    def attack(self, coord_x, coord_y):
        pass
