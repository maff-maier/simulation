import random
from typing import Protocol, Type

from dying import Dying
from entites_config import EntityConfig
from entities import Creature, Entity
from moving import Moving
from spawning import Spawning
from world import World


class Action(Protocol):
    def perform(self, world: World) -> None:
        pass


class FillWorldAction:
    def __init__(self, entities_config: dict[Type[Entity], EntityConfig]) -> None:
        self.entities_config = entities_config

    def perform(self, world: World) -> None:
        for _, config in self.entities_config.items():
            for _ in range(int(config.spawn_coeff * world.width * world.height)):
                Spawning(factory=config.factory,
                         attributes=config.attributes).act(world=world)


class MakeMoveAction:
    def __init__(self, moving: Moving) -> None:
        self.moving = moving

    def perform(self, world: World) -> None:
        for entity in world.get_all_entities():
            if not isinstance(entity, Creature):
                continue

            self.moving.act(world=world, creature=entity)


class RemoveEntitiesAction:
    def __init__(self, dying: Dying) -> None:
        self.dying = dying

    def perform(self, world: World) -> None:
        to_delete = []
        for entity in world.get_all_entities():
            if not entity.hp:
                to_delete.append(entity)

        for entity in to_delete:
            self.dying.act(world=world, entity=entity)


class ResetActionPointsAction:
    def __init__(self, configs: dict[Type[Entity], EntityConfig]) -> None:
        self.configs = configs

    def perform(self, world: World) -> None:
        for entity in world.get_all_entities():
            entity.action_points = self.configs[entity.__class__].attributes.action_points


class RespawnEntitiesAction:
    def __init__(self, configs: dict[Type[Entity], EntityConfig]) -> None:
        self.configs = configs

    def perform(self, world: World) -> None:
        for _, config in self.configs.items():
            if (random.random() < config.respawn_coeff):
                Spawning(factory=config.factory,
                         attributes=config.attributes).act(world=world)
