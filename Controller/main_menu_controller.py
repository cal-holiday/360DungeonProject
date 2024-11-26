from View import main_menu_view
from Controller import Choose_Hero_Controller
import pygame

def run(theScreen):
    is_running = True
    screen = theScreen
    while is_running:
        main_menu_view.setScreen(screen)
        main_menu_view.screen.fill((234, 165, 108))
        main_menu_view.draw_scaled_image("dungeonBackground.png", 0, 0, 810, 810)
        main_menu_view.draw_scaled_image("banner.png", 155, 80, 500, 150)
        main_menu_view.draw_header("Dungeon Adventure", 197, 120)
        pygame.display.set_caption("Main Menu")
        new_game = main_menu_view.draw_button("button.png", "New Game", 300, 300, 210, 50)
        load_game = main_menu_view.draw_button("button.png", "Load Game", 300, 370, 210, 50)
        rules = main_menu_view.draw_button("button.png", "How to play", 300, 440, 210, 50)
        quit_game = main_menu_view.draw_button("button.png", "Quit", 300, 510, 210, 50)

        if(quit_game):
            is_running = False

        if(new_game):
            Choose_Hero_Controller.run(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

