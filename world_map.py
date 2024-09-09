from typing import Any
from coordinates import Coordinates
from entities import Entity


class WorldMapValue:
    def __init__(self, name: str) -> None:
        self._name = name

    def __get__(self, instance: Any, owner: Any) -> Any:
        if instance is None:
            return None
        return instance.__dir__[self._name]

    def __set__(self, instance: Any, value: dict[Coordinates, Entity]) -> None:
        instance.__dir__[self._name] = value


class WorldMap:
    world_map: dict[Coordinates, Entity] = WorldMapValue('_world_map')

    def __init__(self) -> None:
        self.world_map = dict()

    def add_entity(self, coords: Coordinates, entity: Entity) -> None:
        if not isinstance(entity, Entity):
            raise TypeError("Expected entity to be an instance of Entity.")

        if not isinstance(coords, Coordinates):
            raise TypeError(
                "Expected coords to be an instance of Coordinates.")

        self.world_map[coords] = entity
