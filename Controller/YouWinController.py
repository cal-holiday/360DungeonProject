import pygame

from Controller import ChooseHeroController
from Model.Dungeon import Dungeon
from View import YouWinView as you_win

def run(screen):
    is_running = True
    while is_running:
        you_win.screen.fill((0, 0, 0))
        you_win.draw_scaled_image(screen,'Assets/dungeonBackground.png', 0, 0, 810, 810)
        you_win.draw_scaled_image(screen,'Assets/banner.png', 155, 200, 500, 150)
        you_win.draw_text(screen,"You Win!",260,230)
        you_win.draw_scaled_image(screen,'Assets/treasure_chest.jpg',367,375,75,75)
        new_game = you_win.draw_button(screen,'Assets/button.png',"Play Again",300,500,200,75)
        quit_game = you_win.draw_button(screen,'Assets/button.png',"Quit",300,600,200,75)
        Dungeon.delete_instance()
        if quit_game:
            is_running = False
            pygame.quit()
            exit()
        if new_game:
            pygame.mixer.init()
            pygame.mixer.music.load('Assets/buddy holly 10 12 24.wav')
            pygame.mixer.music.play(loops=-1)
            ChooseHeroController.run(screen)
            is_running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
