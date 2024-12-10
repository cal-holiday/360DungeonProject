import pygame
pygame.init()

FONT = "8-bit-pusab.ttf"
COLOR = (211,191,143)


screen = pygame.display.set_mode((10,4))
header_font = pygame.font.Font(FONT, 25)
font = pygame.font.Font(FONT, 20)


Clock = pygame.time.Clock()

def setScreen(the_screen):
    screen = the_screen

def draw_header(text, x,y):
    img = header_font.render(text, True, COLOR)
    screen.blit(img,(x,y))

def draw_text(text, x, y):
    img = font.render(text, True, COLOR)
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
    text_surface = font.render(text, True, COLOR)
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


