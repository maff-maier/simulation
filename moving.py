from math import ceil

from coordinates import Coordinates
from eating import Eating
from entities import Creature
from path_finder import BFS, PathFinder
from world import World


class Moving:
    def __init__(self, path_finder: PathFinder, target_finder: BFS) -> None:
        self.path_finder = path_finder
        self.target_finder = target_finder

    def act(self, world: World, creature: Creature) -> None:
        while creature.action_points:
            target_coords = self.target_finder.find_target(
                world=world, base_creature=creature)

            if not target_coords:
                return

            target_entity = world.get_entity(coords=target_coords)

            base_coords = world.get_coordinates(target_entity=creature)

            pathes: list[tuple[int, list[Coordinates]]] = find_reachable_pathes(world=world, path_finder=self.path_finder,
                                                                                base_coords=base_coords, target_coords=target_coords)

            if not pathes:
                return

            path = pathes[0][1]
            is_near = not bool(path_len := len(path))

            if is_near:
                points_to_kill = ceil(target_entity.hp/creature.damage)
                action_counts = min(points_to_kill, creature.action_points)

                creature.action_points -= action_counts

                while action_counts:
                    Eating().act(creature=creature, target=target_entity)
                    action_counts -= 1
            else:
                coords_index = min(creature.action_points, path_len)

                self._move(world=world, creature=creature,
                           coords=path[coords_index-1])

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

    if not len(reachable_adjacents):
        return None

    for adjacent in reachable_adjacents:
        path = path_finder.find(
            world=world, base_coords=base_coords, target_coords=adjacent)

        if path is not None:
            pathes.append((len(path), path))

    return sorted(pathes, key=lambda x: x[0])
