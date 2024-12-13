import pygame
import os

from Controller import dungeon_controller
from Controller.SaveLoad import SaveLoad
from Model.CharacterFactory import CharacterFactory
from Model.Dungeon import Dungeon
from Model.Element import Element
from View import LoadView


def run(screen):
    isRunning = True
    file_list = [f for f in os.listdir("LoadGame") if f.endswith(".pickle")]
    selected_file = None  # To track the selected file

    while isRunning:
        # Draw the background and UI
        LoadView.draw_image(screen, "dungeonBackground.png", 0, 0, 810, 810)
        LoadView.draw_image(screen, "banner.png", 45, 20, 700, 150)
        LoadView.draw_header(screen, "Load Game", 300, 70)
        save_button = LoadView.draw_button(screen,"buttonSquare_beige.png", "Confirm", 600, 700, 175, 75)
        # Draw file buttons
        for i, file_name in enumerate(file_list):
            button_clicked = LoadView.draw_button(
                screen, "button.png", file_name[:-7], 250, 300 + i * 100, 300, 50
            )
            if button_clicked:
                pygame.draw.rect(
                    pygame.display.get_surface(),
                    (0, 255, 0),
                    pygame.Rect(240, 295 + i * 100, 320, 60),
                    2)
                selected_file = file_name

        # Handle confirm click
        if selected_file and save_button:
            dungeon_list = SaveLoad.load_game(selected_file[:-7])  # Load the dungeon data
            Dungeon(True, dungeon_list[0], dungeon_list[1], dungeon_list[2])
            dungeon_controller.run(screen)
            isRunning = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
