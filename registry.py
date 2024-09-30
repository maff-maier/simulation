from factories import EntityFactory


class FactoryRegisty:
    def __init__(self) -> None:
        self._factories = dict()
        
    def register_factory(self, entity_name: str, factory: EntityFactory) -> None:
        self._factories[entity_name] = factory
        
    def get_factory(self, entity_name: str) -> EntityFactory:
        factory = self._factories.get(entity_name, None)
        
        if factory is None:
            raise ValueError(f'Factory for {entity_name} not found.')
        
        return factory