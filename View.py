import pygame
from Hero import Hero
from Room import Room
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dungeon Adventure')




def draw_hero(hero):
    screen.blit(pygame.image.load(hero.get_image()), (hero.get_x(),hero.get_y()))
def draw_room(room, room_size):
    x = room.get_location()[0] * room_size
    y = room.get_location()[1] * room_size




