from configs.simulation_config import SimulationConfig


class Simulation:
    def __init__(self, config: SimulationConfig) -> None:
        self.world = config.world
        self.init_actions = config.init_actions
        self.turn_actions = config.turn_actions

    def start(self) -> None:
        for action in self.init_actions:
            action.perform(world=self.world)

    def turn(self) -> None:
        for action in self.turn_actions:
            action.perform(world=self.world)
