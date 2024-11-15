import unittest
from Monster import Monster
from Element import Element



class MyTestCase(unittest.TestCase):
    monster = Monster("Gross", "image", 12, 12, Element.EARTH)

    def test_monsterconstructor(self):
        monster = Monster("Gross", "image", 12, 10, Element.EARTH)
        self.assertEqual(monster.get_hp(),12) #tests hp
        self.assertEqual(monster.get_image(), "image") #tests image
        self.assertEqual(monster.get_max_hp(), 12) #tests max hp
        self.assertEqual(monster.get_agility(), 10) #tests aglility
        self.assertEqual(monster.get_element(), Element.EARTH) #tests element

    def test_heal(self):

    #def test_specialattack(self):

    #def test_attack(self):


if __name__ == '__main__':
    unittest.main()
