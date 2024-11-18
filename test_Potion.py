from unittest import TestCase

from Element import Element
from Hero import Hero
from Potion import HealthPotion, VisionPotion


class TestPotion(TestCase):

    def setUp(self):
        self.hero = Hero("lil man", "image", 100, 2, Element.EARTH)
        self.health_potion = HealthPotion("image", self.hero)
        self.vision_potion = VisionPotion("image", self.hero)

    def test_set_image(self):
        with self.assertRaises(ValueError):
            HealthPotion(None, self.hero)

    def test_set_hero(self):
        with self.assertRaises(ValueError):
            VisionPotion("image", None)

    def test_get_name(self):
        self.assertEqual(self.health_potion.get_name(), "health")
        self.assertEqual(self.vision_potion.get_name(), "vision")

    def test_get_image(self):
        self.assertEqual(self.health_potion.get_image(), "image")
        self.assertEqual(self.vision_potion.get_image(), "image")

    def test_health_potion(self):
        self.health_potion.drink()
        self.assertEqual(self.health_potion.hero.get_hp(), self.health_potion.hero.get_max_hp())

        self.health_potion.hero.set_hp(80)
        original_health = self.health_potion.hero.get_hp()
        self.health_potion.drink()
        self.assertEqual(self.health_potion.hero.get_hp(), original_health + 10)

        self.health_potion.hero.set_hp(95)
        self.health_potion.drink()
        self.assertEqual(self.health_potion.hero.get_hp(), self.health_potion.hero.get_max_hp())

    def test_vision_potion(self):
        self.vision_potion.drink()
        self.assertEqual(self.vision_potion.hero.drank_vision_potion, True)




