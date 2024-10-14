from abc import ABC, abstractmethod

from attributes import Attributes, GrassAttributes, HerbivoreAttributes, PredatorAttributes, RockAttributes, TreeAttributes
from entities import Entity, Grass, Herbivore, Tree, Rock, Predator


class Factory(ABC):
    @abstractmethod
    def create(self, attributes: Attributes) -> Entity:
        pass


class GrassFactory(Factory):
    def create(self, attributes: GrassAttributes) -> Grass:
        return Grass(hp=attributes.hp)


class HerbivoreFactory(Factory):
    def create(self, attributes: HerbivoreAttributes) -> Herbivore:
        return Herbivore(hp=attributes.hp, action_points=attributes.action_points, attack=attributes.attack)


class TreeFactory(Factory):
    def create(self, attributes: TreeAttributes) -> Tree:
        return Tree(hp=attributes.hp)


class RockFactory(Factory):
    def create(self, attributes: RockAttributes) -> Rock:
        return Rock(hp=attributes.hp)


class PredatorFactory(Factory):
    def create(self, attributes: PredatorAttributes) -> Predator:
        return Predator(hp=attributes.hp, action_points=attributes.action_points, attack=attributes.attack)
