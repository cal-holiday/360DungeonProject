import unittest
from Element import Element
from Hero import Hero


class HeroTest(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("lil man", "image", 100, 2, Element.EARTH)
    def test_constructor(self):
        self.assertEqual(self.hero.get_name(), "lil man")
        self.assertEqual(self.hero.get_image(), "image")
        self.assertEqual(self.hero.get_max_hp(), 100)
        self.assertEqual(self.hero.get_agility(), 2)
        self.assertEqual(self.hero.get_element(), Element.EARTH)
        self.assertEqual(self.hero.get_hp(), 100)

    def test_get_opposite(self):
        self.assertEqual(self.hero.get_opposite_element(), Element.AIR)


if __name__ == '__main__':
    unittest.main()
