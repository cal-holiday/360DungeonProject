from abc import ABC
from enum import Enum
from random import randint


class CharacterInterface(ABC):
    BASIC_DAMAGE = 5
    SPECIAL_DAMAGE = 10

    #constructor
    def __init__(self, name, image, maxHP, agility, element, opposite):
        self.setName(name)
        self.setImage(image)
        self.setMaxHP(maxHP)
        self.setAgility(agility)
        self.setElement(element)
        self.setOppositeElement(opposite)


    #setter methods
    #setters
    def setName(self, name):
        if name is not None:
            self.name = name
        else:
            print("Name string is null")

    def setImage(self, image):
        if image is not None:
            self.image = image
        else:
            print("Image string is null")

    def setMaxHP(self, maxHP):
        if maxHP > 0:
            self.maxHP = maxHP
            self.set_hp(maxHP)
        else:
            print("Max HP cannot be 0 or negative")

    def set_hp(self, hp):
        if 0 < hp <= self.maxHP:
            self.hp = hp
        else:
            print("HP cannot be 0 or negative or higher than MaxHP")

    def setAgility(self, agility):
        if agility > 0:
            self.agility = agility
        else:
            print("Agility cannot be 0 or negative")

    def setElement(self, element):
        if isinstance(element, Enum):
            self.element = element
        else:
            print(f"{element} is not an Enum.")

    def setOppositeElement(self, element):
        if isinstance(element, Enum):
            self.opposite = element
        else:
            print(f"{element} is not an Enum.")




    #getter methods
    def getName(self):
        return self.name

    def getImage(self):
        return self.image

    def getHealth(self):
        return self.HP

    def getMaxHP(self):
        return self.maxHP

    def getHP(self):
        return self.hp

    def getAgility(self):
        return self.agility

    def getElement(self):
        return self.element

    def getOppositeElement(self):
        return self.opposite

    def attack(self):
        return (randint(1, 20), 5)

    def specialAttack(self):
        return ((randint(1, 20) - 3), 10)