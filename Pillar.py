from abc import ABC, abstractmethod


class Pillar(ABC):

    """
    Construction for abstract base class for pillar object,
    passes incoming parameters to a setter method to check that
    incoming data is valid.

    @param name of OO pillar
    @param image for that pillar (GUI)
    @param hero reference so pillars can give hero perks
    """
    def __init__(self, name, image, hero):
        self.set_name(name)
        self.set_image(image)
        self.set_hero(hero)


    """
    Setter methods checks that name and image for pillar
    is not null and then sets fields for pillar object
    to those values.
    """
    def set_name(self, name):
        if name is not None:
            self.name = name
        else:
            print("The name for this pillar is null")

    def set_image(self, image):
        if image is not None:
            self.image = image
        else:
            print("The image for this pillar is null")
    def set_hero(self, hero):
        if hero is not None:
            self.hero = hero
        else:
            print("The hero for this pillar is null")


    def get_name(self):
        return self.name

    def get_image(self):
        return self.image

    def get_hero(self):
        return self.hero

    """
    Every time hero finds pillar it fully heals the hero
    """
    def restore_health(self):
        self.hero.set_hp(self.hero.get_max_hp())

    """
    Abstract method that all subclasses have to implement,
    each pillar gives the hero a different perk
    """
    @abstractmethod
    def enhance(self):
        pass



"""
Abstraction pillar adds +5 damage to basic and special attack
"""
class AbstractionPillar(Pillar):
    def enhance(self):
        self.hero.add_damage_mod(5)


"""
Polymorphism pillar increases hero's max health by 10
"""
class PolymorphismPillar(Pillar):
    def enhance(self):
        self.hero.set_max_hp(self.hero.getMaxHP + 10)


"""
Inheritance pillar does +2 hit chance
"""
class InheritancePillar(Pillar):
    def enhance(self):
        self.hero.add_attack_mod(2)

"""
Encapsulation pillar adds +4 to hero's agility stat
"""
class EncapsulationPillar(Pillar):
    def enhance(self):
        self.hero.set_agility(self.hero.get_agility() + 4)

