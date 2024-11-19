from Potion import HealthPotion, VisionPotion
from Pillar import PolymorphismPillar, EncapsulationPillar, InheritancePillar, AbstractionPillar


class Inventory:
    def __init__(self):
        self.health_potions = []
        self.vision_potions = []
        self.pillars = []


    def add(self, object):
        if object is not None:
            if (isinstance(object, PolymorphismPillar)
                    or (isinstance(object, EncapsulationPillar))
                    or (isinstance(object, InheritancePillar))
                    or isinstance(object, AbstractionPillar)):
                self.pillars.append(object)
                object.enhance()
            elif isinstance(object, HealthPotion) or isinstance(object, VisionPotion):
                if object.get_name() == "health":
                    self.health_potions.append(object)
                else:
                    self.vision_potions.append(object)
        else:
            raise ValueError("Cannot add null object to inventory")


    def drink_potion(self, potion):
        if len(self.health_potions) > 0 and potion.get_name() == "health":
            self.health_potions[0].drink()
            del self.health_potions[0]
        elif len(self.vision_potions) > 0:
            self.vision_potions[0].drink()
            del self.vision_potions[0]

    def has_all_pillars(self):
        return len(self.pillars) == 4
