import pygame
from View import Choose_Hero as View

class ChooseHeroController:
    def __init__(self):
        self.isRunning = True
        self.clock = pygame.time.Clock()
        self.hero_name = ""
        self.text_field_active = False

        # Hero button definitions
        self.heroes = {
            "fire": {"rect": pygame.Rect(150, 675, 100, 100), "element": "Fire", "health": "80", "agility": "12"},
            "water": {"rect": pygame.Rect(450, 550, 100, 100), "element": "Water", "health": "60", "agility": "8"},
            "air": {"rect": pygame.Rect(250, 550, 100, 100), "element": "Air", "health": "40", "agility": "16"},
            "earth": {"rect": pygame.Rect(550, 675, 100, 100), "element": "Earth", "health": "100", "agility": "4"},
        }

        # Default stats (will be updated upon hovering or selecting a hero)
        self.current_stats = {"element": "---", "health": "---", "agility": "---"}
        self.selected_hero = None
        self.confirm_button_visible = False
        self.confirmation_prompt = False

        # Confirmation state
        self.confirmation_result = False  # Tracks if "Yes" was clicked

    def run(self):
        while self.isRunning:
            mouse_pos = pygame.mouse.get_pos()

            # Draw the background and UI
            View.draw_scaled_image("dungeonBackground.png", 0, 0, 810, 810)
            View.draw_scaled_image("banner.png", 45, 20, 700, 150)
            View.draw_header("Choose Your Hero", 90, 50)

            # Draw the text field
            if not self.confirmation_prompt:
                View.draw_text_field(90, 200, 375, 50, "Name Your Hero", self.text_field_active, self.hero_name)

            # Draw current stats (display selected hero stats if a hero is selected, or hover stats if no hero selected)
            View.draw_text(f"Element: {self.current_stats['element']}", 245, 300)
            View.draw_text(f"Health: {self.current_stats['health']}", 265, 375)
            View.draw_text(f"Agility: {self.current_stats['agility']}", 258, 450)

            # Draw hero buttons and highlight if hovered or selected
            for hero, data in self.heroes.items():
                if data["rect"].collidepoint(mouse_pos) and not self.confirmation_prompt:
                    # Update stats when hovering
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
                    # Highlight the selected hero with a persistent box
                    pygame.draw.rect(
                        pygame.display.get_surface(),
                        (0, 255, 0),
                        data["rect"].inflate(10, 10),
                        3
                    )

                # Draw the button image
                View.draw_button(f"{hero}_hero.png", "", data["rect"].x, data["rect"].y, data["rect"].width, data["rect"].height)

            # Draw the Confirm button if visible and no confirmation prompt
            if self.confirm_button_visible and not self.confirmation_prompt:
                View.draw_button("button.png", "confirm", 490, 200, 200, 50)

            # Handle the confirmation prompt
            if self.confirmation_prompt:
                pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0), (200, 300, 400, 200))  # Background box
                View.draw_text("Are you sure?", 280, 325)
                View.draw_button("button.png", "Yes", 250, 400, 100, 50)
                View.draw_button("button.png", "No", 450, 400, 100, 50)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
                    pygame.quit()
                    exit()

                if not self.confirmation_prompt:
                    # Handle mouse clicks for hero selection and confirm button
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Check if the click is on a hero button
                        for hero, data in self.heroes.items():
                            if data["rect"].collidepoint(event.pos):
                                self.selected_hero = hero
                                # Set stats for selected hero
                                self.current_stats = {
                                    "element": data["element"],
                                    "health": data["health"],
                                    "agility": data["agility"]
                                }
                                self.confirm_button_visible = bool(self.hero_name)  # Show confirm if name is entered
                                break

                        # Handle text field activation
                        if 100 <= event.pos[0] <= 400 and 200 <= event.pos[1] <= 250:
                            self.text_field_active = True
                        else:
                            self.text_field_active = False

                        # Check if the Confirm button is clicked
                        if self.confirm_button_visible and pygame.Rect(490, 200, 200, 50).collidepoint(event.pos):
                            self.confirmation_prompt = True  # Show the confirmation prompt
                            self.confirm_button_visible = False  # Hide the confirm button

                    # Handle keyboard input
                    if event.type == pygame.KEYDOWN and self.text_field_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.hero_name = self.hero_name[:-1]
                            self.confirm_button_visible = bool(self.hero_name and self.selected_hero)
                        elif event.key == pygame.K_RETURN:
                            print(f"Hero Name Confirmed: {self.hero_name}")
                        else:
                            self.hero_name += event.unicode
                            self.confirm_button_visible = bool(self.hero_name and self.selected_hero)

                else:
                    # Handle the confirmation prompt buttons
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.Rect(250, 400, 100, 50).collidepoint(event.pos):  # Yes button
                            self.confirmation_result = True
                            self.isRunning = False  # End the loop or proceed to the next screen
                        elif pygame.Rect(450, 400, 100, 50).collidepoint(event.pos):  # No button
                            self.confirmation_prompt = False  # Close the prompt
                            self.confirm_button_visible = True  # Re-show the confirm button

            # Update the display
            pygame.display.update()
            self.clock.tick(60)

    def confirmed(self):
        return self.confirmation_result

# Instantiate and run the controller
if __name__ == "__main__":
    controller = ChooseHeroController()
    controller.run()
