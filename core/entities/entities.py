from abc import ABC
from typing import Type

from core.utils.descriptors import NonNegativeValue


class Entity(ABC):
    hp: int = NonNegativeValue('_hp')

    def __init__(self, hp: int) -> None:
        self.hp = hp

    def __repr__(self) -> str:
        return f'{type(self).__name__}'


class Creature(Entity):
    target_type: Type[Entity] = None
    action_points: int = NonNegativeValue('_action_points')
    damage: int = NonNegativeValue('_damage')
    satiety: int = NonNegativeValue('_satiety')

    def __init__(self, hp: int, action_points: int, damage: int) -> None:
        super().__init__(hp=hp)
        self.action_points = action_points
        self.damage = damage

    def bite(self, target: Entity) -> None:
        if isinstance(target, type(self).target_type):
            target.hp = 0 if target.hp <= self.damage else (target.hp - self.damage)


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
