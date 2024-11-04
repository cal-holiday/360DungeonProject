from abc import ABC, abstractmethod

"""
The abstract potion class for both the health and 
vision potions.
"""
class Potion(ABC):
    myImage = None
    """
    Constructor for abstract base class of potion
    @param theImage is the image for the potion
    """
    def __init__(theSelf, image):
        if image is not None:
            theSelf.myImage = image



    """
    setter method for the image of the potion
    @param theImage the image for the potion
    """
    def setImage(self,image):
        if image is not None:
            self.myImage = image
        else:
            print("Image string is null")


    """
    gets image for the potion
    @return theImage returns the image
    """
    def getImage(self):
        return self.image

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

    def __init__(self, image, theHP):
        super().__init__(image)
        if theHP > 0:
            self.myHP = theHP

    def drink(self):
        return True

"""
the vision potion child class of the Potion ABC
"""
class VisionPotion(Potion):
    def __init__(self, image):
        super().__init__(image)

    def drink(self):
        return True
