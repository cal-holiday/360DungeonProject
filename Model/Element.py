from enum import Enum

class Element(Enum):
    EARTH = 1
    FIRE = 2
    AIR = 3
    WATER = 4

    def get_opposite(self):
        return opposites[self]
opposites = {
             Element.EARTH: Element.AIR,
             Element.FIRE: Element.WATER,
             Element.AIR: Element.EARTH,
             Element.WATER:Element.FIRE
            }