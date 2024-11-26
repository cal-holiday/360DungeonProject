import pygame
pygame.init()

SCREEN_WIDTH = 810
SCREEN_HEIGHT = 810
FONT = "8-bit-pusab.ttf"
BLACK = (0,0,0)
WHITE = (255,255,255)

screen = pygame.display.set_mode((10,4))
font = pygame.font.Font(FONT, 20)
button_font = pygame.font.Font(FONT, 18)
text_font = pygame.font.Font(FONT, 25)
pygame.display.set_caption("Battle")

def pass_screen(passed_screen):
    screen = passed_screen

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x,y))

def draw_result(text, x, y):
    img = text_font.render(text, True, WHITE)
    screen.blit(img, (x,y))


def draw_image(img, x, y, width, height):
    original_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(original_img, (width, height))
    screen.blit(scaled_img, (x, y))

def draw_button(img_path, text, x, y, width, height):
    # Load and scale the button image
    button_img = pygame.image.load(img_path).convert()
    scaled_img = pygame.transform.scale(button_img, (width, height))
    button_rect = scaled_img.get_rect(topleft=(x, y))

    # Render the text
    text_surface = button_font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(scaled_img, button_rect)
    screen.blit(text_surface, text_rect)

    # Return the button rectangle for external use
    return button_rect
