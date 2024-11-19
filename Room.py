
class Room:
    """
    constructor for the room class
    """
    def __init__(self,northWall,southWall,eastWall,westWall,location,potion,monster):
        #boolean values for if a wall exists
        self.set_nwall(northWall)
        self.set_ewall(eastWall)
        self.set_swall(southWall)
        self.set_wwall(westWall)
        self.set_potion(potion)
        self.set_monster(monster)
        self.set_location(location)

    """
    setters for the instance fields
    """

    def set_nwall(self,wall):
        if wall:
            self.northWall = True
        else:
            self.northWall = False

    def set_swall(self,wall):
        if wall:
            self.southWall = True
        else:
            self.southWall = False


    def set_ewall(self,wall):
        if wall:
            self.eastWall = True
        else:
            self.eastWall = False

    def set_wwall(self,wall):
        if wall:
            self.westWall = True
        else:
            self.westWall = False

    def set_monster(self,monster):
            self.monster = monster

    def set_potion(self,potion):
            self.potion = potion

    def set_location(self,location):
        if location is not None:
            self.location = location
        else:
            print("Location value is null.")

    #getters for room
    def get_nwall(self):
        return self.northWall

    def get_swall(self):
        return self.southWall

    def get_ewall(self):
        return self.eastWall

    def get_wwall(self):
        return self.westWall

    def get_location(self):
        return self.location

    def get_potion(self):
        return self.potion

    def get_monster(self):
        return self.monster
