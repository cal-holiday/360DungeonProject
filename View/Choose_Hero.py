import pygame
from sys import exit
pygame.init()

SCREEN_WIDTH = 810
SCREEN_HEIGHT = 810
FONT = "8-bit-pusab.ttf"
BLACK = (0,0,0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
header_font = pygame.font.Font(FONT, 40)
font = pygame.font.Font(FONT, 20)
pygame.display.set_caption("Choose Your Hero")

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
    draw_header("Choose Your Hero", 90, 50)
    draw_text("Health:", 575, 400)
    draw_text("Agility:",570, 475)
    draw_text("Element:", 555, 550)

    draw_image("fire_hero.png", 100, 400)
    draw_text("Fire Hero", 50, 475)
    draw_image("water_hero.png", 350, 600)
    draw_text("Water Hero", 300, 675)
    draw_image("air_hero.png", 100, 600)
    draw_text("Air Hero", 50, 675)
    draw_image("earth_hero.png", 350, 400)
    draw_text("Earth Hero", 300, 475)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    Clock.tick(60)
