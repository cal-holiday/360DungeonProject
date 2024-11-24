import pygame
pygame.init()

SCREEN_WIDTH = 810
SCREEN_HEIGHT = 810
FONT = "8-bit-pusab.ttf"
BLACK = (0,0,0)
WHITE = (255,255,255)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
header_font = pygame.font.Font(FONT, 40)
font = pygame.font.Font(FONT, 20)
pygame.display.set_caption("Choose Your Hero")


def draw_header(text, x,y):
    img = header_font.render(text, True, WHITE)
    screen.blit(img,(x,y))

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
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
    scaled_img = pygame.transform.scale(button_img, (width,height))
    button_rect = scaled_img.get_rect(topleft=(x, y))

    # Render the text
    text_surface = font.render(text, True, WHITE)
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

def draw_text_field(x, y, width, height, placeholder, active, text):
    # Draw the text field box
    pygame.draw.rect(screen, WHITE, (x, y, width, height), border_radius=5)
    pygame.draw.rect(screen, WHITE if active else (200, 200, 200), (x, y, width, height), 2)

    # Render the placeholder or user text
    display_text = placeholder if not text and not active else text
    text_surface = font.render(display_text, True, BLACK if text or active else (150, 150, 150))
    screen.blit(text_surface, (x + 10, y + (height // 2 - text_surface.get_height() // 2)))


