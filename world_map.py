from typing import Any
from random import randrange

from coordinates import Coordinates
from entities import Creature, Entity
from loader import ConfigLoader, load_file


class WorldMapValue:
    def __init__(self, name: str) -> None:
        self._name = name

    def __get__(self, instance: Any, owner: Any) -> Any:
        if instance is None:
            return None
        return instance.__dir__[self._name]

    def __set__(self, instance: Any, value: dict[Coordinates, Entity]) -> None:
        instance.__dir__[self._name] = value


class WorldSizeValue:
    def __init__(self, name: str) -> None:
        self._name = name

    def __get__(self, instance: Any, ownder: Any) -> Any:
        if instance is None:
            return None
        return instance.__dir__[self._name]

    def __set__(self, instance: Any, value: int) -> None:
        constraints = load_file(loader=ConfigLoader())['map_constraints']

        if value < constraints[self._name]:
            raise ValueError(
                f'{constraints[self._name.capitalize()]} cannot be less than {constraints[self._name]}')

        instance.__dir__[self._name] = value


class WorldMap:
    entities: dict[Coordinates, Entity] = WorldMapValue('_entities')
    height: int = WorldSizeValue('_height')
    width: int = WorldSizeValue('_width')

    def __init__(self, height: int, width: int) -> None:
        self.entities = dict()
        self.height = height
        self.width = width

    def add_entity(self, coords: Coordinates, entity: Entity) -> None:
        if not isinstance(entity, Entity):
            raise TypeError("Expected entity to be an instance of Entity.")

        if not isinstance(coords, Coordinates):
            raise TypeError(
                "Expected coordinates to be an instance of Coordinates.")

        self.entities[coords] = entity

    def get_random_coordinates(self) -> Coordinates:
        return Coordinates(height=randrange(0, self.height), width=randrange(0, self.width))

    def is_empty_coordinates(self, coords: Coordinates) -> bool:
        return self.entities.get(key=coords, default=None) is None

    def update_entity_coordinates(self, entity: Creature, new_coords: Coordinates) -> None:
        coords = self._find_coordinates_by_entity(entity=entity)

        if coords is None:
            raise ValueError('Entity not found')

        self.entities[new_coords] = self.entities.pop(key=coords)

    def get_reachable_coords(self, coords: Coordinates) -> list[Coordinates]:
        adjacents = self._get_adjacents_coords(target=coords)
        return [adjacent for adjacent in adjacents if self._can_reach(coords=coords, target_coords=adjacent)]

    def _find_coordinates_by_entity(self, entity: Entity) -> Coordinates:
        for coords, ent in self.entities.items():
            if ent == entity:
                return coords
        return None

    def _get_adjacents_coords(self, target: Coordinates) -> list[Coordinates]:
        adjacents = [
            Coordinates(height=target.height+1,
                        width=target.width) if target.height+1 < self.height else None,
            Coordinates(height=target.height-1,
                        width=target.width) if target.height-1 >= 0 else None,
            Coordinates(height=target.height,
                        width=target.width+1) if target.width + 1 < self.width else None,
            Coordinates(height=target.height,
                        width=target.width-1) if target.width - 1 >= 0 else None,
        ]

        return list(filter(lambda x: x is not None, adjacents))

    def _can_reach(self, coords: Coordinates, target_coords: Coordinates) -> bool:
        entity = self.entities[coords]
        target = self.entities.get(key=target, defaulf=None)

        if not isinstance(entity, Creature):
            return False

        if target is None:
            return False

        return entity.is_possible_bite(entity=self.entities[target_coords])
