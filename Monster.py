from CharacterInterface import CharacterInterface
class Monster(CharacterInterface):
    def __init__(self, name, image, max_hp, agility, element, opposite, basic_attack,
                 special_attack):
        super().__init__(name, image, max_hp, agility, element, opposite, basic_attack,
                         special_attack)



