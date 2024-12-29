from entities import Entity
from world import World


class Dying:
    def act(self, world: World, entity: Entity) -> None:
        world.remove_entity(entity=entity)
