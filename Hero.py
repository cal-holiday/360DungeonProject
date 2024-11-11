from CharacterInterface import CharacterInterface
from Direction import Direction
class Hero(CharacterInterface):
    def __init__(self, name, image, max_hp, agility, element):
        super().__init__(name, image, max_hp, agility, element)

    def attack(self):
        pre_mod =  super().attack()
        mod = (pre_mod[0] + self.attack_mod, pre_mod[1] + self.damage_mod)
        return mod

    def special_attack(self):
        pre_mod = super().special_attack()
        mod = (pre_mod[0] + self.attack_mod, pre_mod[1] + self.damage_mod)
        return mod

    def drink_potion(self):
        if self.get_hp() <= (self.get_max_hp() - 10):
            self.set_hp(self.get_hp() + 10)

    def add_attack_mod(self, attack_mod):
        if attack_mod.isdigit() and attack_mod > 0:
            self.attack_mod = attack_mod
        else:
            print("Attack modifier must be an int and cannot be 0 or negative")

    def add_damage_mod(self, damage_mod):
        if damage_mod.isdigit() and damage_mod > 0:
            self.attack_mod = damage_mod
        else:
            print("Attack modifier must be an int and cannot be 0 or negative")
    def set_direction(self, direction):
        if isinstance(direction, Direction):
            self.direction = direction
        else:
            print(f"{direction} is not an Direction.")

    def get_direction(self):
        return self.direction


