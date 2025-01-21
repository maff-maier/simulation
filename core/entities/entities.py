from abc import ABC
from typing import Type

from configs.attributes import Attributes
from core.utils.descriptors import NonNegativeValue


class Entity(ABC):
    hp: int = NonNegativeValue('_hp')

    def __init__(self, attributes: Attributes) -> None:
        self.hp = attributes.hp
        self._max_hp = attributes.hp

    def __repr__(self) -> str:
        return f'{type(self).__name__}'


class Creature(Entity):
    target_type: Type[Entity]
    action_points: int = NonNegativeValue('_action_points')
    damage: int = NonNegativeValue('_damage')
    satiety: int = NonNegativeValue('_satiety')
    max_satiety: int = NonNegativeValue('_max_satiety')

    def __init__(self, attributes: Attributes) -> None:
        super().__init__(attributes=attributes)
        self.action_points = attributes.action_points
        self.damage = attributes.damage
        self.satiety = attributes.satiety
        self.max_satiety = attributes.satiety

    def bite(self, target: Entity) -> None:
        if isinstance(target, type(self).target_type):
            target.hp = 0 if target.hp <= self.damage else (
                target.hp - self.damage)

    def hungering(self, satiety_scale: int) -> None:
        if not satiety_scale:
            return

        satiety = self.satiety + satiety_scale
        if satiety_scale > 0:
            self.satiety = min(satiety, self.max_satiety)
        else:
            self.satiety = max(satiety, 0)

            if satiety < 0:
                self._exhauste(exhausted_scale=abs(satiety))

    def _exhauste(self, exhausted_scale: int) -> None:
        self.hp = 0 if self.hp <= exhausted_scale else (
            self.hp - exhausted_scale)

    def _satisfy(self, satisfy_scale: int) -> None:
        self.hp = self._max_hp if self._max_hp < (
            satisfy_scale + self.hp) else self.hp + satisfy_scale


class Resource(Entity):
    pass


class Herbivore(Creature):
    target_type: Type[Entity] = Resource


class Predator(Creature):
    target_type: Type[Entity] = Herbivore


class StaticEntity(Entity):
    pass


class Grass(Resource):
    pass


class Rock(StaticEntity):
    pass


class Tree(StaticEntity):
    pass
