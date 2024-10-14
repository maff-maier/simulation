from abc import ABC, abstractmethod

from descriptors import NonNegativeValue


class Entity(ABC):
    hp: int = NonNegativeValue(name='_hp')

    def __init__(self, hp: int) -> None:
        self.hp = hp


class Resource(Entity):
    pass


class Grass(Resource):
    pass


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
    def bite(self, target: Resource) -> None:
        if isinstance(target, Resource):
            return super().bite(target)


class Predator(Creature):
    def bite(self, target: Herbivore) -> None:
        if isinstance(target, Herbivore):
            return super().bite(target)


class Tree(Entity):
    pass


class Rock(Entity):
    pass
