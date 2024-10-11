from random import randrange

from coordinates import Coordinates
from descriptors import NonNegativeValue
from entities import Entity


class World:
    height: int = NonNegativeValue(name='_height')
    width: int = NonNegativeValue(name='_width')

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

        self._map: dict[Entity, Coordinates] = dict()

    def get_entities(self) -> dict[Entity, Coordinates]:
        return self._map

    def get_entity(self, entity: Entity) -> tuple[Entity, Coordinates]:
        return self._map.get(key=entity)

    def add_entity(self, entity: Entity, coords: Coordinates) -> None:
        is_within_bounds = (0 <= coords.height < self.height and
                            0 <= coords.width < self.width)
        is_exists = entity in self._map or coords in self._map.values()

        if not is_exists and is_within_bounds:
            self._map[entity] = coords

    def remove_entity(self, entity: Entity) -> None:
        if entity in self._map:
            del self._map[entity]

    def get_random_empty_coordinates(self) -> Coordinates:
        while True:
            coords = self._get_random_coordinates()

            if coords not in self._map.values():
                return coords

    def get_empty_adjacent_coordinates(self, coords: Coordinates) -> list[Coordinates]:
        shifts = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        adjacent_coords = list()

        for hshift, wshift in shifts:
            height = coords.height + hshift
            width = coords.width + wshift
            
            is_within_bounds = (0 <= height < self.height and
                            0 <= width < self.width)
            is_exists = coords in self._map.values()
            
            if not is_exists and is_within_bounds:
                adjacent_coords.append(Coordinates(height=height, width=width))

        return adjacent_coords

    def _get_random_coordinates(self) -> Coordinates:
        return Coordinates(height=randrange(self.height), width=randrange(self.width))
