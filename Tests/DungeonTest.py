import unittest

from Controller.SaveLoad import SaveLoad
from Model.Dungeon import Dungeon
from Model.Element import Element
from Model.Hero import Hero
from Model.Inventory import Inventory


class MyTestCase(unittest.TestCase):
    def test_dungeon_get_instance_none(self):
        self.assertIsNone(Dungeon.get_instance())
    def test_dungeon_get_instance_dungeon(self):
        Dungeon(False, ["name", Element.EARTH])
        self.assertIsNotNone(Dungeon.get_instance())
        self.assertIsNotNone(Inventory.get_instance())
        self.assertEqual(Hero.get_instance().get_name(), "name")
        self.assertEqual(Hero.get_instance().get_element(), Element.EARTH)
        Dungeon.delete_instance()
    def test_dungeon_delete_instance(self):
        Dungeon(False, ["name", Element.EARTH])
        Dungeon.delete_instance()
        self.assertIsNone(Dungeon.get_instance())
        self.assertIsNone(Hero.get_instance())
        self.assertIsNone(Inventory.get_instance())
    def test_dungeon_constructor_hold_the_pickles(self):
        Dungeon(False, ["name", Element.EARTH])
        self.assertIsNotNone(Dungeon.get_instance())
        self.assertIsNotNone(Inventory.get_instance())
        self.assertEqual(Hero.get_instance().get_name(), "name")
        self.assertEqual(Hero.get_instance().get_element(), Element.EARTH)
        self.assertEqual(Hero.get_instance().get_x(), -100)
        self.assertEqual(Hero.get_instance().get_y(), -100)
        Dungeon.delete_instance()

    def test_dungeon_constructor_extra_pickles(self):
        Dungeon(False, ["name", Element.EARTH])
        SaveLoad.save_game(Dungeon.pickle_dungeon(), "test")
        Dungeon.delete_instance()
        pickle_info = SaveLoad.load_game("test")
        Dungeon(True, pickle_info[0], pickle_info[1], pickle_info[2])
        self.assertIsNotNone(Dungeon.get_instance())
        self.assertIsNotNone(Inventory.get_instance())
        self.assertEqual(Hero.get_instance().get_name(), "name")
        self.assertEqual(Hero.get_instance().get_element(), Element.EARTH)
        self.assertEqual(Hero.get_instance().get_x(), -100)
        self.assertEqual(Hero.get_instance().get_y(), -100)
        Dungeon.delete_instance()