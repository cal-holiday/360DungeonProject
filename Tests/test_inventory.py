import unittest

from Model.Element import Element
from Model.Hero import Hero
from Model.Inventory import Inventory
from Model.Potion import HealthPotion, VisionPotion
from Model.Pillar import PolymorphismPillar, EncapsulationPillar, InheritancePillar, AbstractionPillar

class TestInventory(unittest.TestCase):
    def setUp(self):
        Hero("hero", "hero.png", "hero_hit.png", "hero_dead.png", 100, 10, Element.FIRE)
        Inventory.delete_instance()  # Ensure fresh singleton instance
        self.inventory = Inventory()
        self.health_potion = HealthPotion()
        self.vision_potion = VisionPotion()
        self.pillars = [
            PolymorphismPillar(),
            EncapsulationPillar(),
            InheritancePillar(),
            AbstractionPillar(),
        ]

    def tearDown(self):
        Inventory.delete_instance()  # Clean up singleton instance after tests
        Hero.delete_instance()
    def test_singleton_enforcement(self):
        with self.assertRaises(Exception) as context:
            Inventory()
        self.assertEqual(str(context.exception), "Inventory already exists!")

    def test_get_instance(self):
        self.assertEqual(Inventory.get_instance(), self.inventory)

    def test_delete_instance(self):
        Inventory.delete_instance()
        new_inventory = Inventory()
        self.assertNotEqual(self.inventory, new_inventory)

    def test_add_health_potion(self):
        self.inventory.add(self.health_potion)
        self.assertIn(self.health_potion, self.inventory.get_health_potions())

    def test_add_vision_potion(self):
        self.inventory.add(self.vision_potion)
        self.assertIn(self.vision_potion, self.inventory.get_vision_potions())

    def test_add_pillar(self):
        for pillar in self.pillars:
            self.inventory.add(pillar)
        self.assertEqual(self.inventory.get_pillars(), self.pillars)

    def test_add_invalid_object(self):
        with self.assertRaises(ValueError):
            self.inventory.add(None)

    def test_has_health_potion(self):
        self.assertFalse(self.inventory.has_health_potion())
        self.inventory.add(self.health_potion)
        self.assertTrue(self.inventory.has_health_potion())

    def test_has_vision_potion(self):
        self.assertFalse(self.inventory.has_vision_potion())
        self.inventory.add(self.vision_potion)
        self.assertTrue(self.inventory.has_vision_potion())

    def test_number_of_health_potions(self):
        self.assertEqual(self.inventory.number_of_health_potions(), 0)
        self.inventory.add(self.health_potion)
        self.assertEqual(self.inventory.number_of_health_potions(), 1)
        self.inventory.add(HealthPotion())
        self.assertEqual(self.inventory.number_of_health_potions(), 2)

    def test_drink_health_potion(self):
        self.inventory.add(self.health_potion)
        self.inventory.add(self.health_potion)
        self.assertEqual(self.inventory.number_of_health_potions(), 2)
        self.inventory.drink_health_potion()
        self.assertEqual(self.inventory.number_of_health_potions(), 1)

    def test_drink_health_potion_empty(self):
        self.assertFalse(self.inventory.has_health_potion())
        self.inventory.drink_health_potion()  # Should handle gracefully without throwing

    def test_drink_vision_potion(self):
        self.inventory.add(self.vision_potion)
        self.inventory.add(self.vision_potion)
        self.assertTrue(self.inventory.has_vision_potion())
        self.inventory.drink_vision_potion()
        self.assertEqual(len(self.inventory.get_vision_potions()), 1)

    def test_drink_vision_potion_empty(self):
        self.assertFalse(self.inventory.has_vision_potion())
        self.inventory.drink_vision_potion()  # Should handle gracefully without throwing

    def test_has_all_pillars(self):
        self.assertFalse(self.inventory.has_all_pillars())
        for pillar in self.pillars:
            self.inventory.add(pillar)
        self.assertTrue(self.inventory.has_all_pillars())

    def test_get_pillars(self):
        self.assertEqual(self.inventory.get_pillars(), [])
        self.inventory.add(self.pillars[0])
        self.assertEqual(self.inventory.get_pillars(), [self.pillars[0]])

    def test_get_health_potions(self):
        self.assertEqual(self.inventory.get_health_potions(), [])
        self.inventory.add(self.health_potion)
        self.assertEqual(self.inventory.get_health_potions(), [self.health_potion])

    def test_get_vision_potions(self):
        self.assertEqual(self.inventory.get_vision_potions(), [])
        self.inventory.add(self.vision_potion)
        self.assertEqual(self.inventory.get_vision_potions(), [self.vision_potion])

if __name__ == "__main__":
    unittest.main()
