from random import randint

from Model.CharacterInterface import CharacterInterface
from Model.Potion import HealthPotion, VisionPotion


class Monster(CharacterInterface):
    def __init__(self, name, image, hit_image, dead_image, max_hp, agility, element):
        super().__init__(name, image, hit_image, dead_image, max_hp, agility, element)
        self.hp = max_hp
        self.pillar = None
        self.health_potion = None
        self.vision_potion = None
        num1 = randint(1,10)
        num2 = randint(1,10)
        if num1 > 4:
            self.health_potion = HealthPotion()
        if num2 > 4:
            self.vision_potion = VisionPotion()

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
    def get_pillar(self):
        return self.pillar
    def get_health_potion(self):
        if self.has_health_potion():
            return self.health_potion
        else:
            raise ValueError("Monster has no health potion!")
    def get_vision_potion(self):
        if self.has_vision_potion():
            return self.vision_potion
        else:
            raise ValueError("Monster has no vision potion!")

    def has_health_potion(self):
        return self.health_potion is not None
    def has_vision_potion(self):
        return self.vision_potion is not None
    def has_pillar(self):
        return self.pillar is not None

    def set_pillar(self, pillar):
        self.pillar = pillar
