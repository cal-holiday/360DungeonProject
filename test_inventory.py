import unittest

from Element import Element
from Hero import Hero
from Inventory import Inventory
from Pillar import Pillar, PolymorphismPillar, AbstractionPillar, InheritancePillar, EncapsulationPillar
from Potion import HealthPotion, VisionPotion


class MyTestCase(unittest.TestCase):
    def setUp(self):
        hero = Hero("lil man", "image", 100, 2, Element.EARTH)
        self.inventory = Inventory()
        self.health_potion = HealthPotion("image", hero)
        self.vision_potion = VisionPotion("image", hero)
        self.abstraction_pillar = AbstractionPillar("image", hero)
        self.polymorphism_pillar = PolymorphismPillar("image", hero)
        self.inheritance_pillar = InheritancePillar("image", hero)
        self.encapsulation_pillar = EncapsulationPillar("image", hero)
    def test_inventory_constructor(self):
        self.assertEqual(self.inventory.health_potions, [])
        self.assertEqual(self.inventory.vision_potions,[])
        self.assertEqual(self.inventory.pillars,[])
        self.assertEqual(self.inventory.has_all_pillars(),False)

    #def test_inventory_add_health_potion(self):
    #def test_inventory_add_vision_potion(self):
    #def test_inventory_add_potion(self):
    #def test_drink_health_potion(self):
    #def test_drink_vision_potion(self):

    def test_add(self):
        self.inventory.add(self.abstraction_pillar)
        self.assertEqual(len(self.inventory.pillars), 1)

        self.inventory.add(self.health_potion)
        self.assertEqual(len(self.inventory.health_potions), 1)

        self.inventory.add(self.vision_potion)
        self.assertEqual(len(self.inventory.vision_potions), 1)

    def test_has_all_pillars_with_two_pillars(self):
        pillar = PolymorphismPillar("image","hero")
        self.inventory.add(pillar)
        self.inventory.add(pillar)
        self.assertEqual(self.inventory.has_all_pillars(),False)

    def test_all_pillars_with_all_pillars(self):
        pillar = PolymorphismPillar("image", "hero")
        self.inventory.add(pillar)
        self.inventory.add(pillar)
        self.inventory.add(pillar)
        self.inventory.add(pillar)
        print(len(self.inventory.pillars))
        self.assertEqual(self.inventory.has_all_pillars(), True)

if __name__ == '__main__':
    unittest.main()