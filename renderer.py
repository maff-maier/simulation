

from copy import copy
from typing import Protocol

from loader import IconLoader
from world import World


class Renderer(Protocol):
    def render(self, world: World) -> None:
        pass


class CliRenderer(Renderer):
    def __init__(self, icons_path: str = 'icons.json') -> None:
        self._icons = IconLoader().load(path=icons_path)

    def render(self, world: World) -> None:
        row = [self._icons['space']] * world.width
        world_map = [copy(row) for _ in range(world.height)]

        for entity, coords in world.get_entities().items():
            class_name = entity.__class__.__name__.lower()
            # review
            world_map[coords.height][coords.width] = self._icons[class_name]

        for row in world_map:
            for column in range(len(row)):
                print(row[column], sep='', end='')
            print()
