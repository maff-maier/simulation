from typing import Protocol

from configs import Config
from entities import Entity
from world import World


class Action(Protocol):
    def execute(self) -> None:
        pass


class CreateEntityAction(Action):
    def execute(self, world: World, config: Config) -> None:
        entity = config.factory().create(attributes=config.attributes())
        coords = world.get_random_empty_coordinates()

        world.add_entity(entity=entity, coords=coords)


class RemoveEntityAction(Action):
    def execute(self, world: World, entity: Entity) -> None:
        world.remove_entity(entity=entity)
