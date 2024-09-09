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
    hp = PositiveValue('_hp')

    def __init__(self, hp: int) -> None:
        self.hp = hp

    @abstractmethod
    def make_move(self) -> None:
        pass


class StaticEntity(Entity):
    pass


class Rock(StaticEntity):
    def make_move(self) -> None:
        return super().make_move()


class Tree(StaticEntity):
    def make_move(self) -> None:
        return super().make_move()


class Resource(Entity):
    pass


class Grass(Resource):
    def __init__(self, hp: int = 3) -> None:
        super().__init__(hp=hp)

    def make_move(self) -> None:
        return super().make_move()


class Creature(Entity):
    speed: int = PositiveValue('_speed')
    attack: int = PositiveValue('_attack')

    def __init__(self, hp: int, speed: int, attack: int) -> None:
        super().__init__(hp=hp)
        self.speed = speed
        self.attack = attack

    @abstractmethod
    def _bite(self, entity: Entity) -> None:
        entity.hp -= self.attack


class Herbivore(Creature):
    def _bite(self, entity: Resource) -> None:
        super()._bite(entity=entity)


class Predator(Creature):
    def _bite(self, entity: Herbivore) -> None:
        super()._bite(entity=entity)


class Sheep(Herbivore):
    def __init__(self, hp: int = 10, speed: int = 1, attack: int = 1) -> None:
        super().__init__(hp=hp, speed=speed, attack=attack)


class Wolf(Predator):
    def __init__(self, hp: int, speed: int, attack: int) -> None:
        super().__init__(hp=hp, speed=speed, attack=attack)
