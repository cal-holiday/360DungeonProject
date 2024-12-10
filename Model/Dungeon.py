import pygame

from Model.CharacterFactory import CharacterFactory
from Model.Element import Element
from Model.Hero import Hero
from Model.Pillar import PolymorphismPillar, AbstractionPillar, EncapsulationPillar, InheritancePillar
from Model.Potion import HealthPotion, VisionPotion
from Model.Room import Room
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
            self.room_array = [[Room(True, True, True, True, (x, y), None, None)for y in range(cols)] for x in range(rows)]
            self.room_array = self.generate_maze()
            self.add_exit()
            self.add_monsters()
            self.add_health_potions()
            self.add_vision_potions()
            Dungeon.__instance = self
    def check_neighbors(self, room):
        location = room.get_location()
        col = location[0]
        row = location[1]
        neighbors = []

        if col > 0:
            west = self.room_array[col-1][row]
            if not west.get_has_visited():
                neighbors.append(west)
        if row > 0:
            north = self.room_array[col][row-1]
            if not north.get_has_visited():
                neighbors.append(north)
        if col < self.size - 1:
            east = self.room_array[col+1][row]
            if not east.get_has_visited():
                neighbors.append(east)
        if row < self.size - 1:
            south = self.room_array[col][row +1]
            if not south.get_has_visited():
                neighbors.append(south)
        return choice(neighbors) if neighbors else None

    def remove_walls(self, current, next_room):
        curr_location = current.get_location()
        next_location = next_room.get_location()
        curr_row = curr_location[1]
        curr_col = curr_location[0]
        next_row = next_location[1]
        next_col = next_location[0]
        d_row = curr_row - next_row
        if d_row == 1:
            self.room_array[curr_col][curr_row].set_nwall(False)

            self.room_array[curr_col][curr_row-1].set_swall(False)

        elif d_row == -1:
            self.room_array[curr_col][curr_row].set_swall(False)

            self.room_array[curr_col][curr_row+1].set_nwall(False)

        d_col = curr_col - next_col
        if d_col == 1:
            self.room_array[curr_col][curr_row].set_wwall(False)

            self.room_array[curr_col-1][curr_row].set_ewall(False)

        elif d_col == -1:
            self.room_array[curr_col][curr_row].set_ewall(False)

            self.room_array[curr_col+1][curr_row].set_wwall(False)



    def generate_maze(self):
        current_room = self.room_array[0][0]
        stack = [current_room]
        while stack:
            next_room = self.check_neighbors(current_room)
            if next_room:
                self.remove_walls(current_room, next_room)
                if not current_room.get_has_visited():
                    stack.append(current_room)
                current_room.set_has_visited(True)
                current_room = next_room
            else:
                while self.check_neighbors(current_room) is None and stack:
                    current_room = stack.pop()
        return self.room_array
    def add_exit(self):
        col = choice(self.room_array)
        row = choice(col)
        row.set_has_exit(True)
    def add_monsters(self):
        number = 4 + self.size//4
        for i in range(number):
            monster = CharacterFactory.create_monster(Element(i%4 +1))
            if i == 0:
                monster.set_pillar(PolymorphismPillar())
            elif i == 1:
                monster.set_pillar(AbstractionPillar())
            elif i == 2:
                monster.set_pillar(EncapsulationPillar())
            elif i == 3:
                monster.set_pillar(InheritancePillar())
            col = choice(self.room_array)
            row = choice(col)
            row.set_monster(monster)
    def add_health_potions(self):
        number = 2 + self.size//8
        potion = HealthPotion()
        for i in range(number):
            col = choice(self.room_array)
            row = choice(col)
            if row.get_monster() is None:
                row.set_potion(potion)
            else:
                i -= i
    def add_vision_potions(self):
        number = 2 + self.size//8
        potion = VisionPotion()
        for i in range(number):
            col = choice(self.room_array)
            row = choice(col)
            if row.get_potion() is None and row.get_monster() is None:
                row.set_potion(potion)
            else:
                i -= 1


"""
CharacterFactory.create_hero("TEST", Element.AIR)
Hero.get_instance().set_x(258)
Hero.get_instance().set_y(258)
thing = Dungeon(6)
array = thing.generate_maze()
thing.add_exit()
thing.add_monsters()
thing.add_potions()
run = True
while run:
    View.screen.fill(0)
    for i in range(len(array)):
        for j in range(len(array[i])):
            View.draw_room(array[i][j])
            #View.draw_exit(array[i][j])
            View.draw_monster(array[i][j])
            #View.draw_potion(array[i][j])
    pygame.display.update()
"""