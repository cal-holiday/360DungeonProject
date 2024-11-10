from abc import ABC
from Element import Element
from random import randint


class CharacterInterface(ABC):
    """
    Static fields for all characters. Both monsters and heroes
    deal 5 points damage for a basic attack and 10 for a special
    attack, not including modifiers the hero can add from finding pillars.
    """
    BASIC_DAMAGE = 5
    SPECIAL_DAMAGE = 10

    """
    Constructor for abstract base class for character object,
    passes incoming parameters to a setter method to check that
    incoming data is valid.
    
    @param name of the character
    @param image for the character (GUI)
    @param max hit points(hp) the character can have
    @param agility score of the character, determines if an attack hits
    @param element of the character, enumerated element type
    """
    def __init__(self, name, image, max_hp, agility, element):
        self.set_name(name)
        self.set_image(image)
        self.set_max_hp(max_hp)
        self.set_agility(agility)
        self.set_element(element)


    """
    Setter methods checks that name and image for the character
    is not null and then sets fields for character object
    to those values.
    """
    def set_name(self, name):
        if name is not None:
            self.name = name
        else:
            print("Name string is null")

    def set_image(self, image):
        if image is not None:
            self.image = image
        else:
            print("Image string is null")

    def set_max_hp(self, max_hp):
        if max_hp.isdigit() and max_hp > 0:
            self.max_hp = max_hp
            self.set_hp(max_hp)
        else:
            print("Max HP must be an int and cannot be 0 or negative")

    def set_hp(self, hp):
        if hp.isdigit() and 0 < hp <= self.max_hp:
            self.hp = hp
        else:
            print("HP must be an int and cannot be 0 or negative or higher than MaxHP")

    def set_agility(self, agility):
        if agility.isdigit() and agility > 0:
            self.agility = agility
        else:
            print("Agility must be an int and cannot be 0 or negative")

    def set_element(self, element):
        if isinstance(element, Element):
            self.element = element
        else:
            print(f"{element} is not an Element.")

    def set_x(self, x):
        if isinstance(x, int):
            self.x = x
        else:
            print(x, "is not an integer")

    def set_y(self, y):
        if isinstance(y, int):
            self.y = y
        else:
            print(y, "is not an integer")

    """
    Getters return the values of the fields for a 
    character object
    """
    def get_name(self):
        return self.name

    def get_image(self):
        return self.image

    def get_max_hp(self):
        return self.max_hp

    def get_hp(self):
        return self.hp

    def get_agility(self):
        return self.agility

    def get_element(self):
        return self.element

    def get_opposite_element(self):
        return self.element.get_opposite()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    """
    When a character uses its basic attack, it sends the character
    it is attacking a tuple containing the value of the attack so 
    the other player can determine if they can dodge the attack
    and the amount of damage (5) the attack will do if it lands.
    """
    def attack(self):
        return randint(1, 20), 5

    """
    When a character uses its special attack, it sends the character
    it is attacking a tuple containing the value of the attack (which
    is decreased by 3 because it is less likely to hit) so 
    the other player can determine if they can dodge the attack
    and the amount of damage (10) the attack will do if it lands.
    """
    def special_attack(self):
        return (randint(1, 20) - 3), 10
