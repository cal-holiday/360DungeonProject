from random import randint

from CharacterInterface import CharacterInterface
class Monster(CharacterInterface):
    def __init__(self, name, image, max_hp, agility, element, opposite):
        super().__init__(name, image, max_hp, agility, element, opposite)

    def attack(self):
        return super().attack()

    def specialAttack(self):
        return super().specialAttack()

    def heal(self):
        if randint(1, 20) > 10 and self.getHP() <= (self.getMaxHP() - 5):
            self.set_hp(self.getHP() + 5)

