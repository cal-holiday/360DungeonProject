from View import MainMenuView
from Controller import ChooseHeroController, YouWinController, LoadController
from Controller import HowToPlayController
import pygame
pygame.mixer.init()
pygame.mixer.music.load('Assets/buddy holly 10 12 24.wav')
pygame.mixer.music.play(loops=-1)


def run(screen):
    is_running = True
    while is_running:
        screen.fill((234, 165, 108))
        MainMenuView.draw_scaled_image(screen,'Assets/dungeonBackground.png', 0, 0, 810, 810)
        MainMenuView.draw_scaled_image(screen,'Assets/banner.png', 155, 80, 500, 150)
        MainMenuView.draw_header(screen,"Dungeon Adventure", 197, 120)
        new_game = MainMenuView.draw_button(screen,'Assets/button.png', "New Game", 300, 300, 210, 50)
        load_game = MainMenuView.draw_button(screen,'Assets/button.png', "Load Game", 300, 370, 210, 50)
        rules = MainMenuView.draw_button(screen,'Assets/button.png', "How to play", 300, 440, 210, 50)
        quit_game = MainMenuView.draw_button(screen,'Assets/button.png', "Quit", 300, 510, 210, 50)

        if(quit_game):
            is_running = False

        if(new_game):
            ChooseHeroController.run(screen)

        if(rules):
            HowToPlayController.run()

        if(load_game):
            LoadController.run(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

