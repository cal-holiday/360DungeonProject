import pygame

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
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Hero.get_instance().get_image())
        self.rect = self.image.get_rect()
        self.rect.topleft = (Hero.get_instance().get_x(), Hero.get_instance().get_y())

    def move(self):
        hero_x = Hero.get_instance().get_x()
        hero_y = Hero.get_instance().get_y()
        if self.rect.colliderect(potion_rect):
            pygame.event.post(pygame.event.Event(GET_POTION))
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
        self.rect.topleft = (Hero.get_instance().get_x(), Hero.get_instance().get_y())

    def collide_down(self):
        for rect in room_rects:
            if self.rect.colliderect(rect) and self.rect.bottom <= rect.top + 5:
                return True
        return False

    def collide_up(self):
        for rect in room_rects:
            if self.rect.colliderect(rect) and self.rect.top >= rect.bottom - 5:
                return True
        return False

    def collide_right(self):
        for rect in room_rects:
            if self.rect.colliderect(rect) and self.rect.right <= rect.left + 5:
                return True
        return False

    def collide_left(self):
        for rect in room_rects:
            if self.rect.colliderect(rect) and self.rect.left >= rect.right - 5:
                return True
        return False


def handle_event(event):
    global POTION_REMOVED
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


clock = pygame.time.Clock()
FPS = 60
run = True

GET_POTION = pygame.USEREVENT + 1

inventory = Inventory()
room = Room(True, True, True, True, (1,1), HealthPotion(), None)
CharacterFactory.create_hero("TEST", Element.EARTH)
room_rects = View.draw_room(room)
potion_rect = View.draw_potion(room)
print(potion_rect)
Hero.get_instance().set_x(440)
Hero.get_instance().set_y(440)
player = ControllerHero()
POTION_REMOVED = False
while run:
    clock.tick(FPS)
    View.screen.fill(0)
    View.draw_room(room)
    View.draw_potion(room)
    View.draw_hero()


    player.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        handle_event(event)
    pygame.display.update()
pygame.quit()




