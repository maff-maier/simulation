import time
from actions import FillWorldAction, MakeMoveAction, RemoveEntitiesAction, ResetActionPointsAction, RespawnEntitiesAction
from core.acts.dying import Dying
from configs.entites_config import get_entities_config
from core.acts.moving import Moving
from core.path_finders.path_finder import BFS, AStar
from core.presentation.renderer import CliRenderer
from core.utils.states import GameStates
from core.world.world import World


if __name__ == '__main__':
    renderer = CliRenderer()
    world = World(height=10, width=10)

    configs = get_entities_config()
    FillWorldAction(entities_config=configs).perform(world=world)
    state = GameStates.RUNNING
    renderer.render(world=world, state=state)
    while True:
        time.sleep(1.5)
        
        MakeMoveAction(moving=Moving(path_finder=AStar(),
                    target_finder=BFS())).perform(world=world)
        
        RemoveEntitiesAction(dying=Dying()).perform(world=world)
        ResetActionPointsAction(configs=configs).perform(world=world)
        
        RespawnEntitiesAction(configs=configs).perform(world=world)
        
        renderer.render(world=world, state=state)        
