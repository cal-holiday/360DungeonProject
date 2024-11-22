import pygame
from View import View
from Model.Direction import Direction
from Model.Element import Element
from Model.CharacterFactory import CharacterFactory
from Model.Room import Room
from Model.Hero import Hero

room = Room(True, True, True, True, (1,1), False, False)
CharacterFactory.create_hero("TEST", Element.EARTH)
def move_hero(left, right, up, down):
    hero_x = Hero.get_instance().get_x()
    hero_y = Hero.get_instance().get_y()
    if down:
        Hero.get_instance().set_direction(Direction.SOUTH)
        Hero.get_instance().set_y(hero_y + 5)
    if up:
        Hero.get_instance().set_direction(Direction.NORTH)
        Hero.get_instance().set_y(hero_y - 5)
    if right:
        Hero.get_instance().set_direction(Direction.EAST)
        Hero.get_instance().set_x(hero_x + 5)
    if left:
        Hero.get_instance().set_direction(Direction.WEST)
        Hero.get_instance().set_x(hero_x - 5)


def handle_event(event, left, right, up, down):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
            down = True
        if event.key == pygame.K_w:
            up = True
        if event.key == pygame.K_d:
            right = True
        if event.key == pygame.K_a:
            left = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_s:
            down = False
        if event.key == pygame.K_w:
            up = False
        if event.key == pygame.K_d:
            right = False
        if event.key == pygame.K_a:
            left = False
    return_list = [left, right, up, down]
    return return_list


clock = pygame.time.Clock()
FPS = 60
run = True
left = False
right = False
up = False
down = False
while run:
    clock.tick(FPS)
    View.screen.fill(0)
    room_rects = View.draw_room(room, 300)
    hero_rect = View.draw_hero(Hero.get_instance())
    move_hero(left, right, up, down)
    #work on collisions next
    #if hero_rect.collidelist(room_rects):


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        directions = handle_event(event, left, right, up, down)
        left = directions[0]
        right = directions[1]
        up = directions[2]
        down = directions[3]
    pygame.display.update()
pygame.quit()




