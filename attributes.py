
from abc import ABC


class Attributes(ABC):
    hp = 0
    action_points = 0
    attack = 0


class HerbivoreAttributes(Attributes):
    hp = 10
    action_points = 2
    attack = 2


class PredatorAttributes(Attributes):
    hp = 15
    action_points = 3
    attack = 3


class GrassAttributes(Attributes):
    hp = 5


class TreeAttributes(Attributes):
    hp = 25


class RockAttributes(Attributes):
    hp = 50
