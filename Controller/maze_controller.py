import pygame

from Model.Pillar import AbstractionPillar, PolymorphismPillar, InheritancePillar, EncapsulationPillar
from Model.Potion import HealthPotion, VisionPotion
from View import maze_view
from Model.Direction import Direction
from Model.Element import Element
from Model.CharacterFactory import CharacterFactory
from Model.Room import Room
from Model.Hero import Hero
from Model.Inventory import Inventory
from View.maze_view import draw_inventory

GET_POTION = pygame.USEREVENT + 1
MONSTER_BATTLE = pygame.USEREVENT + 2
EXIT_DUNGEON = pygame.USEREVENT + 3
POTION_REMOVED = False
MONSTER_DEFEATED = False
INVENTORY_CLICKED = False
RUN = True


def run(screen):
    global RUN
    clock = pygame.time.Clock()
    fps = 60

    monster = CharacterFactory.create_monster(Element.EARTH)
    current_room = Room(False, False, False, False, (1, 1), HealthPotion(), None)
    current_room.set_has_exit(True)

    inventory = Inventory()
    inventory.add(AbstractionPillar())
    inventory.add(PolymorphismPillar())
    inventory.add(InheritancePillar())
    inventory.add(HealthPotion())
    inventory.add(HealthPotion())
    inventory.add(VisionPotion())

    Hero.get_instance().set_x(10)
    Hero.get_instance().set_y(10)
    player = ControllerHero(maze_view.draw_hero(screen))
    controller_room = ControllerRoom(screen, current_room)
    while RUN:
        global INVENTORY_CLICKED
        clock.tick(fps)
        screen.fill(0)
        maze_view.draw_room(screen, current_room)
        maze_view.draw_potion(screen, current_room)
        maze_view.draw_monster(screen, current_room)
        maze_view.draw_exit(screen, current_room)
        maze_view.draw_hero(screen)
        maze_view.draw_toolbar(screen)
        if INVENTORY_CLICKED:
            maze_view.draw_inventory(screen)

        player.move(controller_room)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            handle_event(player, event, current_room, controller_room)
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

    def move(self, room):
        hero_x = Hero.get_instance().get_x()
        hero_y = Hero.get_instance().get_y()
        if room.potion_rect is not None and self.rect.colliderect(room.potion_rect):
            pygame.event.post(pygame.event.Event(GET_POTION))
        if room.monster_rect is not None and self.rect.colliderect(room.monster_rect):
            pygame.event.post(pygame.event.Event(MONSTER_BATTLE))
        if room.exit_rect is not None and self.rect.colliderect(room.exit_rect):
            pygame.event.post(pygame.event.Event(EXIT_DUNGEON))
        if self.down and not self.collide_down(room):
            Hero.get_instance().set_direction(Direction.SOUTH)
            Hero.get_instance().set_y(hero_y + 5)
        if self.up and not self.collide_up(room):
            Hero.get_instance().set_direction(Direction.NORTH)
            Hero.get_instance().set_y(hero_y - 5)
        if self.right and not self.collide_right(room):
            Hero.get_instance().set_direction(Direction.EAST)
            Hero.get_instance().set_x(hero_x + 5)
        if self.left and not self.collide_left(room):
            Hero.get_instance().set_direction(Direction.WEST)
            Hero.get_instance().set_x(hero_x - 5)
        self.rect.topleft = (Hero.get_instance().get_x(), Hero.get_instance().get_y())

    def collide_down(self, room):
        for rect in room.room_rects:
            if self.rect.colliderect(rect) and self.rect.bottom <= rect.top + 5:
                return True
        return False

    def collide_up(self, room):
        for rect in room.room_rects:
            if self.rect.colliderect(rect) and self.rect.top >= rect.bottom - 5:
                return True
        return False

    def collide_right(self, room):
        for rect in room.room_rects:
            if self.rect.colliderect(rect) and self.rect.right <= rect.left + 5:
                return True
        return False

    def collide_left(self, room):
        for rect in room.room_rects:
            if self.rect.colliderect(rect) and self.rect.left >= rect.right - 5:
                return True
        return False
class ControllerRoom():
    def __init__(self, screen, room):
        self.room = room
        self.floor_rect, self.room_rects = maze_view.draw_room(screen, self.room)
        self.potion_rect = maze_view.draw_potion(screen, self.room)
        self.monster_rect = maze_view.draw_monster(screen, room)
        self.toolbar_rects = maze_view.draw_toolbar(screen)
        self.exit_rect = maze_view.draw_exit(screen, room)
        self.health_potion_rect, self.vision_potion_rect = maze_view.draw_inventory(screen)



def handle_event(player, event, room, controller_room):
    global POTION_REMOVED
    global MONSTER_DEFEATED
    global RUN
    global INVENTORY_CLICKED
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
    if event.type == GET_POTION and not POTION_REMOVED:
        POTION_REMOVED = True
        Inventory.get_instance().add(room.get_potion())
        room.set_potion(None)
    if event.type == MONSTER_BATTLE and not MONSTER_DEFEATED:
        MONSTER_DEFEATED = True
        #jump to battle here
        room.set_monster(None)
    if event.type == EXIT_DUNGEON:
        print("END Game")
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Check if a hero is clicked
        for i in range(len(controller_room.toolbar_rects)):
            if controller_room.toolbar_rects[i].collidepoint(event.pos):
                if i == 0:
                    if INVENTORY_CLICKED:
                        INVENTORY_CLICKED = False
                    else:
                        INVENTORY_CLICKED = True
                        print("Inventory")
                elif i == 1:
                    print("Map")
                elif i == 2:
                    print("Save")
                elif i == 3:
                    print("Help")
                else:
                    RUN = False
        for i in range(len(controller_room.health_potion_rect)):
            if controller_room.health_potion_rect[i].collidepoint(event.pos):
                Inventory.get_instance().drink_potion(Inventory.get_instance().get_health_potions()[0])
        for i in range(len(controller_room.vision_potion_rect)):
            if controller_room.vision_potion_rect[i].collidepoint(event.pos):
                Inventory.get_instance().drink_potion(Inventory.get_instance().get_vision_potions()[0])
