import pygame

from Controller.demo_controller import monster
from Model.CharacterFactory import CharacterFactory
from Model.Element import Element
from View import Battle_View as View
from Model.Hero import Hero


class BattleController(monster):
    def __init__(self, monster):
        self.isRunning = True
        self.hero = Hero.get_instance()
        self.monster = monster
        self.clock = pygame.time.Clock()

    def run(self):
        while self.isRunning:
            View.draw_scaled_image(self.monster, 500, 200, 90, 90)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
                    pygame.quit()
                    exit()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    monster = CharacterFactory.create_monster(Element.EARTH)
    controller = BattleController(monster)
    controller.run()
