from abc import ABC, abstractmethod

"""
The abstract potion class for both the health and 
vision potions.
"""


class Potion(ABC):
    """
    Constructor for abstract base class of potion
    @param image is the image for the potion
    """

    def __init__(self, name, image, hero):
        self.name = name
        self.set_image(image)
        self.set_hero(hero)

    """
    setter method for the image of the potion
    @param image the image for the potion
    """
    def set_image(self, image):
        if image is not None:
            self.image = image
        else:
            raise ValueError("Image string is null")

    def set_hero(self, hero):
        if hero is not None:
            self.hero = hero
        else:
            raise ValueError("Hero is null")

    """
    return name of potion i.e health or vision
    """
    def get_name(self):
        return self.name

    """
    gets image for the potion
    @return image returns the image
    """
    def get_image(self):
        return self.image

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
    def __init__(self, image, hero):
        super().__init__("health", image, hero)
    def drink(self):
        if self.hero.get_hp() + 10 > self.hero.get_max_hp():
            self.hero.set_hp(self.hero.get_max_hp())
        else:
            self.hero.set_hp(self.hero.get_hp() + 10)

"""
the vision potion child class of the Potion ABC
"""


class VisionPotion(Potion):
    def __init__(self, image, hero):
        super().__init__("vision", image, hero)
    def drink(self):
        self.hero.set_vision_status(True)