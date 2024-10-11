from typing import Any


class NonNegativeValue:
    def __init__(self, name: str) -> None:
        self._name = name

    def __get__(self, instance: Any, owner: Any) -> Any:
        if not instance:
            return None
        return instance.__dir__[self._name]

    def __set__(self, instance: Any, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f'Value should be an integer.')

        if value < 0:
            raise ValueError(f'{self._name.capitalize()} cannot be negative.')

        instance.__dir__[self._name] = value