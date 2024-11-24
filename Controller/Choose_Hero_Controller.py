import pygame
from View import Choose_Hero as View


class ChooseHeroController:
    Clock = pygame.time.Clock()
    while True:
        View.screen.fill((234,165,108))
        View.draw_scaled_image("banner.png", 45, 20, 700, 150)
        """
        View.draw_header("Choose Your Hero", 90, 50)
        View.draw_button("button.png", "confirm", 500, 230, 200,80)

        View.draw_text("Health:", 575, 400)
        View.draw_text("Agility:",570, 475)
        View.draw_text("Element:", 555, 550)

        View.draw_image("fire_hero.png", 100, 400)
        View.draw_text("Fire Hero", 50, 475)
        View.draw_image("water_hero.png", 350, 600)
        View.draw_text("Water Hero", 300, 675)
        View.draw_image("air_hero.png", 100, 600)
        View.draw_text("Air Hero", 50, 675)
        View.draw_image("earth_hero.png", 350, 400)
        View.draw_text("Earth Hero", 300, 475)

        View.draw_text_field(100, 250, 300, 50,"Name Your Hero", False, "" )
        """


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        Clock.tick(60)