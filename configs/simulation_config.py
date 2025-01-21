from typing import NamedTuple

from core.simulaiton.actions import Action, FillWorldAction, MakeMoveAction, RemoveEntitiesAction, ResetActionPointsAction, RespawnEntitiesAction
from configs.entites_config import get_entities_config
from core.acts.dying import Dying
from core.acts.moving import Moving
from core.path_finders.path_finder import BFS, AStar
from core.world.world import World


class SimulationConfig(NamedTuple):
    world: World
    init_actions: list[Action]
    turn_actions: list[Action]


def get_default_sim_config() -> SimulationConfig:
    world = World(height=3, width=3)
    config = get_entities_config()

    init_actions = [FillWorldAction(entities_config=config)]
    turn_actions = [
        MakeMoveAction(moving=Moving(
            path_finder=AStar(), target_finder=BFS())),
        RemoveEntitiesAction(dying=Dying()),
        ResetActionPointsAction(configs=config),
        RespawnEntitiesAction(configs=config)
    ]

    return SimulationConfig(world=world, init_actions=init_actions, turn_actions=turn_actions)
