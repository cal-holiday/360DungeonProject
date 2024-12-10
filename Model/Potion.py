from abc import ABC, abstractmethod
from Model.Hero import Hero

"""
The abstract potion class for both the health and 
vision potions.
"""


class Potion(ABC):
    """
    Constructor for abstract base class of potion
    @param image is the image for the potion
    """

    def __init__(self, name):
        self.name = name

    """
    return name of potion i.e health or vision
    """
    def get_name(self):
        return self.name

    """
    gets image for the potion
    @return image returns the image
    """

    """
    the drink method used to determine when to remove the potion 
    from the inventory
    """

    @abstractmethod
    def drink(self):
        pass


"""
The healthPotion child class of the Potion ABC
"""

class HealthPotion(Potion):
    def __init__(self):
        super().__init__("health")
        self.image = "health_potion.png"
    def drink(self):
        if Hero.get_instance().get_hp() + 10 > Hero.get_instance().get_max_hp():
            Hero.get_instance().set_hp(Hero.get_instance().get_max_hp())
        else:
            Hero.get_instance().set_hp(Hero.get_instance().get_hp() + 10)
    def get_image(self):
        return self.image

"""
the vision potion child class of the Potion ABC
"""


class VisionPotion(Potion):
    def __init__(self):
        super().__init__("vision")
        self.image = "vision_potion.png"
    def drink(self):
        Hero.get_instance().set_vision_status(True)
    def get_image(self):
        return self.image