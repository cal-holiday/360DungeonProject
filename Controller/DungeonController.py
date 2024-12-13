from random import choice

import pygame

from Controller import BattleController, HowToPlayController, YouWinController, SaveFileController
from Model.Maze import Maze
from View import DungeonView
from Model.Hero import Hero
from Model.Inventory import Inventory

GET_POTION = pygame.USEREVENT + 1
MONSTER_BATTLE = pygame.USEREVENT + 2
EXIT_DUNGEON = pygame.USEREVENT + 3
_potion_removed = False
_monster_defeated = False
_inventory_clicked = False
_map_clicked = False
_run = True
_room_rects = []
_monster_rect = []
_potion_rect = []
_toolbar_rects = []
_health_potion_rects = []
_vision_potion_rects = []
_exit_rect = None
_player = None
_array = []
_potion_time = 0

def run(screen):
    global _monster_rect
    global _exit_rect
    global _room_rects
    global _player
    global _array
    global _toolbar_rects
    global GET_POTION
    global MONSTER_BATTLE
    global EXIT_DUNGEON
    global _run
    global _potion_rect
    global _health_potion_rects
    global _vision_potion_rects
    global _inventory_clicked
    global _map_clicked
    global _potion_time
    _potion_time = 0
    pygame.mixer.init()
    pygame.mixer.music.load('Assets/Goblins_Dance_(Battle).wav')
    pygame.mixer.music.play(loops=-1)
    clock = pygame.time.Clock()
    fps = 60
    GET_POTION = pygame.USEREVENT + 1
    MONSTER_BATTLE = pygame.USEREVENT + 2
    EXIT_DUNGEON = pygame.USEREVENT + 3

    DungeonView.set_up(screen)

    _toolbar_rects = DungeonView.draw_toolbar(screen)
    _health_potion_rects, _vision_potion_rects = DungeonView.draw_inventory(screen)
    _array = Maze.get_instance().get_array()
    if Hero.get_instance().get_x() == -100 and Hero.get_instance().get_y() == -100:
        empty_rooms = []
        for i in range(len(_array)):
            for j in range(len(_array[i])):
                if _array[i][j].get_monster() is None and _array[i][j].get_potion() is None:
                        empty_rooms.append(_array[i][j])
        hero_room = choice(empty_rooms)
        x = hero_room.get_location()[0] * DungeonView.ROOM_SIZE + DungeonView.ROOM_SIZE * .5
        y = hero_room.get_location()[1] * DungeonView.ROOM_SIZE + DungeonView.ROOM_SIZE * .5
        Hero.get_instance().set_x(int(x))
        Hero.get_instance().set_y(int(y))
    print(Hero.get_instance().get_x(), Hero.get_instance().get_y())
    _player = ControllerHero(DungeonView.draw_hero(screen))
    _player.rect.topleft = (Hero.get_instance().get_x() - DungeonView.get_camera_offset()[0],
                            Hero.get_instance().get_y() - DungeonView.get_camera_offset()[1])
    _inventory_clicked = False

    while _run:
        pygame.mixer.unpause()
        clock.tick(fps)
        screen.fill(0)
        _room_rects = []
        _monster_rect = []
        _potion_rect = []
        _exit_rect = None
        for i in range(len(_array)):
            for j in range(len(_array[i])):
                _room_rects.append(DungeonView.draw_room(screen, _array[i][j]))
                possible_monster = DungeonView.draw_monster(screen, _array[i][j])
                if not possible_monster is None:
                    _monster_rect.append(possible_monster)
                possible_potion = DungeonView.draw_potion(screen, _array[i][j])
                if not possible_potion is None:
                    _potion_rect.append(possible_potion)
                possible_exit = DungeonView.draw_exit(screen, _array[i][j])
                if not possible_exit is None:
                    _exit_rect = possible_exit

        _player.move()
        DungeonView.draw_hero(screen)
        if _potion_time == 0:
            DungeonView.draw_vision(screen)
        else:
            _potion_time -= 1


        if _inventory_clicked:
            DungeonView.draw_inventory(screen)
            _health_potion_rects, _vision_potion_rects = DungeonView.draw_inventory(screen)
        if _map_clicked:
            DungeonView.draw_mini_map(screen)

        _toolbar_rects = DungeonView.draw_toolbar(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _run = False
            handle_event(screen, event)

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

        for rect in _potion_rect:
            if self.rect.colliderect(rect):
                pygame.event.post(pygame.event.Event(GET_POTION))
                break
        for rect in _monster_rect:
            if self.rect.colliderect(rect):
                pygame.event.post(pygame.event.Event(MONSTER_BATTLE))
                break
        if _exit_rect is not None and self.rect.colliderect(_exit_rect):
            pygame.event.post(pygame.event.Event(EXIT_DUNGEON))
        if self.down and not self.collide_down():
            Hero.get_instance().set_y(hero_y + 5)
        if self.up and not self.collide_up():
            Hero.get_instance().set_y(hero_y - 5)
        if self.right and not self.collide_right():
            Hero.get_instance().set_x(hero_x + 5)
        if self.left and not self.collide_left():
            Hero.get_instance().set_x(hero_x - 5)
        self.rect.topleft = (Hero.get_instance().get_x() - DungeonView.get_camera_offset()[0], Hero.get_instance().get_y() - DungeonView.get_camera_offset()[1])

    def collide_down(self):
        for rect_list in _room_rects:
            for rect in rect_list:
                if self.rect.colliderect(rect) and self.rect.bottom <= rect.top + 5:
                    return True
        return False

    def collide_up(self):
        for rect_list in _room_rects:
            for rect in rect_list:
                if self.rect.colliderect(rect) and self.rect.top >= rect.bottom - 5:
                    return True
        return False

    def collide_right(self):
        for rect_list in _room_rects:
            for rect in rect_list:
                if self.rect.colliderect(rect) and self.rect.right <= rect.left + 5:
                    return True
        return False

    def collide_left(self):
        for rect_list in _room_rects:
            for rect in rect_list:
                if self.rect.colliderect(rect) and self.rect.left >= rect.right - 5:
                    return True
        return False


def handle_event(screen, event):
    global _run
    global _inventory_clicked
    global _map_clicked
    global _toolbar_rects
    global _potion_time
    room = get_current_room()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
            _player.down = True
        if event.key == pygame.K_w:
            _player.up = True
        if event.key == pygame.K_d:
            _player.right = True
        if event.key == pygame.K_a:
            _player.left = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_s:
            _player.down = False
        if event.key == pygame.K_w:
            _player.up = False
        if event.key == pygame.K_d:
            _player.right = False
        if event.key == pygame.K_a:
            _player.left = False
    if event.type == GET_POTION:
        Inventory.get_instance().add(room.get_potion())
        room.set_potion(None)
    if event.type == MONSTER_BATTLE:
        _player.down = False
        _player.up = False
        _player.right = False
        _player.left = False
        BattleController.run(room.get_monster())
        room.set_monster(None)
    if event.type == EXIT_DUNGEON:
        YouWinController.run(screen)
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Check if a hero is clicked
        for i in range(len(_toolbar_rects)):
            if _toolbar_rects[i].collidepoint(event.pos):
                if i == 0:
                    if _inventory_clicked:
                        _inventory_clicked = False
                    else:
                        _inventory_clicked = True

                elif i == 1:
                    if _map_clicked:
                        _map_clicked = False
                    else:
                        _map_clicked = True
                        _player.down = False
                        _player.up = False
                        _player.right = False
                        _player.left = False
                elif i == 2:
                    SaveFileController.run()
                elif i == 3:
                    HowToPlayController.run()
                else:
                    _run = False
            for i in range(len(_health_potion_rects)):
                if _health_potion_rects[i].collidepoint(event.pos):
                    Inventory.get_instance().drink_health_potion()
                    _health_potion_rects.pop(i)
                    break
            for i in range(len(_vision_potion_rects)):
                if _vision_potion_rects[i].collidepoint(event.pos):
                    Inventory.get_instance().drink_vision_potion()
                    _potion_time = 600
                    _vision_potion_rects.pop(i)
                    break

def get_current_room():
    x = Hero.get_instance().get_x()
    y = Hero.get_instance().get_y()
    room_x = x//DungeonView.ROOM_SIZE
    room_y = y//DungeonView.ROOM_SIZE
    _array[room_x][room_y].set_hero_has_visited(True)
    return _array[room_x][room_y]