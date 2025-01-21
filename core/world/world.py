from core.world.coordinates import Coordinates
from core.utils.descriptors import NonNegativeValue
from core.entities.entities import Entity


class World:
    height: int = NonNegativeValue('_height')
    width: int = NonNegativeValue('_width')

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width
        self._map: dict[Entity, Coordinates] = dict()

    def get_entity(self, coords: Coordinates) -> Entity:
        entity = [entity for entity, coordinates in self._map.items()
                  if coordinates == coords]
        return entity[0] if len(entity) else None

    def get_coordinates(self, target_entity: Entity) -> Coordinates:
        return self._map.get(target_entity)

    def get_all_entities(self) -> list[Entity]:
        return self._map.keys()

    def get_all_coordinates(self) -> list[Coordinates]:
        return self._map.values()

    def remove_entity(self, entity: Entity) -> None:
        if entity in self._map.keys():
            del self._map[entity]

    def update_coordinates(self, entity: Entity, new_coords: Coordinates) -> None:
        if entity in self._map.keys():
            self._map[entity] = new_coords

    def add_entity(self, entity: Entity, coords: Coordinates) -> None:
        if entity not in self._map.keys():
            self._map[entity] = coords

    def is_within_bounds(self, height: int, width: int) -> bool:
        return (0 <= height < self.height) and (0 <= width < self.width)

    def get_adjacent_coordinates(self, coords: Coordinates) -> list[Coordinates]:
        shifts = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        adjacents = []
        for hshift, wshift in shifts:
            height = coords.height + hshift
            width = coords.width + wshift

            if self.is_within_bounds(height=height, width=width):
                adjacents.append(Coordinates(height=height, width=width))
        return adjacents

    def get_empty_adjacent_coordinates(self, adjacents: list[Coordinates]) -> list[Coordinates]:
        return [adjacent for adjacent in adjacents if adjacent not in self._map.values()]

    def get_empty_random_coordinates(self) -> Coordinates:
        while True:
            coords = self._get_random_coordinates()

            if coords not in self._map.values():
                return coords

    def is_full_map(self) -> bool:
        return self.height * self.width == len(self._map)
    
    def _get_random_coordinates(self) -> Coordinates:
        from random import randrange
        return Coordinates(height=randrange(self.height), width=randrange(self.width))
