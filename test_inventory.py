import unittest
from Inventory import Inventory

class MyTestCase(unittest.TestCase):
    def test_inventory_constructor(self):
        inventory = Inventory()
        self.assertEqual(inventory.health_potions, [])
        self.assertEqual(inventory.vision_potions,[])
        self.assertEqual(inventory.pillars,[])
        self.assertEqual(inventory.has_all_pillars,False)

    def test_inventory_add_health_potion(self):
    def test_inventory_add_stealth_potion(self):
    def test_inventory_add_potion(self):

    def test_drink_health_potion(self):
    def test_drink_

if __name__ == '__main__':
    unittest.main()
