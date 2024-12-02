import pygame
from View import Battle_View as View


def run(screen):
    View.pass_screen(screen)
    isRunning = True
    clock = pygame.time.Clock()
    while isRunning:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                exit()


        # Update the display
        pygame.display.update()
        clock.tick(60)


