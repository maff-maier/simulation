from typing import Protocol

from coordinates import Coordinates
from loader import IconsLoader, load_data
from world_map import WorldMap


class Renderer(Protocol):
    def render(self, world_map: WorldMap) -> None:
        pass


class CliRenderer(Renderer):
    def __init__(self, path: str) -> None:
        self._icons = self._get_icons(path=path)

    def render(self, world_map: WorldMap) -> None:
        for height in range(world_map.height):
            for width in range(world_map.width):
                curr_coords = Coordinates(height=height, width=width)
                if world_map.is_empty_coordinates(coords=curr_coords):
                    print(self._icons['space'], end='')
                else:
                    # TODO: add attribute name for all concrete classes and synchronize with config names in entities
                    entity = world_map.entities.get(key=curr_coords)
                    print(self._get_icons[entity.__class__.__name__], end='')
            print()

    def _get_icons(self, path: str) -> dict[str, str]:
        return load_data(loader=IconsLoader(), path=path)
