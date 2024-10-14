from typing import NamedTuple, Type

from attributes import Attributes, GrassAttributes, HerbivoreAttributes, PredatorAttributes, RockAttributes, TreeAttributes
from factories import Factory, GrassFactory, HerbivoreFactory, PredatorFactory, RockFactory, TreeFactory


class Config(NamedTuple):
    entity_count_coeff: float
    spawn_coeff: float
    factory: Type[Factory]
    attributes: Type[Attributes]


def get_configs() -> list[Config]:
    return [
        Config(entity_count_coeff=0.10, spawn_coeff=0.10, factory=HerbivoreFactory, attributes=HerbivoreAttributes),
        Config(entity_count_coeff=0.08, spawn_coeff=0.07, factory=PredatorFactory, attributes=PredatorAttributes),
        Config(entity_count_coeff=0.12, spawn_coeff=0.12, factory=GrassFactory, attributes=GrassAttributes),
        Config(entity_count_coeff=0.05, spawn_coeff=0.01, factory=TreeFactory, attributes=TreeAttributes),
        Config(entity_count_coeff=0.05, spawn_coeff=0.01, factory=RockFactory, attributes=RockAttributes)
    ]
