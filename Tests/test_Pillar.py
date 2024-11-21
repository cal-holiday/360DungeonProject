from unittest import TestCase

from Model.Hero import Hero
from Model.Pillar import AbstractionPillar, PolymorphismPillar, InheritancePillar, EncapsulationPillar
from Element import Element

class TestPillar(TestCase):
    def setUp(self):
        self.hero = Hero("lil man", "image", 100, 2, Element.EARTH)
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
        self.assertEqual(self.abstraction_pillar.get_name(), "abstraction")

    def test_get_image(self):
        self.assertEqual(self.abstraction_pillar.get_image(), "image")

    def test_get_hero(self):
        self.assertIsInstance(self.abstraction_pillar.get_hero(),Hero)

    def test_restore_health(self):
        self.hero.set_hp(20)
        self.abstraction_pillar.restore_health()
        self.assertEqual(self.hero.get_hp(), 100)

    def test_Abstraction_pillar(self):
        original_damage_mod = self.abstraction_pillar.hero.get_damage_mod()
        self.abstraction_pillar.enhance()
        self.assertEqual(self.abstraction_pillar.hero.get_damage_mod(), original_damage_mod + 5)

    def test_Polymorphism_pillar(self):
        original_max_hp = self.polymorphism_pillar.hero.get_max_hp()
        self.polymorphism_pillar.enhance()
        self.assertEqual(self.polymorphism_pillar.hero.get_max_hp(), original_max_hp + 10)

    def test_Inheritance_pillar(self):
        original_attack_mod = self.inheritance_pillar.hero.get_damage_mod()
        self.inheritance_pillar.enhance()
        self.assertEqual(self.inheritance_pillar.hero.get_attack_mod(), original_attack_mod + 2)

    def test_Encapsulation_pillar(self):
        original_agility = self.encapsulation_pillar.hero.get_agility()
        self.encapsulation_pillar.enhance()
        self.assertEqual(self.encapsulation_pillar.hero.get_agility(), original_agility + 4)


