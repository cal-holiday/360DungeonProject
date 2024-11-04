from CharacterInterface import CharacterInterface
class Monster(CharacterInterface):
    def __init__(theSelf, theName, theImage, theHealth, theMaxHP, theAgility, theElement, theOpposite, theBasicAttack,
                 theMainAttack):
        super().__init__(theName, theImage, theHealth, theMaxHP, theAgility, theElement, theOpposite, theBasicAttack,
                         theMainAttack)



