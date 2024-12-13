import pygame
import os

from Controller import dungeon_controller
from Controller.SaveLoad import SaveLoad
from Model.CharacterFactory import CharacterFactory
from Model.Dungeon import Dungeon
from Model.Element import Element
from View import Choose_Hero_View as View, LoadView


def run(screen):
    isRunning = True
    clock = pygame.time.Clock()
    file_list = os.listdir("LoadGame")
    while isRunning:
        mouse_pos = pygame.mouse.get_pos()
        # Draw the background and UI
        View.draw_image(screen, "dungeonBackground.png", 0, 0, 810, 810)
        View.draw_image(screen, "banner.png", 45, 20, 700, 150)
        View.draw_header(screen, "Load Game", 225, 50)
        button_list = []
        dungeon_list = []
        confirm_button_visible = False
        confirm_click = False
        for i in range(len(file_list)):
            x = file_list[i].find(".pickle")
            button_list.append(LoadView.draw_button(screen, "button.png", file_list[i][:x],250, 300 + i*100, 300, 50))

        for i in range(len(button_list)):
            if button_list[i]:
                confirm_button_visible = True
                x = file_list[i].find(".pickle")
                dungeon_list = SaveLoad.load_game(file_list[i][:x])

        # Draw the Confirm button (at new position)
        if confirm_button_visible:
            confirm_click = View.draw_button(screen, "button.png", "confirm", 600, 700, 200, 50)

        if confirm_click:
            Dungeon(True, dungeon_list[0], dungeon_list[1], dungeon_list[2])
            dungeon_controller.run(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()