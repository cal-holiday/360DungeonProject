import unittest

from Element import Element
from Hero import Hero


class HeroTest(unittest.TestCase):
    def test_construcotr(self):
        hero = Hero("lil man", "image", 100, 2, Element.EARTH)
        self.assertEqual(hero.get_name(), "lil man")


if __name__ == '__main__':
    unittest.main()
