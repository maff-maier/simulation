from copy import copy
from typing import Protocol

from loader import IconsLoader
from world import World


class Renderer(Protocol):
    def render(self, world: World) -> None:
        pass
    
class CliRenderer:
    def __init__(self, icons_path: str = 'icons.json') -> None:
        self._icons = IconsLoader().load(path=icons_path)
        
    def render(self, world: World) -> None:
        width = [self._icons['space']] * world.width
        world_map = [copy(width) for _ in range(world.height)]
        
        entities = world.get_all_entities()
        all_coords = world.get_all_coordinates()
        for entity, coords in zip(entities, all_coords):
            class_name = entity.__class__.__name__.lower()
            world_map[coords.height][coords.width] = self._icons[class_name]
        
        for row in world_map:
            for column in range(len(row)):
                print(row[column], sep='', end='')
            print()