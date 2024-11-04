from abc import ABC, abstractmethod

"""
The abstract potion class for both the health and 
vision potions.
"""
class Potion(ABC):
    myImage = none
    """
    Constructor for abstract base class of potion
    @param theImage is the image for the potion
    """
    def __init__(theSelf, theImage):
        if theImage is not None:
            theSelf.myImage = theImage



    """
    setter method for the image of the potion
    @param theImage the image for the potion
    """
    def setImage(theSelf,theImage):
        if theImage is not None:
            theSelf.myImage = theImage
        else:
            print("Image string is null")


    """
    gets image for the potion
    @return theImage returns the image
    """
    def getImage(theSelf):
        return theSelf.theImage

    """
    the drink method used to determine when to remove the potion 
    from the inventory
    """
    @abstractmethod
    def drink(self):
        return True

"""
The healthPotion child class of the Potion ABC
"""
class HealthPotion(Potion):
    myHP = 0
  
    def __init__(theSelf, theImage, theHP):
        super().__init__(theImage)
        if theHP is > 0:
            theSelf.myHP = theHP

    def drink(self):
        return True

"""
the vision potion child class of the Potion ABC
"""
class VisionPotion(Potion):
  
    super().__init__(theImage)
    def drink(self):
        return True
