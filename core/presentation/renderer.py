from copy import copy
from typing import Protocol

from core.presentation.loader import IconsLoader
from core.presentation.menu import Menu
from core.world.world import World
from core.utils.states import GameStates


class Renderer(Protocol):
    def render(self, world: World) -> None:
        pass


class CliRenderer:
    def __init__(self, icons_path: str = 'core\\presentation\\icons.json') -> None:
        self._icons = IconsLoader().load(path=icons_path)
        self._menu = Menu()

    def render(self, world: World, state: GameStates) -> None:
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

        self._print_ingame_menu(state=state)

    def _print_ingame_menu(self, state: GameStates) -> None:
        match state:
            case GameStates.RUNNING:
                print(self._menu.get_pause_menu())
            case GameStates.PAUSED:
                print(self._menu.get_continuing_menu())

    def print_start_menu(self) -> None:
        print(self._menu.get_start_menu())
