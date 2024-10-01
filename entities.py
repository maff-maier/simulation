from abc import ABC, abstractmethod
from typing import Any


class PositiveValue:
    def __init__(self, name: str) -> None:
        self._name = name

    def __get__(self, instance: Any, owner: Any) -> Any:
        if instance is None:
            return None
        return instance.__dir__[self._name]

    def __set__(self, instance: Any, value: int) -> None:
        if value < 0:
            raise ValueError(f'{self._name.capitalize()} cannot be negative')
        instance.__dict__[self._name] = value


class Entity(ABC):
    hp: int = PositiveValue('_hp')

    def __init__(self, hp: int) -> None:
        self.hp = hp


class StaticEntity(Entity):
    pass


class Rock(StaticEntity):
    def __init__(self, hp: int = 20) -> None:
        super().__init__(hp=hp)


class Tree(StaticEntity):
    def __init__(self, hp: int = 50) -> None:
        super().__init__(hp=hp)


class Resource(Entity):
    pass


class Grass(Resource):
    def __init__(self, hp: int = 5) -> None:
        super().__init__(hp=hp)


class Creature(Entity):
    action_points: int = PositiveValue('_action_points')
    attack: int = PositiveValue('_attack')

    def __init__(self, hp: int, aciton_points: int, attack: int) -> None:
        super().__init__(hp=hp)
        self.action_points = aciton_points
        self.attack = attack

    @abstractmethod
    def make_move(self) -> None:
        pass

    @abstractmethod
    def is_possible_bite(self, entity: Entity) -> None:
        pass

    @abstractmethod
    def _bite(self, entity: Entity) -> None:
        entity.hp -= self.attack


class Herbivore(Creature):
    def _bite(self, entity: Resource) -> None:
        super()._bite(entity=entity)

    def is_possible_bite(self, entity: Resource) -> bool:
        return isinstance(entity, Resource)


class Predator(Creature):
    def is_possible_bite(self, entity: Herbivore) -> None:
        return isinstance(entity, Herbivore)

    def _bite(self, entity: Herbivore) -> None:
        super()._bite(entity=entity)


class Sheep(Herbivore):
    def __init__(self, hp: int = 10, action_points: int = 2, attack: int = 2) -> None:
        super().__init__(hp=hp, aciton_points=action_points, attack=attack)

    def make_move(self) -> None:
        return super().make_move()


class Wolf(Predator):
    def __init__(self, hp: int = 15, action_points: int = 3, attack: int = 3) -> None:
        super().__init__(hp=hp, aciton_points=action_points, attack=attack)

    def make_move(self) -> None:
        return super().make_move()
