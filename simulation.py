from actions import Action
from core.world.world import World


class Simulation:
    def __init__(self, world: World, init_actions: list[Action], turn_actions: list[Action]) -> None:
        self._world = world
        self._init_actions = init_actions
        self._turn_actions = turn_actions
        
    def start(self) -> None:
        for action in self._init_actions:
            action.perform(world=self._world)

    def turn(self) -> None:
        for action in self._turn_actions:
            action.perform(world=self._world)
    