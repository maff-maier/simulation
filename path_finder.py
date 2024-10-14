from typing import Protocol

from coordinates import Coordinates


class DistanceCalculator(Protocol):
    def calculate(self, base: Coordinates, target: Coordinates) -> int:
        pass


class ManhattanDistanceCalculator(DistanceCalculator):
    def calculate(self, base: Coordinates, target: Coordinates) -> int:
        return abs((base.height - target.height) + (base.width - target.width))


class PathFinder(Protocol):
    def find(self, base: Coordinates, target: Coordinates) -> list[Coordinates]:
        pass
