import pygame
import random
from Model.CharacterFactory import CharacterFactory
from Model.Element import Element
from Model.Hero import Hero
from Model.Inventory import Inventory
from Model.Potion import HealthPotion
from View import Battle_View as View

# Initialize pygame
pygame.init()

def run(monster):
    screen = pygame.display.set_mode((810, 810))
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
        View.draw_text(f"Health Potions: {inventory.number_of_health_potions()}", 470, 625)

    def update(character, text, damage):
        """Update health bars and display results."""
        result = character.get_hp() + damage
        if result <= 0:
            character.set_hp(0)
        else:
            character.set_hp(result)
        pygame.draw.rect(screen, (0, 0, 0), black_rect)
        redraw_screen()
        display_health_bars()
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
            pygame.display.update()
            pygame.time.wait(2000)
            return False

    def display_health_bars():
        """Draw health bars for the hero and monster."""
        # Hero health bar

        if hero.get_hp() == 0:
            hero_health_width = 0 # If hero is defeated, set width to 0
        else:
            hero_health_width = (hero.get_hp() / hero.get_max_hp()) * 150
        pygame.draw.rect(screen, (34, 139, 34), pygame.Rect(80, 20, hero_health_width, 25))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(80, 20, 150, 25), 3)
        View.draw_text("HP", 20, 15)
        View.draw_text(f"{hero.get_hp()}/{hero.get_max_hp()}", 250, 15)

        # Monster health bar
        if monster.get_hp() == 0:
            monster_health_width = 0  # If monster is defeated, set width to 0
        else:
            monster_health_width = (monster.get_hp() / monster.get_max_hp()) * 150
        pygame.draw.rect(screen, (34, 139, 34), pygame.Rect(370, 280, monster_health_width, 25))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(370, 280, 150, 25), 3)
        View.draw_text(f"{monster.get_hp()}/{monster.get_max_hp()}", 400, 300)

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
            if result[0] > monster.get_agility() and monster.get_element() == hero.get_opposite_element():
                return update(monster, f"{hero.get_name()} did {2 * result[1]} damage!", 2 * -result[1])
            elif result[0] > monster.get_agility():
                return update(monster, f"{hero.get_name()} did {result[1]} damage!", -result[1])
            else:
                return update(monster, f"{hero.get_name()} missed!", 0)

        elif action == "potion":
            inventory.drink_health_potion()
            return update(monster, f"{hero.get_name()} used a health potion!", 10)

    while isRunning and in_battle:
        redraw_screen()
        display_health_bars()

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
                    if inventory.has_health_potion() and hero.get_hp() + 10 <= hero.get_max_hp():
                        in_battle = hero_turn("potion")
                        clock.tick(10)
                        in_battle = monsters_turn()
                    else:
                        View.draw_result("You can't use that", 40, 500)

                elif 605 <= mx <= 790 and 700 <= my <= 775:
                    isRunning = False
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    hero = CharacterFactory.create_hero("hero", Element.WATER)
    screen = pygame.display.set_mode((810, 810))
    monster = CharacterFactory.create_monster(Element.EARTH)
    inventory = Inventory()
    inventory.add(HealthPotion())
    inventory.add(HealthPotion())
    print(f"Inventory has health potions: {inventory.has_health_potion()}")
    run(monster)