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
    action_delay = 400  # Delay in milliseconds between turns

    black_rect = pygame.Rect(25, 475, 760, 190)
    white_rect = pygame.Rect(20, 470, 770, 200)

    def redraw_screen():
        """Redraw the screen elements."""
        screen.fill((0, 0, 0))
        View.draw_image("battle_background.jpg", 0, 0, 810, 450)
        View.draw_image(hero.get_image(), 75, 330, 90, 90)
        View.draw_image(monster.get_image(), 400, 330, 90, 90)
        pygame.draw.rect(screen, (255, 255, 255), white_rect, 5)

    def update(character, text, damage):
        """Update health bars and display results."""
        pygame.draw.rect(screen, (0, 0, 0), black_rect)
        result = character.get_hp() + damage
        character.set_hp(result)
        redraw_screen()
        display_health_bars(hero, monster)

        if result > 0:
            if character.get_name() == hero.get_name():
                View.draw_monster_result(text, 40, 500)
            else:
                View.draw_result(text, 40, 500)
            pygame.display.update()
            pygame.time.wait(action_delay)
            return True
        else:
            if character.get_name() == hero.get_name():
                View.draw_monster_result(hero.get_name() + " was defeated", 40, 500)
            else:
                View.draw_result(hero.get_name() + " won!", 40, 500)

            # Ensure the defeated character's health bar is gone
            if character.get_name() == hero.get_name():
                # If hero is defeated, set monster's health bar to 0
                monster.set_hp(0)
            else:
                # If monster is defeated, set hero's health bar to 0
                hero.set_hp(0)

            pygame.display.update()
            pygame.time.wait(2000)
            return False

    def display_health_bars(hero, monster):
        """Draw health bars for the hero and monster."""
        # Hero health bar
        hero_current_hp = max(0, hero.get_hp())  # Ensure hero's HP doesn't go below 0
        hero_health_width = (hero_current_hp / hero.get_max_hp()) * 150
        if hero_current_hp == 0:
            hero_health_width = 0  # If hero is defeated, set width to 0
        pygame.draw.rect(screen, (34, 139, 34), pygame.Rect(80, 20, hero_health_width, 25))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(80, 20, 150, 25), 3)
        View.draw_text("HP", 20, 15)
        View.draw_text(f"{hero_current_hp}/{hero.get_max_hp()}", 250, 15)

        # Monster health bar
        monster_current_hp = max(0, monster.get_hp())  # Ensure monster's HP doesn't go below 0
        monster_health_width = (monster_current_hp / monster.get_max_hp()) * 150
        if monster_current_hp == 0:
            monster_health_width = 0  # If monster is defeated, set width to 0
        pygame.draw.rect(screen, (34, 139, 34), pygame.Rect(370, 280, monster_health_width, 25))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(370, 280, 150, 25), 3)
        View.draw_text(f"{monster_current_hp}/{monster.get_max_hp()}", 400, 300)

    def monsters_turn():
        """Monster's actions during its turn."""
        num = random.randint(1, 3)
        pygame.time.wait(action_delay)
        if num == 1:
            result = monster.attack()
            if result[0] > hero.get_agility():
                return update(hero, f" {monster.get_name()} dealt {result[1]} damage!", -result[1])
            else:
                return update(hero, f"{monster.get_name()} missed!", 0)
        elif num == 2:
            result = monster.special_attack()
            if result[0] > hero.get_agility():
                return update(hero, f"{monster.get_name()} dealt {result[1]} damage!", -result[1])
            else:
                return update(hero, f"{monster.get_name()} missed!", 0)
        else:
            healed = monster.heal()
            if healed == False:
                result = monster.attack()
                if result[0] > hero.get_agility():
                    return update(hero, f"{monster.get_name()} dealt {result[1]} damage!", -result[1])
                else:
                    return update(hero, f"{monster.get_name()} missed!", 0)

            return update(hero, f" {monster.get_name()} healed!", 0)

    def hero_turn(action):
        """Handle hero's actions based on input."""
        monster_agility = monster.get_agility()

        if action == "attack":
            result = hero.attack()
            if result[0] > monster_agility:
                return update(monster, f"{hero.get_name()} did {result[1]} damage!", -result[1])
            else:
                return update(monster, f"{hero.get_name()} missed!", 0)

        elif action == "special":
            result = hero.special_attack()
            multiplier = 2 if monster.get_opposite_element() == hero.get_element() else 1
            if result[0] > monster_agility:
                return update(monster, f"{hero.get_name()} did {multiplier * result[1]} damage!", multiplier * -result[1])
            else:
                return update(monster, f"{hero.get_name()} missed!", 0)

        elif action == "potion":
            if inventory.has_health_potion() and hero.get_hp() + 10 <= hero.get_max_hp():
                inventory.drink_health_potion()
                return update(monster, f"{hero.get_name()} used a health potion!", 10)
            else:
                View.draw_result("You can't use that", 40, 500)
                return True  # Continue battle
        elif action == "skip":
            return False

    while isRunning and in_battle:
        redraw_screen()
        display_health_bars(hero, monster)

        View.draw_button("battle_button.png", "Attack", 20, 700, 185, 75)
        View.draw_button("battle_button.png", "Special", 215, 700, 185, 75)
        View.draw_button("battle_button.png", "Potion", 410, 700, 185, 75)
        View.draw_button("battle_button.png", "Skip", 605, 700, 185, 75)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos

                if 20 <= mx <= 205 and 700 <= my <= 775:
                    in_battle = hero_turn("attack")
                    if in_battle:
                        clock.tick(10)
                        in_battle = monsters_turn()

                elif 215 <= mx <= 400 and 700 <= my <= 775:
                    in_battle = hero_turn("special")
                    if in_battle:
                        clock.tick(10)
                        in_battle = monsters_turn()

                elif 410 <= mx <= 595 and 700 <= my <= 775:
                    in_battle = hero_turn("potion")
                    if in_battle:
                        clock.tick(10)
                        in_battle = monsters_turn()

                elif 605 <= mx <= 790 and 700 <= my <= 775:
                    in_battle = hero_turn("skip")
                    if in_battle:
                        isRunning = False


        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    hero = CharacterFactory.create_hero("hero", Element.WATER)
    screen = pygame.display.set_mode((810, 810))
    monster = CharacterFactory.create_monster(Element.EARTH)
    inventory = Inventory()
    inventory.add(HealthPotion)
    inventory.add(HealthPotion)
    inventory.add(HealthPotion)
    run(screen, monster)
