from random import randint

from CharacterInterface import CharacterInterface
class Monster(CharacterInterface):
    def __init__(self, name, image, max_hp, agility, element, opposite):
        super().__init__(name, image, max_hp, agility, element, opposite)

    def attack(self):
        return super().attack()

    def special_attack(self):
        return super().special_attack()

    def heal(self):
        if randint(1, 20) > 10 and self.get_hp() <= (self.get_max_hp() - 5):
            self.set_hp(self.get_hp() + 5)

