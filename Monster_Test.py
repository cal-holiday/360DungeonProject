import unittest
from Monster import Monster
from Element import Element



class MyTestCase(unittest.TestCase):

    def test_something(self):
        monster = Monster("Gross","image",12,12,Element.EARTH)

        self.assertEqual(monster.get_hp(),12)  # add assertion here


if __name__ == '__main__':
    unittest.main()
