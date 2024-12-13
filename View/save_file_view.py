import pygame
pygame.init()

SCREEN_WIDTH = 810
SCREEN_HEIGHT = 300
FONT = "8-bit-pusab.ttf"
COLOR = (87,57,46)
WHITE = (255,255,255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(FONT, 20)
header_font = pygame.font.Font(FONT, 30)

def draw_header(text, x, y):
    """Draws a header text on the screen."""
    img = header_font.render(text, True, COLOR)
    screen.blit(img, (x, y))

def draw_text(text, x, y):
    """Draws regular text on the screen."""
    img = font.render(text, True, COLOR)
    screen.blit(img, (x, y))

def draw_scaled_image(img, x, y, width, height):
    """Draws a scaled image on the screen."""
    original_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(original_img, (width, height))
    screen.blit(scaled_img, (x, y))

def draw_button(img, text, x, y, width, height):
    """Draws a button with an image and text and checks if it's clicked."""
    # Load the button image and scale it
    button_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(button_img, (width, height))
    button_rect = scaled_img.get_rect(topleft=(x, y))

    # Render the button text
    text_surface = font.render(text, True, COLOR)
    text_rect = text_surface.get_rect(center=button_rect.center)

    # Draw the button and its text
    screen.blit(scaled_img, button_rect)
    screen.blit(text_surface, text_rect)

    # Check if the button is clicked
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if button_rect.collidepoint(mouse_pos) and mouse_click[0]:
        return True  # Button is clicked

    return False

def draw_text_field(x, y, width, height, placeholder, active, text):
    """Draws a text field with a placeholder and user input."""
    # Draw the text field box
    pygame.draw.rect(screen, WHITE, (x, y, width, height), border_radius=5)
    pygame.draw.rect(screen, WHITE if active else (200, 200, 200), (x, y, width, height), 2)

    # Render the placeholder or user text
    display_text = placeholder if not text and not active else text
    text_surface = font.render(display_text, True, COLOR if text or active else (150, 150, 150))

    # Center the text both horizontally and vertically within the text field
    text_x = x + (width - text_surface.get_width()) // 2
    text_y = y + (height - text_surface.get_height()) // 2
    screen.blit(text_surface, (text_x, text_y))

