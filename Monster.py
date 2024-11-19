from random import randint

from CharacterInterface import CharacterInterface
class Monster(CharacterInterface):
    def __init__(self, name, image, max_hp, agility, element):
        super().__init__(name, image, max_hp, agility, element)

    #if anyone sees this comment, are these necessary or will it work to just go my_monster.attack()?
    #that should call the parent method inherently right?
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

