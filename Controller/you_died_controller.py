import pygame

from Model.Hero import Hero
from View import you_died_view as you_died

def run(theScreen):
    #hero = Hero.get_instance()
    is_running = True
    screen = theScreen
    while is_running:
        you_died.setScreen(screen)
        you_died.screen.fill((0, 0, 0))
        you_died.draw_text("You Died :(",175,100)
        new_game = you_died.draw_button("button.png","New Game",300,500,200,75)
        quit_game = you_died.draw_button("button.png","Quit",300,600,200,75)
        you_died.draw_rotated_image("air_hero_dead.png",350,300,100,100,90) #change to hero get instance once its all plugged together

        if (quit_game):
            is_running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
