import pygame
from Controller import main_menu_controller, Choose_Hero_Controller
from Model.CharacterFactory import CharacterFactory
from Model.Element import Element


class StartGame:
    pygame.init()
    SCREEN_WIDTH = 810
    SCREEN_HEIGHT = 810
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #main_menu_controller.run(screen)
    Choose_Hero_Controller.run(screen)