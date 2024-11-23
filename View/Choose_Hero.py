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

def draw_text_field(x, y, width, height, placeholder):
    # Initial text and state
    text = ""
    active = False  # Tracks if the text field is active (clicked on)
    placeholder_active = True  # Tracks if the placeholder text is displayed

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the text field is clicked
                if x < pygame.mouse.get_pos()[0] < x + width and y < pygame.mouse.get_pos()[1] < y + height:
                    active = True
                    placeholder_active = False  # Hide placeholder when clicked
                else:
                    active = False  # Deactivate if clicked outside

            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    # Remove the last character
                    text = text[:-1]
                elif len(text) < 20:  # Limit character input
                    text += event.unicode

        # Draw the text field box
        pygame.draw.rect(screen, (255,255,255), (x, y, width, height), border_radius=5)

        # Render text or placeholder
        text_surface = font.render(text if not placeholder_active else placeholder, True, BLACK if not placeholder_active else (150, 150, 150))
        screen.blit(text_surface, (x + 10, y + (height // 2 - text_surface.get_height() // 2)))

        # Highlight the box if active
        if active:
            pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height), 2)

        # Update the display
        pygame.display.update()

        # Return the entered text when Enter is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and active:
            return text

while True:
    screen.fill((234,165,108))
    draw_scaled_image("banner.png", 45, 20, 700, 150)
    draw_header("Choose Your Hero", 90, 50)

    draw_button("button.png", "confirm", 500, 200, 200,80)

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
