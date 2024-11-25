import pygame

from Room import Room
from random import choice
from View import View
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

        if x > 0:
            west = self.room_array[x - 1][y]
            if not west.get_has_visited():
                neighbors.append(west)
        if y > 0:
            north = self.room_array[x][y - 1]
            if not north.get_has_visited():
                neighbors.append(north)
        if x < self.size - 1:
            east = self.room_array[x + 1][y]
            if not east.get_has_visited():
                neighbors.append(east)
        if y < self.size - 1:
            south = self.room_array[x][y + 1]
            if not south.get_has_visited():
                neighbors.append(south)
        return choice(neighbors) if neighbors else None
    def remove_walls(self, current, next_room):
        curr_location = current.get_location()
        next_location = next_room.get_location()
        curr_x = curr_location[0]
        curr_y = curr_location[1]
        next_x = next_location[0]
        next_y = next_location[1]
        dx = curr_x - next_x
        if dx == 1:
            current.set_wwall(False)
            next_room.set_ewall(False)
        elif dx == -1:
            current.set_ewall(False)
            next_room.set_wwall(False)
        dy = curr_y - next_y
        if dy == 1:
            current.set_nwall(False)
            next_room.set_swall(False)
        elif dy == -1:
            current.set_swall(False)
            next_room.set_nwall(False)
        #next_room.set_has_visited(True)


    def generate_maze(self):
        current_room = self.room_array[0][0]
        stack = []
        break_count = 1
        while break_count != (self.size * self.size):
            current_room.set_has_visited(True)
            next_room = self.check_neighbors(current_room)
            if next_room is not None:
                next_room.set_has_visited(True)
                break_count += 1
                stack.append(current_room)
                self.remove_walls(current_room, next_room)
                current_room = next_room
            elif stack:
                current_room = stack.pop()
        return self.room_array

thing = Dungeon(6)
array = thing.generate_maze()
run = True
while run:
    View.screen.fill(0)
    for i in range(len(array)):
        for j in range(len(array[i])):
            View.draw_room(array[i][j])
    pygame.display.update()
