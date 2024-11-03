from abc import ABC
class Pillar(ABC):

    """
    Construction for abstract base class for pillar object,
    passes incoming parameters to a setter method to check that
    incoming data is valid.

    @param name of OO pillar
    @param image for that pillar (GUI)
    """
    def __init__(theSelf, theName, theImage):
        theSelf.setFields(theName, theImage)


    """
    Setter methods checks that name and image for pillar
    is not null and then sets fields for pillar object
    to those values.
    
    @param name of OO pillar
    @param image for that pillar (GUI)
    """
    def setFields(theSelf, theName, theImage):
        if theName is not None and theImage is not None:
            theSelf.myName = theName
            theSelf.myImage = theImage
        else:
            print("The name or image is for this pillar is null")


    """
    Once a hero finds the pillar, it will increase the hero's
    max HP by 10 points and fully heal the hero.
    
    @param hero for game
    """
    def increaseHP(theSelf, theHero):
        theHero.setMaxHealth(theHero.getMaxHealth() + 10)
        theHero.setHealth(theHero.getMaxHealth())

    """
    Add pillar to inventory
    
    @param the dungeon
    """
    def addToInventory(theSelf, theDungeon):
        theDungeon.addToInventory(theSelf)


class AbstractionPillar(Pillar):
    pass
class PolymorphismPillar(Pillar):
    pass
class InheritancePillar(Pillar):
    pass
class EncapsulationPillar(Pillar):
    pass

