import pygame
from View import View
from Model.Direction import Direction
from Model.Element import Element
from Model.CharacterFactory import CharacterFactory
from Model.Room import Room
from Model.Hero import Hero

class ControllerHero(pygame.sprite.Sprite):
    left = False
    right = False
    up = False
    down = False
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Hero.get_instance().get_image())
        self.rect = self.image.get_rect()

    def move(self):
        hero_x = Hero.get_instance().get_x()
        hero_y = Hero.get_instance().get_y()
        if self.down:
            Hero.get_instance().set_direction(Direction.SOUTH)
            Hero.get_instance().set_y(hero_y + 5)
        if self.up:
            Hero.get_instance().set_direction(Direction.NORTH)
            Hero.get_instance().set_y(hero_y - 5)
        if self.right:
            Hero.get_instance().set_direction(Direction.EAST)
            Hero.get_instance().set_x(hero_x + 5)
        if self.left:
            Hero.get_instance().set_direction(Direction.WEST)
            Hero.get_instance().set_x(hero_x - 5)



def handle_event(event):
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



clock = pygame.time.Clock()
FPS = 60
run = True
room = Room(True, True, True, True, (1,1), False, False)
CharacterFactory.create_hero("TEST", Element.EARTH)
room_rects = View.draw_room(room, 300)

player = ControllerHero()

while run:
    clock.tick(FPS)
    View.screen.fill(0)
    View.draw_room(room, 300)
    View.draw_hero(Hero.get_instance())

    player.move()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        handle_event(event)
    pygame.display.update()
pygame.quit()




