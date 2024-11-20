from abc import ABC, abstractmethod
from typing import Type

from attributes import Attributes
from entities import Entity, Grass, Herbivore, Predator, Rock, Tree


class Factory(ABC):
    @abstractmethod
    def create(self, attributes: Type[Attributes]) -> Entity:
        pass


class HerbivoreFactory(Factory):
    def create(self, attributes: Type[Attributes]) -> Herbivore:
        return Herbivore(hp=attributes.hp, action_points=attributes.action_points, damage=attributes.damage)


class PredatorFactory(Factory):
    def create(self, attributes: Type[Attributes]) -> Predator:
        return Predator(hp=attributes.hp, action_points=attributes.action_points, damage=attributes.damage)


class GrassFactory(Factory):
    def create(self, attributes: Type[Attributes]) -> Grass:
        return Grass(hp=attributes.hp)


class RockFactory(Factory):
    def create(self, attributes: Type[Attributes]) -> Rock:
        return Rock(hp=attributes.hp)


class TreeFactory(Factory):
    def create(self, attributes: Type[Attributes]) -> Tree:
        return Tree(hp=attributes.hp)

