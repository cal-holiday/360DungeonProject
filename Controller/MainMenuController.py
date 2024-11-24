from View import MainMenuView
from View import Choose_Hero
import pygame

run = True

while run:
    MainMenuView.screen.fill((234, 165, 108))
    MainMenuView.draw_scaled_image("dungeonBackground.png", 0, 0, 810, 810)
    MainMenuView.draw_scaled_image("banner.png", 155, 80, 500, 150)
    MainMenuView.draw_header("Dungeon Adventure", 197, 120)
    MainMenuView.draw_button("button.png", "New Game", 300, 300, 210, 50)
    MainMenuView.draw_button("button.png", "Load Game", 300, 370, 210, 50)
    MainMenuView.draw_button("button.png", "How to play", 300, 440, 210, 50)
    quit_button = MainMenuView.draw_button("button.png", "Quit", 300, 510, 210, 50)

    if(quit_button == True):
        run = False

    if():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
