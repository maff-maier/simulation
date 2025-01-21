from typing import NamedTuple, Type

from configs.attributes import Attributes, GrassAttributes, HerbivoreAttributes, PredatorAttributes, RockAttributes, TreeAttributes
from core.entities.entities import Entity, Grass, Herbivore, Predator, Rock, Tree
from core.entities.factories import Factory, GrassFactory, HerbivoreFactory, PredatorFactory, RockFactory, TreeFactory


class EntityConfig(NamedTuple):
    spawn_coeff: int
    respawn_coeff: int
    factory: Type[Factory]
    attributes: Type[Attributes]


def get_entities_config() -> dict[Entity, EntityConfig]:
    return {
        Herbivore: EntityConfig(spawn_coeff=0.07, respawn_coeff=0.18, factory=HerbivoreFactory, attributes=HerbivoreAttributes),
        Predator: EntityConfig(spawn_coeff=0.05, respawn_coeff=0.2, factory=PredatorFactory, attributes=PredatorAttributes),
        Grass: EntityConfig(spawn_coeff=0.09, respawn_coeff=0.23, factory=GrassFactory, attributes=GrassAttributes),
        Tree: EntityConfig(spawn_coeff=0.02, respawn_coeff=0.008, factory=TreeFactory, attributes=TreeAttributes),
        Rock: EntityConfig(spawn_coeff=0.01, respawn_coeff=0.008, factory=RockFactory, attributes=RockAttributes),
    }
