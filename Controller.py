import pygame
import View
from Direction import Direction
from Element import Element
from CharacterFactory import CharacterFactory
from Hero import Hero
from Room import Room

room = Room(True, True, True, True, (1,1), False, False)
hero = CharacterFactory.create_hero("TEST", Element.EARTH)
def move_hero(left, right, up, down):
    hero_x = hero.get_x()
    hero_y = hero.get_y()
    if down:
        hero.set_direction(Direction.SOUTH)
        hero.set_y(hero_y + 5)
    if up:
        hero.set_direction(Direction.NORTH)
        hero.set_y(hero_y - 5)
    if right:
        hero.set_direction(Direction.EAST)
        hero.set_x(hero_x + 5)
    if left:
        hero.set_direction(Direction.WEST)
        hero.set_x(hero_x - 5)


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
    hero_rect = View.draw_hero(hero)
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




