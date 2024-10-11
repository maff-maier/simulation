import json

from typing import Iterable, Protocol


class Loader(Protocol):
    def load(self, path: str) -> Iterable:
        pass
    
class IconLoader(Loader):
    def load(self, path: str = 'icons.json') -> Iterable:
        with open(file=path, mode='r', encoding='utf-8') as file:
            return json.load(file)