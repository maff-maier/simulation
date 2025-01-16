from abc import ABC


class Attributes(ABC):
    hp: int = 0
    action_points: int = 0
    damage: int = 0
    satiety: int = 0


class HerbivoreAttributes(Attributes):
    hp: int = 12
    action_points: int = 2
    damage: int = 2
    satiety: int = 3


class PredatorAttributes(Attributes):
    hp: int = 10
    action_points: int = 3
    damage: int = 3
    satiety: int = 2


class GrassAttributes(Attributes):
    hp: int = 5


class RockAttributes(Attributes):
    hp: int = 50


class TreeAttributes(Attributes):
    hp: int = 25
