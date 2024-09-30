from typing import Any
from random import randint

from coordinates import Coordinates
from entities import Entity
from loader import ConfigLoader, load_data


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
        constraints = load_data(loader=ConfigLoader())['constrains']

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
                "Expected coords to be an instance of Coordinates.")

        self.entities[coords] = entity
        
    def get_random_coordinates(self) -> Coordinates:
        # -1 because randint includes both border values
        return Coordinates(height=randint(0, self.height-1), width=randint(0, self.width-1))
    
    def is_empty_coordinates(self, coords: Coordinates) -> bool:
        return self.entities.get(key=coords, default=None) is None
