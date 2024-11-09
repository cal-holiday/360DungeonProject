from CharacterInterface import CharacterInterface
class Hero(CharacterInterface):
    attack_mod = 0
    damage_mod = 0
    def __init__(self, name, image, max_hp, agility, element, opposite):
        super().__init__(name, image, max_hp, agility, element, opposite)

    def attack(self):
        pre_mod  = super.attack()
        pre_mod[0] += self.attack_mod
        pre_mod[1] += self.damage_mod

    def specialAttack(self):
        pre_mod  = super.specialAttack()
        pre_mod[0] += self.attack_mod
        pre_mod[1] += self.damage_mod

    def drinkPotion(self):
        if self.getHP() <= (self.getMaxHP() - 5):
            self.set_hp(self.getHP() + 5)


