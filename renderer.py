import os
import platform
from copy import copy
from typing import Protocol, Union

from loader import IconsLoader
from menu import Menu
from world import World
from states import RunningOptions, PausedOptions


class Renderer(Protocol):
    def render(self, world: World) -> None:
        pass


class CliRenderer:
    def __init__(self, icons_path: str = 'icons.json') -> None:
        self._icons = IconsLoader().load(path=icons_path)
        self._menu = Menu()

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
        print()

    def _print_ingame_menu(self, state: Union[RunningOptions, PausedOptions]) -> None:
        if isinstance(state, RunningOptions):
            print(self._menu.get_pause_menu())
        elif isinstance(state, PausedOptions):
            print(self._menu.get_continuing_menu())

    def print_start_menu(self) -> None:
        print(self._menu.get_start_menu())

    def clear_console(self) -> None:
        command = 'cls' if platform.system() == 'Windows' else 'clear'
        os.system(command)
