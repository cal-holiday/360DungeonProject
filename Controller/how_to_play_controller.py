
from View import how_to_play_view as help_view
import pygame

pygame.init()
Clock = pygame.time.Clock()

def run():
    is_running = True
    while is_running:
        help_view.draw_scaled_image("panel.png",0,0,help_view.SCREEN_WIDTH,help_view.SCREEN_HEIGHT)
        help_view.draw_header("HOW TO PLAY",150,50)
        pygame.display.set_caption("How To Play")

        exit_button = help_view.draw_button("buttonSquare_beige.png","x",760,0,50,50)

        if exit_button:
            is_running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
