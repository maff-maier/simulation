import json
from abc import ABC, abstractmethod
from typing import Any, Iterable, Protocol


class Loader(Protocol):
    def load(self, path: str) -> Iterable:
        pass


class JsonLoader(Loader):
    def load(self, path: str) -> Iterable:
        with open(file=path, mode='r', encoding='utf-8') as file:
            return json.load(fp=file)


class ConfigLoader(JsonLoader):
    def load(self, path: str = 'config.json') -> Iterable:
        return super().load(path)


class IconsLoader(JsonLoader):
    def load(self, path: str = 'icons.json') -> Iterable:
        return super().load(path)


def load_data(loader: Loader, path: str) -> Iterable:
    return loader.load(path=path)
