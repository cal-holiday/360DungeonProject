import unittest

from Model.CharacterFactory import CharacterFactory
from Model.Element import Element
from Model.Inventory import Inventory
from Model.Potion import HealthPotion, VisionPotion
from Model.Pillar import PolymorphismPillar, EncapsulationPillar, InheritancePillar, AbstractionPillar


class TestInventory(unittest.TestCase):
    CharacterFactory.create_hero("hero", Element.EARTH)
    Inventory()
    def setUp(self):
        # Initialize a new instance of Inventory for each test
        self.inventory = Inventory.get_instance()

    def test_singleton_instance(self):
        # Test to ensure Inventory class maintains only one instance
        inventory2 = Inventory.get_instance()
        self.assertEqual(self.inventory, inventory2)

        # Deleting the instance and creating a new one to test if singleton logic works
        Inventory.delete_instance()
        inventory3 = Inventory.get_instance()
        self.assertNotEqual(self.inventory, inventory3)

    def test_add_null_object(self):
        # Test to ensure ValueError is raised when adding a null object
        with self.assertRaises(ValueError):
            self.inventory.add(None)

    def test_add_pillar(self):
        # Test adding different types of pillars to the inventory
        abstraction_pillar = AbstractionPillar()
        polymorphism_pillar = PolymorphismPillar()
        inheritance_pillar = InheritancePillar()
        encapsulation_pillar = EncapsulationPillar()

        self.inventory.add(abstraction_pillar)
        self.inventory.add(polymorphism_pillar)
        self.inventory.add(inheritance_pillar)
        self.inventory.add(encapsulation_pillar)

        self.assertEqual(self.inventory.has_all_pillars(), True)
        self.assertEqual(len(self.inventory.get_pillars()), 4)

    def test_add_health_potion(self):
        # Test adding a health potion to the inventory
        health_potion = HealthPotion()
        self.inventory.add(health_potion)

        self.assertTrue(self.inventory.has_health_potion())
        self.assertEqual(self.inventory.number_of_health_potions(), 1)

    def test_add_vision_potion(self):
        # Test adding a vision potion to the inventory
        vision_potion = VisionPotion()
        self.inventory.add(vision_potion)

        self.assertTrue(self.inventory.has_vision_potion())
        self.assertEqual(len(self.inventory.get_vision_potions()), 1)

    def test_drink_health_potion(self):
        # Test drinking a health potion
        health_potion = HealthPotion()
        self.inventory.add(health_potion)
        self.inventory.drink_health_potion()

        self.assertFalse(self.inventory.has_health_potion())
        self.assertEqual(self.inventory.number_of_health_potions(), 0)

    def test_drink_vision_potion(self):
        # Test drinking a vision potion
        vision_potion = VisionPotion()
        self.inventory.add(vision_potion)
        self.inventory.drink_vision_potion()

        self.assertFalse(self.inventory.has_vision_potion())
        self.assertEqual(len(self.inventory.get_vision_potions()), 0)

