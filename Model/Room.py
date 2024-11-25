
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
        self.has_visited = False
        self.hero_has_visited = False

    """
    setters for the instance fields
    """

    def set_nwall(self,wall):
        if wall is not None:
            self.northWall = wall
        else:
            print("Wall value is null.")

    def set_swall(self,wall):
        if wall is not None:
            self.southWall = wall
        else:
            print("Wall value is null.")

    def set_ewall(self,wall):
        if wall is not None:
            self.eastWall = wall
        else:
            print("Wall value is null.")

    def set_wwall(self,wall):
        if wall is not None:
            self.westWall = wall
        else:
            print("Wall value is null.")

    def set_monster(self,monster):
        self.monster = monster


    def set_potion(self,potion):
        self.potion = potion


    def set_location(self,location):
        if location is not None:
            self.location = location
        else:
            print("Location value is null.")
            
    def set_has_visited(self, visited):
        if isinstance(visited, bool) and visited is not None:
            self.has_visited = visited
        else:
            print("Visited status needs to be a boolean.")

    def set_hero_has_visited(self, visited):
        if isinstance(visited, bool) and visited is not None:
            self.hero_has_visited = visited
        else:
            print("Visited status needs to be a boolean.")

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

    def get_has_visited(self):
        return self.has_visited

    def get_hero_has_visited(self):
        return self.hero_has_visited
