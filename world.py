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

    def get_entity(self, entity: Entity) -> tuple[Entity, Coordinates]:
        return self._map.get(key=entity)

    def add_entity(self, entity: Entity, coords: Coordinates) -> None:
        if entity in self._map:
            self._map[entity] = coords

    def remove_entity(self, entity: Entity) -> None:
        if entity in self._map:
            del self._map[entity]
