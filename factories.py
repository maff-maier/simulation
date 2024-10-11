from abc import ABC, abstractmethod

from entities import Entity, Grass, Herbivore, Tree, Rock, Predator


class Factory(ABC):
    @abstractmethod
    def create(self) -> Entity:
        pass


class GrassFactory(Factory):
    def create(self) -> Grass:
        return Grass()


class HerbivoreFactory(Factory):
    def create(self) -> Herbivore:
        return Herbivore()


class TreeFactory(Factory):
    def create(self) -> Tree:
        return Tree()


class RockFactory(Factory):
    def create(self) -> Rock:
        return Rock()


class PredatorFactory(Factory):
    def create(self) -> Predator:
        return Predator()
