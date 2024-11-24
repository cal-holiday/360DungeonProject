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

def draw_scaled_image(img, x, y, width, height):
    original_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(original_img, (width, height))
    screen.blit(scaled_img, (x, y))

def draw_button(img, text, x, y, width, height):
    # Load the button image
    button_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(button_img, (width, height))
    button_rect = scaled_img.get_rect(topleft=(x, y))

    # Render the text
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=button_rect.center)

    # Draw the button
    screen.blit(scaled_img, button_rect)
    screen.blit(text_surface, text_rect)

    # Check if the button is clicked
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if button_rect.collidepoint(mouse_pos) and mouse_click[0]:
        return True  # Button is clicked

    return False

while True:
    screen.fill((234,165,108))
    draw_scaled_image("dungeonBackground.png", 0, 0, 810, 810)
    draw_header("Dungeon Adventure", 70, 50)
    draw_button("mainMenuButton.png","New Game",300,300,210,50)
    draw_button("mainMenuButton.png","Load Game",300,370,210,50)
    draw_button("mainMenuButton.png","How to play",300,440,210,50)
    draw_button("mainMenuButton.png","Quit",300,510,210,50)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    Clock.tick(60)
