from abc import ABC, abstractmethod
from typing import Type

from configs.attributes import Attributes
from core.entities.entities import Entity, Grass, Herbivore, Predator, Rock, Tree


class Factory(ABC):
    @classmethod
    @abstractmethod
    def create(cls, attributes: Type[Attributes]) -> Entity:
        pass


class HerbivoreFactory(Factory):
    @classmethod
    def create(cls, attributes: Type[Attributes]) -> Herbivore:
        return Herbivore(attributes=attributes)


class PredatorFactory(Factory):
    @classmethod
    def create(cls, attributes: Type[Attributes]) -> Predator:
        return Predator(attributes=attributes)


class GrassFactory(Factory):
    @classmethod
    def create(cls, attributes: Type[Attributes]) -> Grass:
        return Grass(attributes=attributes)


class RockFactory(Factory):
    @classmethod
    def create(cls, attributes: Type[Attributes]) -> Rock:
        return Rock(attributes=attributes)


class TreeFactory(Factory):
    @classmethod
    def create(cls, attributes: Type[Attributes]) -> Tree:
        return Tree(attributes=attributes)
