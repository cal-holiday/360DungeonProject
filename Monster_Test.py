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

    def test_heal_if_not_at_full_health(self): #tests if the heal method is true that it updates health
        monster = Monster("Gross", "image", 12, 10, Element.EARTH)
        monster.set_hp(5)
        if monster.heal():
            self.assertEqual(monster.get_hp(),10)
        else:
            self.assertEqual(monster.get_hp(),5)

    def test_heal_if_at_full_health(self):
        monster = Monster("Gross", "image", 12, 10, Element.EARTH)
        self.assertEqual(monster.heal(),False)


if __name__ == '__main__':
    unittest.main()
