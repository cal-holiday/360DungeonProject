from unittest import TestCase
from Model.Element import Element
from Model.Hero import Hero
from Model.Potion import HealthPotion, VisionPotion


class TestPotion(TestCase):

    def setUp(self):
        self.hero = Hero("lil man", "image", 100, 2, Element.EARTH)
        self.health_potion = HealthPotion()
        self.vision_potion = VisionPotion()

    def test_get_name(self):
        self.assertEqual(self.health_potion.get_name(), "health")
        self.assertEqual(self.vision_potion.get_name(), "vision")

    def test_get_image(self):
        self.assertEqual(self.health_potion.get_image(), "health_potion.png")
        self.assertEqual(self.vision_potion.get_image(), "vision_potion.png")

    def test_health_potion(self):
        self.health_potion.drink()
        self.assertEqual(self.hero.get_hp(), self.hero.get_max_hp())

        self.hero.set_hp(80)
        original_health = self.hero.get_hp()
        self.health_potion.drink()
        self.assertEqual(self.hero.get_hp(), original_health + 10)

        self.hero.set_hp(95)
        self.health_potion.drink()
        self.assertEqual(self.hero.get_hp(), self.hero.get_max_hp())

    def test_vision_potion(self):
        self.vision_potion.drink()
        self.assertEqual(self.hero.drank_vision_potion, True)




