from unittest import TestCase

from Hero import Hero
from Pillar import AbstractionPillar, PolymorphismPillar, InheritancePillar, EncapsulationPillar
from Element import Element

class TestPillar(TestCase):
    hero = Hero("lil man", "image", 100, 2, Element.EARTH)
    pillar = AbstractionPillar("image", hero)
    def test_constructor(self):
        self.abstraction_pillar = AbstractionPillar("image", self.hero)
        self.polymorphism_pillar = PolymorphismPillar("image", self.hero)
        self.inheritance_pillar = InheritancePillar("image", self.hero)
        self.encapsulation_pillar = EncapsulationPillar("image", self.hero)

    def test_set_image(self):
        with self.assertRaises(ValueError):
            AbstractionPillar(None, self.hero)

    def test_set_hero(self):
        with self.assertRaises(ValueError):
            AbstractionPillar( "image", None)

    def test_get_name(self):
        self.assertEqual(self.pillar.get_name(), "abstraction")

    def test_get_image(self):
        self.assertEqual(self.pillar.get_image(), "image")

    def test_get_hero(self):
        self.assertIsInstance(self.pillar.get_hero(),Hero)

    def test_restore_health(self):
        self.hero.set_hp(20)
        self.pillar.restore_health()
        self.assertEqual(self.hero.get_hp(), 100)

    def test_Abstraction_enhance(self):
        original_damage_mod = self.pillar.hero.get_damage_mod()
        self.pillar.enhance(
        self.assertEqual(self.pillar.hero.get_damage_mod(), original_damage_mod + 5)


