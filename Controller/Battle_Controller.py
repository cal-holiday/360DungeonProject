from pydoc import text

import pygame
import random
from Model.CharacterFactory import CharacterFactory
from Model.Element import Element
from Model.Hero import Hero
from Model.Inventory import Inventory
from Model.Monster import Monster
from Model.healthPotion import HealthPotion
from View import Battle_View as View

# Initialize pygame
pygame.init()

def run(screen, monster):
    View.pass_screen(screen)
    isRunning = True
    clock = pygame.time.Clock()
    hero = Hero.get_instance()
    inventory = Inventory.get_instance()
    in_battle = True
    monster_turn = False

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
        # Draw the black background for the result text
        pygame.draw.rect(screen, (0, 0, 0), black_rect)
        result = character.get_hp() + damage

        # Update the character's health
        if result > 0:
            character.set_hp(character.get_hp() + damage)
            # Print current health for debugging
            print(character.get_name() + ": " + str(character.get_hp()))

            # Redraw the health bars after the action
            View.draw_image("battle_background.jpg", 0, 0, 810, 450)
            View.draw_image(hero.get_image(), 75, 330, 90, 90)
            View.draw_image(monster.get_image(), 400, 330, 90, 90)
            hero_max_hp = hero.get_max_hp()
            hero_current_hp = hero.get_hp()

            # Calculate the hero's health bar width based on current HP
            hero_health_width = (hero_current_hp / hero_max_hp) * 150  # 150 is the original width of the health bar

            # Monster's health bar calculation
            monster_max_hp = monster.get_max_hp()
            monster_current_hp = monster.get_hp()

            # Calculate the monster's health bar width based on current HP
            monster_health_width = (
                                               monster_current_hp / monster_max_hp) * 150  # 150 is the original width of the health bar

            # Draw the hero's health bar with updated width
            pygame.draw.rect(screen, (34, 139, 34), pygame.Rect(80, 20, hero_health_width, 25))  # Hero's health bar
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(80, 20, 150, 25), 3)  # Hero's health bar outline
            View.draw_text("HP", 20, 15)
            View.draw_text(f"{hero_current_hp}/{hero_max_hp}", 250, 15)

            # Draw the monster's health bar with updated width
            pygame.draw.rect(screen, (34, 139, 34),
                             pygame.Rect(370, 280, monster_health_width, 25))  # Monster's health bar
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(370, 280, 150, 25), 3)  # Monster's health bar outline
            View.draw_text(f"{monster_current_hp}/{monster_max_hp}", 400, 300)
            if isinstance(character, Monster):
                View.draw_result(text, 40, 500)
                pygame.time.wait(1000)
            else:
                View.draw_result(text, 40, 500)
            return True
        elif damage < 0:
            View.draw_result(text, 40, 500)
        else:
            # If character's HP is 0 or less, display the victory message
            View.draw_result(character.get_name() + " won!", 40, 500)
            return False  # End the battle

    def monsters_turn():
        num = random.randint(1, 3)
        hero_agility = hero.get_agility()
        if num == 1:
            # Monster attacks
            result = monster.attack()
            if result[0] > hero_agility:
                in_battle = update(hero, "Monster: " + hero.get_name() + " took " + str(result[1]) + " damage!", -result[1])
            else:
                in_battle = update(hero, "Monster: " + hero.get_name() + " dodged!", 0)
        elif num == 2:
            # Monster uses a special attack
            result = monster.special_attack()  # Assuming `special_attack` method exists for Monster
            if result[0] > hero_agility:
                in_battle = update(hero, "Monster: " + hero.get_name() + " took " + str(result[1]) + " damage!", -result[1])
            else:
                in_battle = update(hero, "Monster: " + hero.get_name() + " dodged!", 0)
        else:
            # Monster heals
            in_battle = update(monster, "Monster: " + monster.get_name() + " healed!", 0)
            monster.heal()

    while isRunning and in_battle:
        # Fill the screen and draw the background
        pygame.draw.rect(screen, (34, 139, 34), health_rect)
        pygame.draw.rect(screen, (255, 255, 255), health_rect_outline, 3)
        View.draw_text("HP", 20, 15)
        View.draw_text(str(hero.get_hp()) + "/" + str(hero.get_max_hp()), 250, 15)
        View.draw_text("Agility:  " + str(hero.get_agility()), 20, 60)

        # Draw hero and monster images
        pygame.draw.rect(screen, (34, 139, 34), enemy_rect)
        pygame.draw.rect(screen, (255, 255, 255), enemy_outline_rect, 3)
        View.draw_text(str(monster.get_hp()) + "/" + str(monster.get_max_hp()), 400, 300)

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
                            in_battle = update(monster, monster.get_name() + " took " + str(result[1]) + " damage!", -result[1])
                        else:
                            update(monster, "The monster dodged!", 0)
                        monster_turn = True
                    elif 215 <= mx <= 400 and 700 <= my <= 775:  # Special button
                        result = hero.get_instance().special_attack()
                        if result[0] > monster_agility and monster.get_opposite_element() == monster.get_element():
                            in_battle = update(monster, monster.get_name() + " took " + str(result[1]) + " damage!", 2 * -result[1])
                        elif result[0] > monster_agility:
                            in_battle = update(monster, monster.get_name() + " took " + str(result[1]) + " damage!", -result[1])
                        else:
                            in_battle = update(monster, monster.get_name() + " dodged! ", 0)
                        monster_turn = True
                    elif 410 <= mx <= 595 and 700 <= my <= 775:  # Potion button
                        if inventory.has_health_potion() and hero.get_hp() + 10 <= hero.get_max_hp():
                            inventory.drink_health_potion()  # Drink the health potion
                            update(hero, hero.get_name() + " used a health potion!", 10)
                            monster_turn = True  # Let monster take its turn after the hero uses the potion
                        else:
                            View.draw_result("You can't use that", 40, 500)  # Display message if potion can't be used
                            monster_turn = False  # Don't allow monster's turn yet
                    elif 605 <= mx <= 790 and 700 <= my <= 775:  # Skip button
                        in_battle = False

                if monster_turn:
                    monsters_turn()


        # Update the display
        pygame.display.update()
        clock.tick(60)
