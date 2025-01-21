from threading import Event, Thread
from time import sleep

from core.presentation.renderer import Renderer
from core.utils.states import GameCommands
from core.simulaiton.simulation import Simulation
from configs.simulation_config import SimulationConfig


class Manager:
    def __init__(self, simulation_config: SimulationConfig, renderer: Renderer) -> None:
        self._simulation = Simulation(config=simulation_config)
        self._renderer = renderer

    def run(self) -> None:
        run_event = Event()
        stop_event = Event()

        subthread = Thread(target=self._run_simulation,
                           args=(run_event, stop_event), daemon=True)

        subthread.start()

        run_event.set()
        self._run_menu(run_event=run_event,
                       stop_event=stop_event)

    def _run_menu(self, run_event: Event, stop_event: Event) -> None:
        while True:
            command = input().strip().lower()
            if not command.isdigit():
                continue

            match int(command):
                case GameCommands.PAUSE:
                    run_event.clear()
                    self._renderer.render_on_pause()
                case GameCommands.RESUME:
                    run_event.set()
                case GameCommands.STOP:
                    stop_event.set()
                    break
                case _:
                    continue

    def _run_simulation(self, run_event: Event, stop_event: Event) -> None:
        self._simulation.start()

        while not (stop_event.is_set() or self._simulation.world.is_full_map()):
            if run_event.is_set():
                self._renderer.render(
                    world=self._simulation.world)

                self._simulation.turn()
                sleep(1)
