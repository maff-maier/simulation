from abc import ABC, abstractmethod

from entities import Entity, Wolf, Sheep, Rock, Tree, Grass, Creature, StaticEntity, Resource


class EntityFactory(ABC):
    @abstractmethod
    def create(self) -> Entity:
        pass


class CreatureFactory(EntityFactory):
    pass


class PredatorFactory(CreatureFactory):
    pass


class HerbivoreFactory(CreatureFactory):
    pass


class StaticEntityFactory(EntityFactory):
    pass


class ResourceFactory(EntityFactory):
    pass


class WolfFactory(PredatorFactory):
    def create(self) -> Wolf:
        return Wolf()


class SheepFactory(HerbivoreFactory):
    def create(self) -> Sheep:
        return Sheep()


class GrassFactory(ResourceFactory):
    def create(self) -> Grass:
        return Grass()


class RockFactory(StaticEntityFactory):
    def create(self) -> Rock:
        return Rock()


class TreeFactory(StaticEntityFactory):
    def create(self) -> Tree:
        return Tree()
