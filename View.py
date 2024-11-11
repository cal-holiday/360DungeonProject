import pygame
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dungeon Adventure')

clock = pygame.time.Clock()
FPS = 60

run = True
while run:
    clock.tick(FPS)

