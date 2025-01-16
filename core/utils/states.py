from enum import Enum
    

class InitOptions(Enum):
    START: int = 1
    END: int = 2
    

class RunningOptions(Enum):
    PAUSE: int = 1
    RESET: int = 2
    END: int = 3
    

class PausedOptions(Enum):
    RESUME: int = 1
    RESET: int = 2
    END: int = 3


class GameStates(Enum):
    RUNNING = 1
    PAUSED = 2