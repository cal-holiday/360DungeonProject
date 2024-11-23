import pygame
from Model import *
pygame.init()

SCREEN_WIDTH = 810
SCREEN_HEIGHT = 810
FONT = "8-bit-pusab.ttf"
BLACK = (0,0,0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
header_font = pygame.font.Font(FONT, 40)
font = pygame.font.Font(FONT, 20)
pygame.display.set_caption("Main Menu")

Clock = pygame.time.Clock()

def draw_header(text, x,y):
    img = header_font.render(text, True, BLACK)
    screen.blit(img,(x,y))

def draw_text(text, x, y):
    img = font.render(text, True, BLACK)
    screen.blit(img, (x,y))


def draw_image(img, x, y):
    screen.blit((pygame.image.load(img).convert()), (x,y))
while True:
    screen.fill((234,165,108))
    draw_header("Dungeon Adventure", 70, 50)
    draw_text("New Game",410,300)
    draw_text("Load Game",410,350)
    draw_text("How to play",410,400)
    draw_text("Quit",410,450)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    Clock.tick(60)
