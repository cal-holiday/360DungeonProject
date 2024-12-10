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
reward_font = pygame.font.Font(FONT, 20)
reward_header_font = pygame.font.Font(FONT, 30)
pygame.display.set_caption("Battle")

def pass_screen(passed_screen):
    screen = passed_screen

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x,y))

def draw_result(text, x, y):
    img = text_font.render(text, True, WHITE)
    screen.blit(img, (x,y))

def draw_monster_result(text, x, y):
    img = text_font.render(text, True, (255,0,0))
    screen.blit(img, (x, y))

def draw_image(img, x, y, width, height):
    original_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(original_img, (width, height))
    screen.blit(scaled_img, (x, y))

def draw_rotated_image(img, x, y, width, height, degree):
    original_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(original_img, (width, height))
    new_img = pygame.transform.rotate(scaled_img, degree)
    screen.blit(new_img, (x, y))

def draw_button(img, text, x, y, width, height):
    # Load the button image
    button_img = pygame.image.load(img).convert()
    scaled_img = pygame.transform.scale(button_img, (width, height))
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


def reward_text(text, x, y):
    img = reward_font.render(text, True, (101, 67, 33))
    screen.blit(img, (x, y))

def reward_header(text, x, y):
    img = reward_header_font.render(text, True, (101, 67, 33))
    screen.blit(img, (x, y))

def draw_rewards(monster):
    dim_surface = pygame.Surface((screen.get_width(), screen.get_height()))
    dim_surface.set_alpha(200)  # Set transparency
    dim_surface.fill((0, 0, 0))  # Black
    screen.blit(dim_surface, (0, 0))
    rect = pygame.Rect(205, 205, 400, 400)
    pygame.draw.rect(screen, (245, 222, 179), rect)
    reward_header("Rewards", 293, 220)
    three_items = [(230, 350), (350, 350), (470, 350)]
    two_items = [(300, 350), (400, 350)]
    one_item = (350, 350)
    if monster.has_health_potion() and monster.has_vision_potion() and monster.has_pillar():
        draw_image("health_potion.png", three_items[0][0], three_items[0][1], 100, 100)
        draw_image("vision_potion.png", three_items[1][0], three_items[1][1], 100, 100)
        draw_image(monster.get_pillar().get_image(), three_items[2][0], three_items[2][1], 100, 100)
    elif monster.has_health_potion() and monster.has_vision_potion():
        draw_image("health_potion.png", two_items[0][0], two_items[0][1], 100, 100)
        draw_image("vision_potion.png", two_items[1][0], two_items[1][1], 100, 100)
    elif monster.has_health_potion() and monster.has_pillar():
        draw_image("health_potion.png", two_items[0][0], two_items[0][1], 100, 100)
        draw_image(monster.get_pillar().get_image(), two_items[1][0], two_items[1][1], 100, 100)
    elif monster.has_vision_potion() and monster.has_pillar():
        draw_image("vision_potion.png", two_items[0][0], two_items[0][1], 100, 100)
        draw_image(monster.get_pillar().get_image(), two_items[1][0], two_items[1][1], 100, 100)
    elif monster.has_health_potion():
        draw_image("health_potion.png", one_item[0], one_item[1], 100, 100)
    elif monster.has_vision_potion():
        draw_image("vision_potion.png", one_item[0], one_item[1], 100, 100)
    elif monster.has_pillar():
        draw_image(monster.get_pillar().get_image(), one_item[0], one_item[1], 100, 100)

    draw_button("button.png", "claim", 315, 500, 175, 70)

