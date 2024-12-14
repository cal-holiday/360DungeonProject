import unittest
from Model.Dungeon import Dungeon
from Model.Element import Element


class MyTestCase(unittest.TestCase):
    def test_dungeon_get_instance_none(self):
        self.assertEqual(Dungeon.get_instance(), None)
    def test_dungeon_get_instance_dungeon(self):
        Dungeon(False, ["name", Element.EARTH])
        self.assertIsNotNone(Dungeon.get_instance())