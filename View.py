import pygame

from CharacterFactory import CharacterFactory
from Controller import Controller
from Element import Element
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dungeon Adventure')

clock = pygame.time.Clock()
FPS = 60

hero = CharacterFactory.create_hero("TEST", Element.EARTH)
def draw_hero(hero):
    screen.blit(hero.getImage(), (hero.get_x(),hero.get_y()))
controller = Controller(hero)
run = True
while run:
    clock.tick(FPS)
    screen.fill(0)
    draw_hero(hero)

    for event in pygame.event.get():
        controller.handle_event(event)

    pygame.display.update()
pygame.quit()
