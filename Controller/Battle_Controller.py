import pygame

from Model.Hero import Hero
from View import Battle_View as View


def run(screen,monster):
    View.pass_screen(screen)
    isRunning = True
    clock = pygame.time.Clock()
    hero = Hero.get_instance()
    while isRunning:
        View.draw_scaled_image("dungeonBackground.png", 0, 0, 810, 810)
        View.draw_scaled_image(Hero.get_instance().get_image(), 100, 300, 90, 90)
        View.draw_scaled_image(monster.get_image(), 500, 300, 90, 90)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                exit()


        # Update the display
        pygame.display.update()
        clock.tick(60)
