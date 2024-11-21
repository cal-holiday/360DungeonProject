from Model.Potion import Potion


class HealthPotion(Potion):
    myHP = 0
  
    def __init__(theSelf, theImage, theHP):
        super().__init__(theImage)
        if theHP  > 0:
            theSelf.myHP = theHP

    def drink(self):
        return True
