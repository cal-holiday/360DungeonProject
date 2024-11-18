
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
        if wall != None:
            self.northWall = wall
        else:
            print("Wall value is null.")

    def set_swall(self,wall):
        if wall != None:
            self.southWall = wall
        else:
            print("Wall value is null.")

    def set_ewall(self,wall):
        if wall != None:
            self.eastWall = wall
        else:
            print("Wall value is null.")

    def set_wwall(self,wall):
        if wall != None:
            self.westWall = wall
        else:
            print("Wall value is null.")

    def set_monster(self,monster):
        if monster != None:
            self.monster = monster
        else:
            print("Monster value is null.")

    def set_potion(self,potion):
        if potion != None:
            self.potion = potion
        else:
            print("Potion value is null.")

    def set_location(self,location):
        if location != None:
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
