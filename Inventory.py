import Pillar
import Potion


class Inventory:
    def __init__(self, hero):
        self.health_potions = []
        self.vision_potions = []
        self.pillars = []
        self.has_all_pillars = False
        if hero is not None:
            self.hero = hero


    def _add(self, object):
        if object is not None:
            if object is isinstance(object, Pillar):
                object.enhance()
                self.pillars.append(object)
            elif object is isinstance(object, Potion):
                if object.get_name() is "health_potion":
                    self.health_potions.append(object)
                else:
                    self.vision_potions.append(object)
        else:
            print("Cannot add null object to inventory")


    def _drink_potion(self, potion):
        if len(self.health_potions) > 0 and potion.get_name() is "health":
            self.health_potions[0].drink()
            del self.health_potions[0]
        elif len(self.vision_potions) > 0:
            self.vision_potions[0].drink()
            del self.vision_potions[0]

    def _has_all_pillars(self):
        if len(self.pillars) is 4:
            self.has_all_pillars = True

