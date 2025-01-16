from typing import Any


class NonNegativeValue:
    def __init__(self, name: str) -> None:
        self._name = name
        
    def __get__(self, instance: Any, owner: Any) -> Any:
        if not instance:
            return None
        return instance.__dict__[self._name]
    
    def __set__(self, instance: Any, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError('Value should be an \'int\' type')
        
        if value < 0:
            raise ValueError('Value should be non-negative')
        
        instance.__dict__[self._name] = value
