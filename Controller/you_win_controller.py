import pygame

from Model.Hero import Hero
from View import you_win_view as you_win

def run(theScreen):
    #hero = Hero.get_instance()
    is_running = True
    screen = theScreen
    while is_running:
        you_win.setScreen(screen)
        you_win.screen.fill((0, 0, 0))
        you_win.draw_scaled_image("dungeonBackground.png", 0, 0, 810, 810)
        you_win.draw_scaled_image("banner.png", 155, 200, 500, 150)
        you_win.draw_text("You Win!",260,230)
        new_game = you_win.draw_button("button.png","Play Again",300,500,200,75)
        quit_game = you_win.draw_button("button.png","Quit",300,600,200,75)

        if (quit_game):
            is_running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
