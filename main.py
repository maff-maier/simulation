from core.presentation.renderer import CliRenderer
from configs.simulation_config import get_default_sim_config
from manager import Manager
    


if __name__ == '__main__':
    manager = Manager(simulation_config=get_default_sim_config(), renderer=CliRenderer())
    manager.run()
