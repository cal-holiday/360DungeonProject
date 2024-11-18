import unittest
from Inventory import Inventory
from Pillar import Pillar, PolymorphismPillar


class MyTestCase(unittest.TestCase):
    def test_inventory_constructor(self):
        inventory = Inventory()
        self.assertEqual(inventory.health_potions, [])
        self.assertEqual(inventory.vision_potions,[])
        self.assertEqual(inventory.pillars,[])
        self.assertEqual(inventory.has_all_pillars(),False)

    #def test_inventory_add_health_potion(self):
    #def test_inventory_add_vision_potion(self):
    #def test_inventory_add_potion(self):
    #def test_drink_health_potion(self):
    #def test_drink_vision_potion(self):
    def test_has_all_pillars_with_two_pillars(self):
        inventory = Inventory()
        pillar = PolymorphismPillar("image","hero")
        inventory.add(pillar)
        inventory.add(pillar)
        self.assertEqual(inventory.has_all_pillars(),False)

    def test_all_pillars_with_all_pillars(self):
        inventory = Inventory()
        pillar = PolymorphismPillar("image", "hero")
        inventory.add(pillar)
        inventory.add(pillar)
        inventory.add(pillar)
        inventory.add(pillar)
        print(len(inventory.pillars))
        self.assertEqual(inventory.has_all_pillars(), True)

if __name__ == '__main__':
    unittest.main()