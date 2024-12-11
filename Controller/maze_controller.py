import pygame

from Controller import Battle_Controller
from Model.Dungeon import Dungeon
from Model.Pillar import AbstractionPillar, PolymorphismPillar, InheritancePillar, EncapsulationPillar
from Model.Potion import HealthPotion, VisionPotion
from View import maze_view
from Model.Direction import Direction
from Model.Element import Element
from Model.CharacterFactory import CharacterFactory
from Model.Room import Room
from Model.Hero import Hero
from Model.Inventory import Inventory

GET_POTION = pygame.USEREVENT + 1
MONSTER_BATTLE = pygame.USEREVENT + 2
EXIT_DUNGEON = pygame.USEREVENT + 3
POTION_REMOVED = False
MONSTER_DEFEATED = False
INVENTORY_CLICKED = False
RUN = True
room_rects = []
monster_rect = []
potion_rect = []
toolbar_rects = []
health_potion_rects = []
vision_potion_rects = []
exit_rect = None
player = None
array = []
potion_time = 0

def run(screen):
    global room_rects
    global monster_rect
    global exit_rect
    global player
    global array
    global toolbar_rects
    global GET_POTION
    global MONSTER_BATTLE
    global EXIT_DUNGEON
    global RUN
    global potion_rect
    global health_potion_rects
    global vision_potion_rects
    global INVENTORY_CLICKED
    global potion_time
    clock = pygame.time.Clock()
    fps = 60
    GET_POTION = pygame.USEREVENT + 1
    MONSTER_BATTLE = pygame.USEREVENT + 2
    EXIT_DUNGEON = pygame.USEREVENT + 3

    toolbar_rects = maze_view.draw_toolbar(screen)

    inventory = Inventory()
    inventory.add(VisionPotion())
    inventory.add(VisionPotion())
    inventory.add(VisionPotion())
    health_potion_rects, vision_potion_rects = maze_view.draw_inventory(screen)

    Hero.get_instance().set_x(405)
    Hero.get_instance().set_y(405)
    player = ControllerHero(maze_view.draw_hero(screen))
    INVENTORY_CLICKED = False

    dungeon = Dungeon(6)
    array = dungeon.room_array
    while RUN:
        camera_offset_x, camera_offset_y = maze_view.get_camera_offset()
        clock.tick(fps)
        screen.fill(0)
        room_rects = []
        monster_rect = []
        potion_rect = []
        exit_rect = None
        for i in range(len(array)):
            for j in range(len(array[i])):
                room_rects.append(maze_view.draw_room(screen,array[i][j]))
                possible_monster = maze_view.draw_monster(screen, array[i][j])
                if not possible_monster is None:
                    monster_rect.append(possible_monster)
                possible_potion = maze_view.draw_potion(screen, array[i][j])
                if not possible_potion is None:
                    potion_rect.append(possible_potion)
                possible_exit = maze_view.draw_exit(screen, array[i][j])
                if not possible_exit is None:
                    exit_rect = possible_exit

        player.move()
        maze_view.draw_hero(screen)
        if potion_time == 0:
            maze_view.draw_vision(screen)
        else:
            potion_time -= 1
        toolbar_rects = maze_view.draw_toolbar(screen)

        if INVENTORY_CLICKED:
            maze_view.draw_inventory(screen)
            health_potion_rects, vision_potion_rects = maze_view.draw_inventory(screen)
        # exit_rect = maze_view.draw_exit(room)

        # maze_view.draw_vision()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            handle_event(event, )
        pygame.display.update()
    pygame.quit()
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
        self.rect.topleft = (Hero.get_instance().get_x() - maze_view.get_camera_offset()[0], Hero.get_instance().get_y() - maze_view.get_camera_offset()[1])

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
    global toolbar_rects
    global potion_time
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
        player.down = False
        player.up = False
        player.right = False
        player.left = False
        Battle_Controller.run(room.get_monster())
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
                    health_potion_rects.pop(i)
                    break
            for i in range(len(vision_potion_rects)):
                if vision_potion_rects[i].collidepoint(event.pos):
                    Inventory.get_instance().drink_vision_potion()
                    potion_time = 600
                    vision_potion_rects.pop(i)
                    break

def get_current_room():
    x = Hero.get_instance().get_x()
    y = Hero.get_instance().get_y()
    room_x = x//maze_view.room_size
    room_y = y//maze_view.room_size
    return array[room_x][room_y]