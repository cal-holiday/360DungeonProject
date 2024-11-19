import unittest

from Element import Element
from Hero import Hero
from Inventory import Inventory

from Pillar import Pillar, PolymorphismPillar, AbstractionPillar, InheritancePillar, EncapsulationPillar
from Potion import HealthPotion, VisionPotion


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("name", "image", 100, 2, Element.EARTH)
        self.inventory = Inventory()
        self.abstraction_pillar = AbstractionPillar("image", self.hero)
        self.polymorphism_pillar = PolymorphismPillar("image", self.hero)
        self.inheritance_pillar = InheritancePillar("image", self.hero)
        self.encapsulation_pillar = EncapsulationPillar("image", self.hero)
        self.health_potion = HealthPotion("image", self.hero)
        self.vision_potion = VisionPotion("image", self.hero)

    def test_inventory_constructor(self):
        self.assertEqual(self.inventory.health_potions, [])
        self.assertEqual(self.inventory.vision_potions,[])
        self.assertEqual(self.inventory.pillars,[])

    def test_add_pillar(self):
        original_hp = self.hero.get_max_hp()
        self.inventory.add(self.polymorphism_pillar)
        self.assertEqual(self.hero.get_max_hp(), original_hp + 10)
        self.assertEqual(len(self.inventory.pillars), 1)

    def test_add_potions(self):
        self.inventory.add(self.health_potion)
        self.assertEqual(len(self.inventory.health_potions), 1)

        self.inventory.add(self.vision_potion)
        self.assertEqual(len(self.inventory.vision_potions), 1)

    def test_drink_potions(self):
        self.inventory.add(self.health_potion)
        self.inventory.drink_potion(self.health_potion)
        self.assertEqual(len(self.inventory.health_potions), 0)

        self.inventory.add(self.vision_potion)
        self.inventory.drink_potion(self.vision_potion)
        self.assertEqual(len(self.inventory.vision_potions), 0)

    def test_has_all_pillars(self):
        self.inventory.add(self.abstraction_pillar)
        self.inventory.add(self.polymorphism_pillar)
        self.assertEqual(self.inventory.has_all_pillars(), False)

        self.inventory.add(self.inheritance_pillar)
        self.inventory.add(self.encapsulation_pillar)
        self.assertEqual(self.inventory.has_all_pillars(), True)

if __name__ == '__main__':
    unittest.main()
