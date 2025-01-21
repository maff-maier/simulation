from enum import IntEnum


class InitOptions(IntEnum):
    START: int = 1
    END: int = 2


class RunningOptions(IntEnum):
    PAUSE: int = 1
    RESET: int = 2
    END: int = 3


class PausedOptions(IntEnum):
    RESUME: int = 1
    RESET: int = 2
    END: int = 3


class GameCommands(IntEnum):
    PAUSE = 1
    RESUME = 2
    STOP = 3
