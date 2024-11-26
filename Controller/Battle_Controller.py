import pygame

from Model.CharacterFactory import CharacterFactory
from Model.Element import Element
from Model.Hero import Hero
from View import Battle_View as View
from View.Battle_View import draw_image


def run(screen,monster):
    View.pass_screen(screen)
    isRunning = True
    clock = pygame.time.Clock()
    hero = Hero.get_instance()
    white_rect = pygame.Rect(20, 470, 770, 200)  # Start with dummy coordinates
    health_rect = pygame.Rect(80, 20, 150, 25)
    health_rect_outline = pygame.Rect(80, 20, 150, 25)
    while isRunning:
        screen.fill((0,0,0))
        View.draw_image("battle_background.jpg", 0, 0, 810, 450)

        pygame.draw.rect(screen, (34, 139, 34), health_rect)
        pygame.draw.rect(screen, (255,255,255), health_rect_outline, 3)
        View.draw_text("HP", 20, 15)
        View.draw_text(str(hero.get_hp()) + "/" + str(hero.get_max_hp()), 250, 15)
        View.draw_text("Agility:  " + str(hero.get_agility()), 20, 60)


        View.draw_image(hero.get_image(), 75, 330, 90, 90)
        View.draw_image(monster.get_image(), 400, 330, 90, 90)

        pygame.draw.rect(screen, (255, 255, 255), white_rect, 5)



        View.draw_button()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                exit()


        # Update the display
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    SCREEN_WIDTH = 810
    SCREEN_HEIGHT = 810
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    monster = CharacterFactory.create_monster(Element.FIRE)
    CharacterFactory.create_hero("chill guy", Element.EARTH)
    run(screen, monster)
