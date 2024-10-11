from abc import ABC, abstractmethod
from typing import Any

from descriptors import NonNegativeValue


class Entity(ABC):
    hp: int = NonNegativeValue(name='_hp')

    def __init__(self, hp: int) -> None:
        self.hp = hp


class Resource(Entity):
    pass


class Grass(Resource):
    def __init__(self, hp: int = 4) -> None:
        super().__init__(hp=hp)


class Creature(Entity):
    action_points: int = NonNegativeValue(name='_action_points')
    attack: int = NonNegativeValue(name='_attack')

    def __init__(self, hp: int, action_points: int, attack: int) -> None:
        super().__init__(hp=hp)

        self.action_points = action_points
        self.attack = attack

    @abstractmethod
    def bite(self, target: Entity) -> None:
        target.hp -= self.attack


class Herbivore(Creature):
    def __init__(self, hp: int = 10, action_points: int = 2, attack: int = 2) -> None:
        super().__init__(hp=hp, action_points=action_points, attack=attack)

    def bite(self, target: Resource) -> None:
        if isinstance(target, Resource):
            return super().bite(target)


class Predator(Creature):
    def __init__(self, hp: int = 15, action_points: int = 3, attack: int = 3) -> None:
        super().__init__(hp=hp, action_points=action_points, attack=attack)

    def bite(self, target: Herbivore) -> None:
        if isinstance(target, Herbivore):
            return super().bite(target)


class Tree(Entity):
    def __init__(self, hp: int = 25) -> None:
        super().__init__(hp=hp)


class Rock(Entity):
    def __init__(self, hp: int = 50) -> None:
        super().__init__(hp=hp)
