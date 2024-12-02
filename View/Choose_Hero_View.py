import pygame
pygame.init()

SCREEN_WIDTH = 810
SCREEN_HEIGHT = 810
FONT = "8-bit-pusab.ttf"
BLACK = (0,0,0)
WHITE = (255,255,255)


screen = pygame.display.set_mode((10,4))
header_font = pygame.font.Font(FONT, 40)
font = pygame.font.Font(FONT, 20)
pygame.display.set_caption("Choose Your Hero")

def pass_screen(passed_screen):
    screen = passed_screen

def draw_header(text, x,y):
    img = header_font.render(text, True, WHITE)
    screen.blit(img,(x,y))

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
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
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(scaled_img, button_rect)
    screen.blit(text_surface, text_rect)

    # Return the button rectangle for external use
    return button_rect


def draw_text_field(x, y, width, height, placeholder, active, text):
    # Draw the text field box
    pygame.draw.rect(screen, WHITE, (x, y, width, height), border_radius=5)
    pygame.draw.rect(screen, WHITE if active else (200, 200, 200), (x, y, width, height), 2)

    # Render the placeholder or user text
    display_text = placeholder if not text and not active else text
    text_surface = font.render(display_text, True, BLACK if text or active else (150, 150, 150))

    # Center the text both horizontally and vertically within the text field
    text_x = x + (width - text_surface.get_width()) // 2
    text_y = y + (height - text_surface.get_height()) // 2
    screen.blit(text_surface, (text_x, text_y))



