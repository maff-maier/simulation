from typing import Protocol

from factories import EntityFactory
from loader import ConfigLoader, load_file
from world_map import WorldMap


class Action(Protocol):
    def execute(self, world_map: WorldMap) -> None:
        pass
    
class CreateEntityAction(Action):
    def execute(self, entity_name: str, factories: dict[str, EntityFactory], world_map: WorldMap) -> None:
        coords = world_map.get_random_coordinates()
        while not world_map.is_empty_coordinates(coords=coords):
            coords = world_map.get_random_coordinates()
        
        factory = factories.get(key=entity_name, default=None)
        if factory is None:
            raise ValueError(f'{entity_name.capitalize()} is not a valid entity name.')
        
        world_map.add_entity(coords=coords, entity=factory.create())
    

class NextStepAction(Action):
    def execute(self, world_map: WorldMap) -> None:
        [entity.make_move() for entity in world_map.entities.values()]

class CreateRandomMapAction(Action):
    def execute(self, world_map: WorldMap) -> None:
        config = load_file(loader=ConfigLoader())
        
        # TODO: Initialize all entity according to coeffs