from abc import ABC
from enum import Enum
from random import randint


def attack():
    return randint(1,20)


def specialAttack():
    return randint(1, 20) - 3


class CharacterInterface(ABC):

    #constructor
    def __init__(self, name, image, maxHP, agility, element, opposite, basicAttack, specialAttack):
        self.setName(name)
        self.setImage(image)
        self.setMaxHP(maxHP)
        self.setAgility(agility)
        self.setElement(element)
        self.setOppositeElement(opposite)
        self.setAttack(basicAttack)
        self.setSpecialAttack(specialAttack)


    #setter methods
    #setters
    def setName(self, name):
        if name is not None:
            self.myName = name
        else:
            print("Name string is null")

    def setImage(self, image):
        if image is not None:
            self.myImage = image
        else:
            print("Image string is null")

    def setMaxHP(self, maxHP):
        if maxHP > 0:
            self.myMaxHP = maxHP
            self.myHP = maxHP
        else:
            print("Max HP cannot be 0 or negative")

    def setAgility(self, agility):
        if agility > 0:
            self.myAgility = agility
        else:
            print("Agility cannot be 0 or negative")

    def setElement(self, element):
        if isinstance(element, Enum):
            self.myElement = element
        else:
            print(f"{element} is not an Enum.")

    def setOppositeElement(self, element):
        if isinstance(element, Enum):
            self.myElement = element
        else:
            print(f"{element} is not an Enum.")

    def setAttack(self, attack):
        if attack > 0:
            self.myAttack = attack
        else:
            print("Basic attack cannot be 0 or negative")

    def setSpecialAttack(self, specialAttack):
        if specialAttack > 0:
            self.mySpecialAttack = specialAttack
        else:
            print("Main attack cannot be 0 or negative")



    #getter methods
    def getName(self):
        return self.myName

    def getImage(self):
        return self.myImage

    def getHealth(self):
        return self.myHealth

    def getHP(self):
        return self.myMaxHP

    def getAgility(self):
        return self.myAgility

    def getElement(self):
        return self.myElement

    def getOppositeElement(self):
        return self.myOppositeElement

    def getBasicAttack(self):
        return self.myBasicAttack

    def getMainAttack(self):
        return self.myMainAttack
