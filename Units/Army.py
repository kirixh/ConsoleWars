from Units.Unit import Unit


class Army(Unit):
    def __init__(self, coord_x, coord_y) -> None:
        super().__init__(coord_x, coord_y)
        self._children = []

    def add(self, unit) -> None:
        self._children.append(unit)
        unit.parent = self

    def remove(self, unit) -> None:
        self._children.remove(unit)
        unit.parent = self

    def move(self, command) -> (int, int):
        for unit in self._children:
            unit.move(self, command)
        pass

    def attack(self, coord_x, coord_y):
        pass
