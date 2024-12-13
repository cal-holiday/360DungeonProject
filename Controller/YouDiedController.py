import pygame

from Controller import ChooseHeroController
from Model.Dungeon import Dungeon
from Model.Hero import Hero
from View import YouDiedView as you_died

def run(screen):
    hero = Hero.get_instance()
    is_running = True
    screen = screen
    while is_running:
        you_died.screen.fill((0, 0, 0))
        you_died.draw_text(screen,"You Died :(",175,100)
        new_game = you_died.draw_button(screen,'Assets/button.png',"New Game",300,500,200,75)
        quit_game = you_died.draw_button(screen,'Assets/button.png',"Quit",300,600,200,75)
        you_died.draw_rotated_image(screen,"Assets/" + hero.get_dead_image(),350,300,100,100,90) #change to hero get instance once its all plugged together
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
