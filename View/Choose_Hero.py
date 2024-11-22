import pygame
from sys import exit
pygame.init()

SCREEN_WIDTH = 810
SCREEN_HEIGHT = 810


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
header_font = pygame.font.SysFont("Times New Roman", 70, bold = True)
font = pygame.font.SysFont("Times New Roman", 40)
pygame.display.set_caption("Choose Your Hero")
Clock = pygame.time.Clock()

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x,y))
while True:
    screen.fill((183,108,43))
    draw_text("Choose Your Hero", header_font, (0,0,0), 140, 100)
    draw_text("Health:", font, (0,0,0), 575, 500)
    draw_text("Agility:", font, (0, 0, 0), 570, 560)
    draw_text("Element:", font, (0, 0, 0), 550, 620)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    Clock.tick(60)
