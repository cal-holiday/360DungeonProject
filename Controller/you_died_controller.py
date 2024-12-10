import pygame
from View import you_died_view as you_died

def run(theScreen):
    is_running = True
    screen = theScreen
    while is_running:
        you_died.setScreen(screen)
        you_died.screen.fill((0, 0, 0))
        you_died.draw_text("You Died :(",175,100)
        #you_died.draw_button()
        you_died.draw_image()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
