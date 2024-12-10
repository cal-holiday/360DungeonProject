import pygame

from Controller import Battle_Controller
from Model.Dungeon import Dungeon
from Model.Pillar import AbstractionPillar, PolymorphismPillar, InheritancePillar, EncapsulationPillar
from Model.Potion import HealthPotion
from View import View
from Model.Direction import Direction
from Model.Element import Element
from Model.CharacterFactory import CharacterFactory
from Model.Room import Room
from Model.Hero import Hero
from Model.Inventory import Inventory

class ControllerHero(pygame.sprite.Sprite):
    left = False
    right = False
    up = False
    down = False

    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.rect = rect
        self.rect.topleft = (Hero.get_instance().get_x(), Hero.get_instance().get_y())


    def move(self):
        hero_x = Hero.get_instance().get_x()
        hero_y = Hero.get_instance().get_y()

        for rect in potion_rect:
            if self.rect.colliderect(rect):
                pygame.event.post(pygame.event.Event(GET_POTION))
                break
        for rect in monster_rect:
            if self.rect.colliderect(rect):
                pygame.event.post(pygame.event.Event(MONSTER_BATTLE))
                break
        if exit_rect is not None and self.rect.colliderect(exit_rect):
            pygame.event.post(pygame.event.Event(EXIT_DUNGEON))
        if self.down and not self.collide_down():
            Hero.get_instance().set_direction(Direction.SOUTH)
            Hero.get_instance().set_y(hero_y + 5)
        if self.up and not self.collide_up():
            Hero.get_instance().set_direction(Direction.NORTH)
            Hero.get_instance().set_y(hero_y - 5)
        if self.right and not self.collide_right():
            Hero.get_instance().set_direction(Direction.EAST)
            Hero.get_instance().set_x(hero_x + 5)
        if self.left and not self.collide_left():
            Hero.get_instance().set_direction(Direction.WEST)
            Hero.get_instance().set_x(hero_x - 5)
        self.rect.topleft = (Hero.get_instance().get_x() - View.get_camera_offset()[0], Hero.get_instance().get_y() - View.get_camera_offset()[1])

    def collide_down(self):
        for rect_list in room_rects:
            for rect in rect_list:
                if self.rect.colliderect(rect) and self.rect.bottom <= rect.top + 5:
                    return True
        return False

    def collide_up(self):
        for rect_list in room_rects:
            for rect in rect_list:
                if self.rect.colliderect(rect) and self.rect.top >= rect.bottom - 5:
                    return True
        return False

    def collide_right(self):
        for rect_list in room_rects:
            for rect in rect_list:
                if self.rect.colliderect(rect) and self.rect.right <= rect.left + 5:
                    return True
        return False

    def collide_left(self):
        for rect_list in room_rects:
            for rect in rect_list:
                if self.rect.colliderect(rect) and self.rect.left >= rect.right - 5:
                    return True
        return False


def handle_event(event):
    global RUN
    global INVENTORY_CLICKED
    room = get_current_room()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
            player.down = True
        if event.key == pygame.K_w:
            player.up = True
        if event.key == pygame.K_d:
            player.right = True
        if event.key == pygame.K_a:
            player.left = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_s:
            player.down = False
        if event.key == pygame.K_w:
            player.up = False
        if event.key == pygame.K_d:
            player.right = False
        if event.key == pygame.K_a:
            player.left = False
    if event.type == GET_POTION:
        Inventory.get_instance().add(room.get_potion())
        room.set_potion(None)
    if event.type == MONSTER_BATTLE:
        print(room.get_location())
        print(room.get_monster())
        Battle_Controller.run(room.get_monster())
        player.down = False
        player.up = False
        player.right = False
        player.left = False
        room.set_monster(None)
    if event.type == EXIT_DUNGEON:
        print("END Game")
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Check if a hero is clicked
        for i in range(len(toolbar_rects)):
            if toolbar_rects[i].collidepoint(event.pos):
                if i == 0:
                    if INVENTORY_CLICKED:
                        INVENTORY_CLICKED = False
                    else:
                        INVENTORY_CLICKED = True
                        print("Inventory")
                        print(Inventory.get_instance().get_health_potions())
                elif i == 1:
                    print("Map")
                elif i == 2:
                    print("Save")
                elif i == 3:
                    print("Help")
                else:
                    RUN = False
            for i in range(len(health_potion_rects)):
                if health_potion_rects[i].collidepoint(event.pos):
                    Inventory.get_instance().drink_health_potion()
            for i in range(len(vision_potion_rects)):
                if vision_potion_rects[i].collidepoint(event.pos):
                    Inventory.get_instance().drink_vision_potion()

def get_current_room():
    x = Hero.get_instance().get_x()
    y = Hero.get_instance().get_y()
    room_x = x//View.room_size
    room_y = y//View.room_size
    return array[room_x][room_y]


clock = pygame.time.Clock()
FPS = 60
RUN = True

GET_POTION = pygame.USEREVENT + 1
MONSTER_BATTLE = pygame.USEREVENT + 2
EXIT_DUNGEON = pygame.USEREVENT + 3

"""
monster = CharacterFactory.create_monster(Element.EARTH)
room = Room(False, False, False, False, (1,1), None, monster)
room.set_has_exit(True)"""
CharacterFactory.create_hero("TEST", Element.AIR)
"""
room_rects = View.draw_room(room)
potion_rect = View.draw_potion(room)
monster_rect = View.draw_monster(room)"""
toolbar_rects = View.draw_toolbar()


inventory = Inventory()
inventory.add(AbstractionPillar())
inventory.add(PolymorphismPillar())
inventory.add(InheritancePillar())
inventory.add(EncapsulationPillar())

health_potion_rects, vision_potion_rects = View.draw_inventory()

Hero.get_instance().set_x(405)
Hero.get_instance().set_y(405)
player = ControllerHero(View.draw_hero())
MONSTER_DEFEATED = False
INVENTORY_CLICKED = False

dungeon = Dungeon(6)
array = dungeon.generate_maze()
dungeon.add_exit()
dungeon.add_monsters()
dungeon.add_health_potions()
dungeon.add_vision_potions()
while RUN:
    camera_offset_x, camera_offset_y = View.get_camera_offset()
    clock.tick(FPS)
    View.screen.fill(0)
    room_rects = []
    monster_rect = []
    potion_rect = []
    exit_rect = None
    for i in range(len(array)):
        for j in range(len(array[i])):
            room_rects.append(View.draw_room(array[i][j]))
            possible_monster = View.draw_monster(array[i][j])
            if not possible_monster is None:
                monster_rect.append(possible_monster)
            possible_potion = View.draw_potion(array[i][j])
            if not possible_potion is None:
                potion_rect.append(possible_potion)
            possible_exit = View.draw_exit(array[i][j])
            if not possible_exit is None:
                exit_rect = possible_exit
    '''room_rects = View.draw_room(room)
    potion_rect = View.draw_potion(room)
    monster_rect = View.draw_monster(room)'''
    toolbar_rects = View.draw_toolbar()

    if INVENTORY_CLICKED:
      View.draw_inventory()
      health_potion_rects, vision_potion_rects = View.draw_inventory()
    #exit_rect = View.draw_exit(room)
    player.move()
    View.draw_hero()
    #View.draw_vision()




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        handle_event(event, )
    pygame.display.update()
pygame.quit()