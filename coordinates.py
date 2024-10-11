from typing import Any

from descriptors import NonNegativeValue


class Coordinates:
    height: int = NonNegativeValue(name='_height')
    width: int = NonNegativeValue(name='_width')

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def get_coordinates(self) -> tuple[int, int]:
        return (self.height, self.width)

    def __hash__(self) -> int:
        return hash((self.height, self.width))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Coordinates):
            return False
        return self.height == other.height and self.width == other.width


