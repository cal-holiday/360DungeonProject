import pygame
from sys import exit
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
    scaled_img = pygame.transform.scale(button_img, (width,height))
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

def draw_text_field(x, y, width, height, box_color, border_color, placeholder, active, text):
    # Draw the text field box
    pygame.draw.rect(screen, box_color, (x, y, width, height), border_radius=5)
    pygame.draw.rect(screen, border_color if active else (200, 200, 200), (x, y, width, height), 2)

    # Render the placeholder or user text
    display_text = placeholder if not text and not active else text
    text_surface = font.render(display_text, True, BLACK if text or active else (150, 150, 150))
    screen.blit(text_surface, (x + 10, y + (height // 2 - text_surface.get_height() // 2)))

while True:
    screen.fill((234,165,108))
    draw_scaled_image("banner.png", 45, 20, 700, 150)
    draw_header("Choose Your Hero", 90, 50)

    draw_button("button.png", "confirm", 500, 230, 200,80)

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

    draw_text_field(100, 250, 300, 50, WHITE,BLACK,
                    "Name Your Hero", False, "" )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    Clock.tick(60)
