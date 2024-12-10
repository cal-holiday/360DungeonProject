from random import randint

from Model.CharacterInterface import CharacterInterface
class Monster(CharacterInterface):
    def __init__(self, name, image, hit_image, dead_image, max_hp, agility, element):
        super().__init__(name, image, hit_image, dead_image, max_hp, agility, element)
        self.hp = max_hp
        self.pillar = None

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
    def set_pillar(self, pillar):
        self.pillar = pillar
