from Model.Potion import HealthPotion, VisionPotion
from Model.Pillar import PolymorphismPillar, EncapsulationPillar, InheritancePillar, AbstractionPillar


class Inventory:
    __instance = None
    @staticmethod
    def get_instance():
        """if Inventory.__instance is not None:
            return Inventory.__instance
        else:
            raise Exception("Inventory does not exist yet!")"""
        return Inventory.__instance

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
    def delete_inventory(self):
        if not Inventory.__instance is None:
            Inventory.__instance = None
        else:
            pass
        #del self

    def has_health_potion(self):
        return len(self.health_potions) > 0

    def number_of_health_potions(self):
        return len(self.health_potions)

    def has_vision_potion(self):
        return len(self.vision_potions) > 0

    def drink_health_potion(self):
        if self.has_health_potion():
            self.health_potions[-1].drink()
            self.health_potions.pop()

    def drink_vision_potion(self):
        if len(self.vision_potions) > 0:
            self.vision_potions[-1].drink()
            self.vision_potions.pop()

    def has_all_pillars(self):
        return len(self.pillars) == 4

    def get_pillars(self):
        return self.pillars

    def get_health_potions(self):
        return self.health_potions

    def get_vision_potions(self):
        return self.vision_potions
