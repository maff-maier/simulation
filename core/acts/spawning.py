from typing import Type
from configs.attributes import Attributes
from core.entities.factories import Factory
from core.world.world import World


class Spawning:
    def __init__(self, factory: Type[Factory], attributes: Type[Attributes]) -> None:
        self.factory = factory
        self.attributes = attributes
        
    def act(self, world: World) -> None:
        coordinates = world.get_empty_random_coordinates()
        entity = self.factory.create(attributes=self.attributes)
        
        world.add_entity(entity=entity, coords=coordinates)