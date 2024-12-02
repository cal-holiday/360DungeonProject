from Model.Potion import HealthPotion, VisionPotion
from Model.Pillar import PolymorphismPillar, EncapsulationPillar, InheritancePillar, AbstractionPillar


class Inventory:
    __instance = None
    @staticmethod
    def get_instance():
        if Inventory.__instance is not None:
            return Inventory.__instance
        else:
            raise Exception("Inventory does not exist yet!")

    def __init__(self):
        if Inventory.__instance is not None:
            raise Exception("Inventory already exists!")
        else:
            self.health_potions = []
            self.vision_potions = []
            self.pillars = []
            Inventory.__instance = self


    def add(self, object):
        if object is not None:
            if (isinstance(object, PolymorphismPillar)
                    or isinstance(object, EncapsulationPillar)
                    or isinstance(object, InheritancePillar)
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

    def has_health_potion(self):
        return len(self.health_potions) > 0

    def has_vision_potion(self):
        return len(self.vision_potions) > 0

    def drink_health_potion(self):
        if self.has_health_potion():
            self.health_potions[0].drink()
            del self.health_potions[0]

    def drink_vision_potion(self, potion):
        if len(self.vision_potions) > 0:
            self.vision_potions[0].drink()
            del self.vision_potions[0]

    def has_all_pillars(self):
        return len(self.pillars) == 4

    def get_pillars(self):
        return self.pillars
