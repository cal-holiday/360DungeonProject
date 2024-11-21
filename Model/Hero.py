from Model.CharacterInterface import CharacterInterface
from Model.Direction import Direction
class Hero(CharacterInterface):
    damage_mod = 0
    attack_mod = 0
    x = 0
    y = 0
    drank_vision_potion = False

    def __init__(self, name, image, max_hp, agility, element):
        super().__init__(name, image, max_hp, agility, element)

    def attack(self):
        pre_mod = super().attack()
        mod = (pre_mod[0] + self.attack_mod, pre_mod[1] + self.damage_mod)
        return mod

    def special_attack(self):
        pre_mod = super().special_attack()
        mod = (pre_mod[0] + self.attack_mod, pre_mod[1] + self.damage_mod)
        return mod

    def set_attack_mod(self, attack_mod):
        if isinstance(attack_mod, int) and attack_mod > 0:
            self.attack_mod = attack_mod
        else:
            raise ValueError("Attack modifier must be an int and cannot be 0 or negative")

    def set_damage_mod(self, damage_mod):
        if isinstance(damage_mod, int) and damage_mod > 0:
            self.damage_mod = damage_mod
        else:
            raise ValueError("Damage modifier must be an int and cannot be 0 or negative")

    def set_direction(self, direction):
        if isinstance(direction, Direction):
            self.direction = direction
        else:
            raise ValueError(f"{direction} is not an Direction.")

    def set_x(self, x):
        if isinstance(x, int):
            self.x = x
        else:
            raise ValueError(x, "is not an integer")

    def set_y(self, y):
        if isinstance(y, int):
            self.y = y
        else:
            raise ValueError(y, "is not an integer")

    def set_vision_status(self, value):
        if isinstance(value, bool):
            self.drank_vision_potion = value
        else:
            raise ValueError("Parameter needs to be a boolean")


    def get_damage_mod(self):
        return self.damage_mod

    def get_attack_mod(self):
        return self.attack_mod

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_direction(self):
        return self.direction

    def get_drank_vision_potion(self):
        return self.drank_vision_potion


