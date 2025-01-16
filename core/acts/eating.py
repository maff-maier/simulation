from core.entities.entities import Creature, Entity


class Eating:
    def act(self, creature: Creature, target: Entity) -> None:
        creature.bite(target=target)
