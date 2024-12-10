from random import randint

from Model.CharacterInterface import CharacterInterface
from Model.Pillar import AbstractionPillar
from Model.Potion import HealthPotion


class Monster(CharacterInterface):
    def __init__(self, name, image, hit_image, dead_image, max_hp, agility, element):
        super().__init__(name, image, hit_image, dead_image, max_hp, agility, element)
        self.hp = max_hp
        self.has_items()

    def has_items(self):
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        num3 = randint(1, 10)

        if num1 > 4:
            self.has_health_potion = True
            #in battle at the end, checks if this is true and creates and adds a potion into inventory
        if num2 > 4:
            self.has_vision_potion = True
        if num3 > 4:
            if AbstractionPillar.__instance
            #check if pillars are made and add one if possible to inventory at end of battle


    def attack(self):
        return super().attack()

    def special_attack(self):
        return super().special_attack()

    def heal(self):
        did_heal = False
        roll = randint(1,20)
        if roll > 10 and self.get_hp() <= (self.get_max_hp() - 5):
            self.set_hp(self.get_hp() + 5)
            did_heal = True
        return did_heal

    def get_image(self):
        return self.image
    def get_hp(self):
        return self.hp
