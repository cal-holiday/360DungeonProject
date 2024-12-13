import unittest

from Model.CharacterFactory import CharacterFactory
from Model.Element import Element
from Model.Potion import HealthPotion, VisionPotion
from Model.Monster import Monster  # Assuming there's a Monster class for testing purposes
from Model.Room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        # Create instances of dependencies for the Room
        self.monster = CharacterFactory.create_monster(Element.WATER)
        self.potion = HealthPotion()  # Using HealthPotion for simplicity
        self.location = (1,1)

        # Initialize a Room instance
        self.room = Room(True, True, True, True, self.location, self.potion, self.monster)

    def test_constructor(self):
        # Test the constructor initializes all attributes correctly
        self.assertTrue(self.room.get_nwall())
        self.assertTrue(self.room.get_swall())
        self.assertTrue(self.room.get_ewall())
        self.assertTrue(self.room.get_wwall())
        self.assertEqual(self.room.get_location(), (1,1))
        self.assertEqual(self.room.get_potion(), self.potion)
        self.assertEqual(self.room.get_monster(), self.monster)
        self.assertFalse(self.room.get_has_visited())
        self.assertFalse(self.room.get_hero_has_visited())
        self.assertFalse(self.room.get_has_exit())

    def test_set_nwall(self):
        self.room.set_nwall(False)
        self.assertFalse(self.room.get_nwall())

        with self.assertRaises(ValueError):
            self.room.set_nwall(None)

    def test_set_swall(self):
        self.room.set_swall(False)
        self.assertFalse(self.room.get_swall())

        with self.assertRaises(ValueError):
            self.room.set_swall(None)

    def test_set_ewall(self):
        self.room.set_ewall(False)
        self.assertFalse(self.room.get_ewall())

        with self.assertRaises(ValueError):
            self.room.set_ewall(None)

    def test_set_wwall(self):
        self.room.set_wwall(False)
        self.assertFalse(self.room.get_wwall())

        with self.assertRaises(ValueError):
            self.room.set_wwall(None)

    def test_set_monster(self):
        new_monster = Monster("New Monster", 60, 15)
        self.room.set_monster(new_monster)
        self.assertEqual(self.room.get_monster(), new_monster)

    def test_set_potion(self):
        new_potion = VisionPotion()
        self.room.set_potion(new_potion)
        self.assertEqual(self.room.get_potion(), new_potion)

    def test_set_location(self):
        self.room.set_location("New Location")
        self.assertEqual(self.room.get_location(), "New Location")

        with self.assertRaises(ValueError):
            self.room.set_location(None)

    def test_set_has_visited(self):
        self.room.set_has_visited(True)
        self.assertTrue(self.room.get_has_visited())

        self.room.set_has_visited(False)
        self.assertFalse(self.room.get_has_visited())

        with self.assertRaises(ValueError):
            self.room.set_has_visited(None)

    def test_set_hero_has_visited(self):
        self.room.set_hero_has_visited(True)
        self.assertTrue(self.room.get_hero_has_visited())

        self.room.set_hero_has_visited(False)
        self.assertFalse(self.room.get_hero_has_visited())

        with self.assertRaises(ValueError):
            self.room.set_hero_has_visited(None)

    def test_set_has_exit(self):
        self.room.set_has_exit(True)
        self.assertTrue(self.room.get_has_exit())

        self.room.set_has_exit(False)
        self.assertFalse(self.room.get_has_exit())

        with self.assertRaises(ValueError):
            self.room.set_has_exit(None)

