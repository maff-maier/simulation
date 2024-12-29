from collections import deque
import heapq
from typing import Protocol

from coordinates import Coordinates
from entities import Creature
from world import World


class ManhattanHeuristicEvaluation:
    def calculate(self, base_coords: Coordinates, target_coords: Coordinates) -> int:
        return abs((base_coords.height - target_coords.height) + (base_coords.width - target_coords.width))


class PathFinder(Protocol):
    def find(self, world: World, base_coords: Coordinates, target_coords: Coordinates) -> list[Coordinates]:
        pass


class BFS:
    def find_target(self, world: World, base_creature: Creature):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        target_type = base_creature.target_type

        start_coords = world.get_coordinates(target_entity=base_creature)
        if not start_coords:
            return None

        to_visit = deque([start_coords])
        visited = {start_coords}
        all_coords = world.get_all_coordinates()

        while to_visit:
            current_coords = to_visit.popleft()

            entity = world.get_entity(coords=current_coords)
            if entity and isinstance(entity, target_type) and entity.hp:
                return current_coords

            for direction in directions:
                height = current_coords.height + direction[0]
                width = current_coords.width + direction[1]

                if not world.is_within_bounds(height=height, width=width):
                    continue

                adjacent_coords = Coordinates(height=height, width=width)
                adjacent_entity = world.get_entity(coords=adjacent_coords)

                if adjacent_coords not in visited and (adjacent_coords not in all_coords or isinstance(adjacent_entity, target_type)):
                    to_visit.append(adjacent_coords)
                    visited.add(adjacent_coords)


class AStar(PathFinder):
    def find(self, world: World, base_coords: Coordinates, target_coords: Coordinates) -> list[Coordinates]:
        visited = set()
        not_visited = []
        heuristic = ManhattanHeuristicEvaluation()

        heapq.heappush(not_visited, (0, base_coords))

        came_from = {}

        g_score = {base_coords: 0}
        f_score = {base_coords: heuristic.calculate(
            base_coords=base_coords, target_coords=target_coords)}

        while not_visited:
            current_coords = heapq.heappop(not_visited)[1]

            if current_coords == target_coords:
                return reconstruct_path(came_from=came_from, current_coords=current_coords)

            visited.add(current_coords)

            adjacents_coords = world.get_adjacent_coordinates(
                coords=current_coords)
            for adjacent_coords in world.get_empty_adjacent_coordinates(adjacents=adjacents_coords):
                if adjacent_coords in visited:
                    continue

                tentative_g_score = g_score[current_coords] + 1

                if adjacent_coords not in g_score or tentative_g_score < g_score[adjacent_coords]:
                    came_from[adjacent_coords] = current_coords
                    g_score[adjacent_coords] = tentative_g_score
                    f_score[adjacent_coords] = (tentative_g_score + heuristic.calculate(
                        base_coords=adjacent_coords, target_coords=target_coords))

                    if all(adjacent_coords != item[1] for item in not_visited):
                        heapq.heappush(
                            not_visited, (f_score[adjacent_coords], adjacent_coords))


def reconstruct_path(came_from: dict[Coordinates, Coordinates], current_coords: Coordinates) -> list[Coordinates]:
    path = []

    while current_coords in came_from:
        path.append(current_coords)
        current_coords = came_from[current_coords]

    return path[::-1]
