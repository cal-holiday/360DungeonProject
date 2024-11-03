from abc import ABC
from enum import Enum
from random import random


class CharacterInterface(ABC):

    #constructor
    def __init__(theSelf, theName, theImage, theHealth, theMaxHP, theAgility, theElement, theOpposite, theBasicAttack, theMainAttack):
        theSelf.setName(theName)
        theSelf.setImage(theImage)
        theSelf.setInitialHealth(theHealth)
        theSelf.setMaxHP(theMaxHP)
        theSelf.setAgility(theAgility)
        theSelf.setElement(theElement)
        theSelf.setOppositeElement(theOpposite)
        theSelf.setBasicAttack(theBasicAttack)
        theSelf.setMainAttack(theMainAttack)


    #setter methods
    #setters
    def setName(theSelf, theName):
        if theName is not None:
            theSelf.myName = theName
        else:
            print("Name string is null")

    def setImage(theSelf, theImage):
        if theImage is not None:
            theSelf.myImage = theImage
        else:
            print("Image string is null")

    def setInitialHealth(theSelf, theHealth):
        if theHealth > 0:
            theSelf.myHealth = theHealth
        else:
            print("Initial health cannot be 0 or negative")

    def setHealth(theSelf, theHealth):
        theSelf.myHealth = theHealth

    def setMaxHP(theSelf, theMaxHP):
        if theMaxHP > 0:
            theSelf.myMaxHP = theMaxHP
        else:
            print("Max HP cannot be 0 or negative")

    def setAgility(theSelf, theAgility):
        if theAgility > 0:
            theSelf.myAgility = theAgility
        else:
            print("Agility cannot be 0 or negative")

    def setElement(theSelf, theElement):
        if isinstance(theElement, Enum):
            theSelf.myElement = theElement
        else:
            print("Element is not an Enum")

    def setOppositeElement(theSelf, theElement):
        if isinstance(theElement, Enum):
            theSelf.myOppositeElement = theElement
        else:
            print("Opposite element is not an Enum")

    def setBasicAttack(theSelf, theBasicAttack):
        if theBasicAttack > 0:
            theSelf.myBasicAttack = theBasicAttack
        else:
            print("Basic attack cannot be 0 or negative")

    def setMainAttack(theSelf, theMainAttack):
        if theMainAttack > 0:
            theSelf.myMainAttack = theMainAttack
        else:
            print("Main attack cannot be 0 or negative")



    #getter methods
    def getName(theSelf):
        return theSelf.myName

    def getImage(theSelf):
        return theSelf.myImage

    def getHealth(theSelf):
        return theSelf.myHealth

    def getMaxHP(theSelf):
        return theSelf.myMaxHP

    def getAgility(theSelf):
        return theSelf.myAgility

    def getElement(theSelf):
        return theSelf.myElement

    def getOppositeElement(theSelf):
        return theSelf.myOppositeElement

    def getBasicAttack(theSelf):
        return theSelf.myBasicAttack

    def getMainAttack(theSelf):
        return theSelf.myMainAttack


    #behavior methods

    #character has a pretty good chance at healing
    def heal(theSelf):
        randomNum = random.randint(1, 20)
        if randomNum > 10:
            theSelf.setHealth(theSelf.getHealth() + theSelf.getHealth() / 2)

    #for every attack, the opponent has an opportunity to dodge
    # if opponent is quicker than you and rolls higher than 7 -> dodge
    # otherwise if opponent is slower but rolls higher than a 11 -> dodge
    # basic attack should be easier to land than main attacks
    def useBasicAttack(theSelf, theOther):
        dodge = random.randint(1,20)
        if dodge < 7 and theOther.getAgility() > theSelf.getAgility():
            theOther.setHealth(theOther.getHealth() - theSelf.getBasicAttack())
        elif dodge < 11 and theOther.getAgility() < theSelf.getName():
            theOther.setHealth(theOther.getHealth() - theSelf.getBasicAttack())



    #first dodge number is generated
    #if you are faster and dodge is less than 17 -> you have a chance to land main attack on opponent
    #note: if you and opponent are opposite types then you can do double damage if it hits, otherwise normal amount
    #otherwise if the opponent is faster but they roll less than 15 -> you have the chance to hit
    #if you can't hit then they dodge
    #this concept works for both heros and monsters, each time hero or monster attack, the other has a chance to dodge
    def useMainAttack(theSelf, theOther):
        randomNum = random.randint(1, 20)
        dodge = random.randint(1,20)
        if dodge < 17 and theOther.getAgility() < theSelf.getAgility():
            if randomNum > 12 and theOther.getElement() == theSelf.getOppositeElement:
                theOther.setHealth(theOther.getHealth - theSelf.getMainAttack() * 2)
            elif randomNum > 12:
                theOther.setHealth(theOther.getHealth - theSelf.getMainAttack())
        elif dodge < 15 and theOther.getAgility() > theSelf.getAgility():
            if randomNum > 12 and theOther.getElement() == theSelf.getOppositeElement:
                theOther.setHealth(theOther.getHealth - theSelf.getMainAttack() * 2)
            elif randomNum > 12:
                theOther.setHealth(theOther.getHealth - theSelf.getMainAttack())


