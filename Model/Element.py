from enum import Enum

class Element(Enum):
    EARTH = 1
    FIRE = 2
    AIR = 3
    WATER = 4

    @staticmethod
    def get_opposite():
        if Element.EARTH:
            return Element.AIR
        elif Element.FIRE:
            return Element.WATER
        elif Element.AIR:
            return Element.EARTH
        else:
            return Element.FIRE
