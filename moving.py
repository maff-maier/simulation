from coordinates import Coordinates
from entities import Creature
from path_finder import BFS, PathFinder
from world import World


class Moving:
    def __init__(self, path_finder: PathFinder, target_finder: BFS) -> None:
        self.path_finder = path_finder
        self.target_finder = target_finder

    def act(self, world: World, creature: Creature) -> None:
        target_coords = self.target_finder.find_target(
            world=world, base_creature=creature)

        if not target_coords:
            return

        base_coords = world.get_coordinates(target_entity=creature)

        pathes: list[tuple[int, list[Coordinates]]] = find_reachable_pathes(world=world, path_finder=self.path_finder,
                                                                            base_coords=base_coords, target_coords=target_coords)

        if pathes is None:
            return

        path = pathes[0][1]

        if not (path_len := len(path)):
            return

        coords_index = (
            creature.action_points
            if creature.action_points <= path_len
            else path_len
        )

        self._move(world=world, creature=creature, coords=path[coords_index-1])

        creature.action_points -= coords_index

    def _move(self, world: World, creature: Creature, coords: Coordinates) -> None:
        if creature not in world.get_all_entities():
            return

        world.update_coordinates(entity=creature, new_coords=coords)


def find_reachable_pathes(world: World, path_finder: PathFinder, base_coords: Coordinates, target_coords: Coordinates) -> list[Coordinates]:
    pathes = []
    adjacents = world.get_adjacent_coordinates(coords=target_coords)
    reachable_adjacents = world.get_empty_adjacent_coordinates(
        adjacents=adjacents)

    if base_coords in adjacents:
        reachable_adjacents.append(base_coords)

    for adjacent in reachable_adjacents:
        path = path_finder.find(
            world=world, base_coords=base_coords, target_coords=adjacent)

        if path is not None:
            pathes.append((len(path), path))

    return sorted(pathes, key=lambda x: x[0])
