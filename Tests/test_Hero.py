from unittest import TestCase
from Element import Element
from Model.Hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("name", "image", 100, 2, Element.EARTH)
    def test_attack(self):
        isTrue = False
        result = self.hero.attack()
        if result[0] >= 1 and result[1] >= 5:
            isTrue = True
        self.assertEqual(isTrue, True)

    def test_attack_with_attack_mod(self):
        isTrue = False
        self.hero.set_attack_mod(2) #simulating hero with inheritance pillar
        result = self.hero.attack()
        if result[0] >= 3 and result[1] >= 5:
            isTrue = True
        self.assertEqual(isTrue, True)

    def test_attack_with_damage_mod(self):
        isTrue = False
        self.hero.set_damage_mod(5) #simulating hero with abstraction pillar
        result = self.hero.attack()
        if result[0] >= 1 and result[1] >= 10:
            isTrue = True
        self.assertEqual(isTrue, True)

    def test_special_attack(self):
        isTrue = False
        result = self.hero.special_attack()
        if result[0] >= 1 and result[1] >= 10:
            isTrue = True
        self.assertEqual(isTrue, True)

    def test_special_attack_with_attack_mod(self):
        isTrue = False
        self.hero.set_attack_mod(2)  # simulating hero with inheritance pillar
        result = self.hero.special_attack()
        if result[0] >= 3 and result[1] >= 10:
            isTrue = True
        self.assertEqual(isTrue, True)

    def test_special_attack_with_damage_mod(self):
        isTrue = False
        self.hero.set_damage_mod(5)  # simulating hero with abstraction pillar
        result = self.hero.special_attack()
        if result[0] >= 1 and result[1] >= 15:
            isTrue = True
        self.assertEqual(isTrue, True)

    def test_set_attack_mod(self):
        with self.assertRaises(ValueError):
            self.hero.set_attack_mod(-1)

        self.hero.set_attack_mod(6)
        self.assertEqual(self.hero.get_attack_mod(), 6)

    def test_set_damage_mod(self):
        with self.assertRaises(ValueError):
            self.hero.set_damage_mod(-1)

        self.hero.set_damage_mod(10)
        self.assertEqual(self.hero.get_damage_mod(), 10)

    def test_set_x(self):
        with self.assertRaises(ValueError):
            self.hero.set_x("Hi")

        self.hero.set_x(58)
        self.assertEqual(self.hero.get_x(), 58)

        self.hero.set_x(-24)
        self.assertEqual(self.hero.get_x(),-24)

    def test_set_y(self):
        with self.assertRaises(ValueError):
            self.hero.set_y("Hi")

        self.hero.set_y(45)
        self.assertEqual(self.hero.get_y(), 45)

        self.hero.set_y(-38)
        self.assertEqual(self.hero.get_y(), -38)

    def test_set_vision_status(self):
        self.assertEqual(self.hero.drank_vision_potion, False)
        self.hero.set_vision_status(True)
        self.assertEqual(self.hero.drank_vision_potion, True)

    def test_get_vision_status(self):
        self.assertEqual(self.hero.get_drank_vision_potion(), False)