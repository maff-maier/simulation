from core.entities.entities import Entity
from core.world.world import World


class Dying:
    def act(self, world: World, entity: Entity) -> None:
        world.remove_entity(entity=entity)
