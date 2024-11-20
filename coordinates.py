from typing import Any

from descriptors import NonNegativeValue


class Coordinates:
    height: int = NonNegativeValue('_height')
    width: int = NonNegativeValue('_width')

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def hash(self) -> int:
        return hash((self.height, self.width))
    
    def __repr__(self) -> str:
        return f'(h={self.height}, w={self.width})'

    def __eq__(self, o: Any) -> bool:
        if not isinstance(o, Coordinates):
            return False
        return self.height == o.height and self.width == o.width
    
    def __lt__(self, o: Any) -> bool:
        if not isinstance(o, Coordinates):
            raise TypeError(f'Cannot compare Coordinates with {type(o).__name__}')
        return (self.height, self.width) < (o.height, o.width)
