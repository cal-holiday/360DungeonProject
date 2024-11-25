from Room import Room
from random import choice
class Dungeon:
    __instance = None
    @staticmethod
    def get_instance():
        if Dungeon.__instance is not None:
            return Dungeon.__instance
        else:
            raise Exception("Dungeon does not exist yet!")

    def __init__(self, size):
        if Dungeon.__instance is not None:
            raise Exception("Dungeon already exists!")
        else:
            self.size = size
            rows, cols =(size, size)
            self.room_array = [[Room(True, True, True, True, (x, y), None, None)for x in range(cols)] for y in range(rows)]
            Dungeon.__instance = self
    def check_neighbors(self, room):
        location = room.get_location()
        x = location[0]
        y = location[1]
        neighbors = []
        west = None
        east = None
        top = None
        bottom = None
        if x > 0:
            left = self.room_array[x - 1][y]
            if not left.get_has_visited():
                neighbors.append(left)
        if y > 0:
            top = self.room_array[x][y - 1]
            if not top.get_has_visited():
                neighbors.append(top)
        if x < self.size - 1:
            right = self.room_array[x + 1][y]
            if not right.get_has_visited():
                neighbors.append(right)
        if y < self.size - 1:
            bottom = self.room_array[x][y-1]
            if not bottom.get_has_visited():
                neighbors.append(bottom)
        return choice(neighbors) if neighbors else None
