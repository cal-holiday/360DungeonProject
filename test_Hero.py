import unittest
from abc import ABC
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

class CharacterInterface(ABC):
    def __init__(self, name, image, health, element:Element):
        self.name = name
        self.image = image
        self.health = health
        self.element = element

class Hero(CharacterInterface):
    def __init__(self, name, image, health, element:Element):
        super().__init__(name, image, health, element)




class Test(unittest.TestCase):
    def test_constructor(self):
        hero = Hero("Silly lil guy", "guy.jpg", 10, Element.EARTH)
        self.assertEqual(hero.name, "Silly lil guy")
        """
        self.assertEqual(hero.get_image(), "guy.jpg")
        self.assertEqual(hero.get_max_hp(), 10)
        self.assertEqual(hero.get_agility(), 2)
        self.assertEqual(hero.get_element(), Element.EARTH)
        """


if __name__ == '__main__':
    unittest.main()
