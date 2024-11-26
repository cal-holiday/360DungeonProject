from random import randint

import pygame
import time

from Model.CharacterFactory import CharacterFactory
from Model.Element import Element
from Model.Hero import Hero
from Model.Monster import Monster
from View import Battle_View as View



def run(screen, monster):
    View.pass_screen(screen)
    isRunning = True
    clock = pygame.time.Clock()
    hero = Hero.get_instance()
    in_battle = True

    black_rect = pygame.Rect(25, 475, 760, 190)
    white_rect = pygame.Rect(20, 470, 770, 200)

    health_rect = pygame.Rect(80, 20, 150, 25)
    health_rect_outline = pygame.Rect(80, 20, 150, 25)

    enemy_rect = pygame.Rect(370, 280, 150, 25)
    enemy_outline_rect = pygame.Rect(370, 280, 150, 25)

    screen.fill((0, 0, 0))
    View.draw_image("battle_background.jpg", 0, 0, 810, 450)
    View.draw_image(hero.get_image(), 75, 330, 90, 90)
    View.draw_image(monster.get_image(), 400, 330, 90, 90)
    pygame.draw.rect(screen, (255, 255, 255), white_rect, 5)

    def update(character, text, damage):
        pygame.draw.rect(screen, (0,0,0), black_rect)
        result = character.get_hp() + damage
        if result > 0:
            View.draw_result(text, 40, 500)
            character.set_hp(character.get_hp() + damage)
            if isinstance(character, Monster):
                time.sleep(5)
                print(character.get_name() + ": " + str(character.get_hp()))
            else:
                print(character.get_name() + ": " + str(character.get_hp()))
            return True
        else:
            View.draw_result(character.get_name() + " won!", 40, 500)
        return False

    def monsters_turn():
        num = randint(1, 3)
        hero_agility = hero.get_agility()
        if num == 1:
            result = monster.attack()
            if result[0] > hero_agility:
                in_battle = update(hero, hero.get_name() + " took " + str(result[1]) + " damage!", -result[1])
            else:
                in_battle = update(hero, hero.get_name() + " dodged!", 0)
        elif num == 2:  # Special button
            result = hero.get_instance().special_attack()
            if result[0] > hero_agility and monster.get_opposite_element() == monster.get_element():
                in_battle = update(hero, hero.get_name() + " took " + str(result[1]) + " damage!", 2 * -result[1])
            elif result[0] > hero_agility:
                in_battle = update(hero, hero.get_name() + " took " + str(result[1]) + " damage!", -result[1])
            else:
                in_battle = update(hero, hero.get_name() + " dodged!", 0)
        else:
            in_battle = update(monster,  monster.get_name() + " healed!", 0)
            monster.heal()

    while isRunning and in_battle:
        # Fill the screen and draw the background

        # Draw hero health bar and outline
        pygame.draw.rect(screen, (34, 139, 34), health_rect)
        pygame.draw.rect(screen, (255, 255, 255), health_rect_outline, 3)
        View.draw_text("HP", 20, 15)
        View.draw_text(str(hero.get_hp()) + "/" + str(hero.get_max_hp()), 250, 15)
        View.draw_text("Agility:  " + str(hero.get_agility()), 20, 60)

        # Draw hero and monster images
        pygame.draw.rect(screen, (34, 139, 34), enemy_rect)
        pygame.draw.rect(screen, (255, 255, 255), enemy_outline_rect, 3)


        # Draw buttons
        View.draw_button("battle_button.png", "Attack", 20, 700, 185, 75)
        View.draw_button("battle_button.png", "Special", 215, 700, 185, 75)
        View.draw_button("battle_button.png", "Potion", 410, 700, 185, 75)
        View.draw_button("battle_button.png", "Skip", 605, 700, 185, 75)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mx, my = event.pos
                    monster_agility = monster.get_agility()
                    # Check if any buttons are clicked
                    if 20 <= mx <= 205 and 700 <= my <= 775:  # Attack button
                        result = hero.get_instance().attack()
                        if result[0] > monster_agility:
                            in_battle = update(monster,  monster.get_name() + " took " + str(result[1]) + " damage!", -result[1])

                        else:
                            in_battle = update(monster, "The monster dodged!", 0)

                    elif 215 <= mx <= 400 and 700 <= my <= 775:  # Special button
                        result = hero.get_instance().special_attack()
                        if result[0] > monster_agility and monster.get_opposite_element() == monster.get_element():
                            in_battle = update(monster,  monster.get_name() + " took " + str(result[1]) + " damage!", 2*-result[1])
                        elif result[0] > monster_agility:
                            in_battle = update(monster,  monster.get_name() + " took " + str(result[1]) + " damage!", -result[1])
                        else:
                            in_battle = update(monster,  monster.get_name() + " dodged! ", 0)

                    elif 410 <= mx <= 595 and 700 <= my <= 775:  # Potion button
                        # Potion logic (if any)
                        pass

                    elif 605 <= mx <= 790 and 700 <= my <= 775:  # Skip button
                        # Skip logic (if any)
                        pass
                monsters_turn()

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
