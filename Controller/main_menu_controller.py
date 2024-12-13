from View import main_menu_view
from Controller import Choose_Hero_Controller, you_win_controller
from Controller import how_to_play_controller
from Controller import you_died_controller
import pygame
pygame.mixer.init()
pygame.mixer.music.load("buddy holly 10 12 24.wav")
pygame.mixer.music.play(loops=-1)


def run(screen):
    is_running = True
    while is_running:
        screen.fill((234, 165, 108))
        main_menu_view.draw_scaled_image(screen,"dungeonBackground.png", 0, 0, 810, 810)
        main_menu_view.draw_scaled_image(screen,"banner.png", 155, 80, 500, 150)
        main_menu_view.draw_header(screen,"Dungeon Adventure", 197, 120)
        new_game = main_menu_view.draw_button(screen,"button.png", "New Game", 300, 300, 210, 50)
        load_game = main_menu_view.draw_button(screen,"button.png", "Load Game", 300, 370, 210, 50)
        rules = main_menu_view.draw_button(screen,"button.png", "How to play", 300, 440, 210, 50)
        quit_game = main_menu_view.draw_button(screen,"button.png", "Quit", 300, 510, 210, 50)

        if(quit_game):
            is_running = False

        if(new_game):
            Choose_Hero_Controller.run(screen)

        if(rules):
            how_to_play_controller.run()

        if(load_game):
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

