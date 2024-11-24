import pygame
from View import Choose_Hero as View

class ChooseHeroController:
    def __init__(self):
        pygame.init()
        self.isRunning = True
        self.clock = pygame.time.Clock()
        self.hero_name = ""
        self.text_field_active = False
        self.text_field_rect = pygame.Rect(200, 180, 400, 50)
        # Hero button definitions
        self.heroes = {
            "fire": {"rect": pygame.Rect(150, 675, 100, 100), "element": "Fire", "health": "80", "agility": "12"},
            "water": {"rect": pygame.Rect(450, 550, 100, 100), "element": "Water", "health": "60", "agility": "8"},
            "air": {"rect": pygame.Rect(250, 550, 100, 100), "element": "Air", "health": "40", "agility": "16"},
            "earth": {"rect": pygame.Rect(550, 675, 100, 100), "element": "Earth", "health": "100", "agility": "4"},
        }
        # Default stats (updated on hover or selection)
        self.current_stats = {"element": "---", "health": "---", "agility": "---"}
        self.selected_hero = None
        self.confirm_button_visible = False
        self.confirmation_prompt = False
        # Confirmation state
        self.confirmation_result = False

    def run(self):
        while self.isRunning:
            mouse_pos = pygame.mouse.get_pos()
            # Draw the background and UI
            View.draw_scaled_image("dungeonBackground.png", 0, 0, 810, 810)
            View.draw_scaled_image("banner.png", 45, 20, 700, 150)
            View.draw_header("Choose Your Hero", 90, 50)

            # Draw elements only if the confirmation prompt is NOT active
            if not self.confirmation_prompt:
                # Draw the text field with active indicator
                border_color = (0, 255, 0) if self.text_field_active else (255, 255, 255)
                pygame.draw.rect(pygame.display.get_surface(), border_color, self.text_field_rect, 2)
                View.draw_text_field(
                    self.text_field_rect.x, self.text_field_rect.y,
                    self.text_field_rect.width, self.text_field_rect.height,
                    "Name Your Hero", self.text_field_active, self.hero_name
                )

                # Draw current stats
                View.draw_text(f"Element: {self.current_stats['element']}", 283, 260)
                View.draw_text(f"Health: {self.current_stats['health']}", 305, 320)
                View.draw_text(f"Agility: {self.current_stats['agility']}", 297, 380)

                # Draw hero buttons
                for hero, data in self.heroes.items():
                    if data["rect"].collidepoint(mouse_pos):
                        # Highlight hovered hero and update stats
                        self.current_stats = {
                            "element": data["element"],
                            "health": data["health"],
                            "agility": data["agility"],
                        }
                        pygame.draw.rect(
                            pygame.display.get_surface(),
                            (255, 255, 0),
                            data["rect"].inflate(10, 10),
                            3
                        )
                    if self.selected_hero == hero:
                        # Highlight the selected hero
                        pygame.draw.rect(
                            pygame.display.get_surface(),
                            (0, 255, 0),
                            data["rect"].inflate(10, 10),
                            3
                        )
                    View.draw_button(f"{hero}_hero.png", "", data["rect"].x, data["rect"].y, data["rect"].width,
                                     data["rect"].height)

                # Draw the Confirm button (at new position)
                if self.confirm_button_visible:
                    View.draw_button("button.png", "confirm", 302, 450, 200, 50)

            # Draw the confirmation prompt
            if self.confirmation_prompt:
                pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0), (200, 300, 400, 200))  # Background box
                View.draw_text("Are you sure?", 280, 325)
                # Ensure confirmation prompt buttons have the correct positions
                View.draw_button("button.png", "Yes", 250, 400, 100, 50)
                View.draw_button("button.png", "No", 450, 400, 100, 50)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
                    pygame.quit()
                    exit()

                if not self.confirmation_prompt:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Check if a hero is clicked
                        for hero, data in self.heroes.items():
                            if data["rect"].collidepoint(event.pos):
                                self.selected_hero = hero
                                self.current_stats = {
                                    "element": data["element"],
                                    "health": data["health"],
                                    "agility": data["agility"],
                                }
                                self.confirm_button_visible = bool(self.hero_name)
                                break
                        # Activate or deactivate text field
                        if self.text_field_rect.collidepoint(event.pos):
                            self.text_field_active = True
                        else:
                            self.text_field_active = False

                        # Confirm button click (use updated position)
                        if self.confirm_button_visible and pygame.Rect(302, 450, 200, 50).collidepoint(event.pos):
                            self.confirmation_prompt = True
                            self.confirm_button_visible = False

                    # Handle text input
                    if event.type == pygame.KEYDOWN and self.text_field_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.hero_name = self.hero_name[:-1]
                        elif event.key == pygame.K_RETURN:
                            print(f"Hero Name Confirmed: {self.hero_name}")
                        elif len(self.hero_name) < 20:  # Limit text length
                            self.hero_name += event.unicode
                        self.confirm_button_visible = bool(self.hero_name and self.selected_hero)

                else:  # Handle confirmation prompt
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Check for Yes button click
                        if pygame.Rect(250, 400, 100, 50).collidepoint(event.pos):  # Yes button
                            self.confirmation_result = True
                            print(f"Hero {self.hero_name} selected with {self.current_stats['element']}.")
                            self.isRunning = False  # End loop or proceed to next screen
                        # Check for No button click
                        elif pygame.Rect(450, 400, 100, 50).collidepoint(event.pos):  # No button
                            self.confirmation_prompt = False
                            self.confirm_button_visible = True

            # Update the display
            pygame.display.update()
            self.clock.tick(60)

    def confirmed(self):
        return self.confirmation_result


if __name__ == "__main__":
    controller = ChooseHeroController()
    controller.run()
