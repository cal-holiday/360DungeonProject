import pygame
import View
from Direction import Direction
from Element import Element
from CharacterFactory import CharacterFactory
from Hero import Hero
class Controller:
    def __init__(self, hero):
        self.hero = hero
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            #fix this!
            View.run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.hero.set_direction(Direction.NORTH)
                self.hero.set_y(self.hero.get_y + 5)
            if event.key == pygame.K_s:
                self.hero.set_direction(Direction.SOUTH)
                self.hero.set_y(self.hero.get_y - 5)
            if event.key == pygame.K_d:
                self.hero.set_direction(Direction.EAST)
                self.hero.set_x(self.hero.get_x + 5)
            if event.key == pygame.K_a:
                self.hero.set_direction(Direction.WEST)
                self.hero.set_x(self.hero.get_x - 5)

    hero = CharacterFactory.create_hero("TEST", Element.EARTH)
    clock = pygame.time.Clock()
    FPS = 60
    run = True
    while run:
        clock.tick(FPS)
        View.screen.fill(0)
        View.draw_hero(hero)

        for event in pygame.event.get():
            handle_event(event)

        pygame.display.update()
    pygame.quit()




