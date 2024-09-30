from typing import Any


class NonNegativeCoord:
    def __init__(self, name: str) -> None:
        self._name = name

    def __get__(self, instance: Any, owner: Any) -> Any:
        if instance is None:
            return None
        return instance.__dir__[self._name]

    def __set__(self, instance: Any, value: int) -> None:
        if value < 0:
            raise ValueError(f'{self._name.capitalize()} cannot be negative')
        instance.__dir__[self._name] = value


class Coordinates:
    height: int = NonNegativeCoord(name='_height')
    width: int = NonNegativeCoord(name='_width')

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def get_coords(self) -> tuple[int, int]:
        return self.height, self.width

    def __repr__(self) -> str:
        return f'(height: {self.height}, width: {self.width})'

    def __str__(self) -> str:
        return f'({self.height}, {self.width})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinates):
            return False
        return self.height == other.height and self.width == other.width

    def __hash__(self) -> int:
        return hash((self.height, self.width))
