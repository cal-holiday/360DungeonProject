from Controller.SaveLoad import SaveLoad
from Model.Dungeon import Dungeon
from View import SaveFileView as View
import pygame

pygame.init()
Clock = pygame.time.Clock()

def run():
    is_running = True
    input_text = ""  # Variable to store the text input
    active = False

    while is_running:

        # Images
        View.draw_scaled_image('Assets/panel.png', 0, 0, View.SCREEN_WIDTH, View.SCREEN_HEIGHT)
        save_file = View.draw_text_field(75, 155, 450, 75, "Save File Name", active, input_text)

        View.draw_header("Save Game", 162, 75)
        save_button = View.draw_button('Assets/buttonSquare_beige.png', "save", 575, 155, 150, 75)
        exit_button = View.draw_button('Assets/buttonSquare_beige.png', "x", 710, 40, 50, 50)


        if save_button:
            SaveLoad.save_game(Dungeon.get_instance().pickle_dungeon(), input_text)
            is_running = False

        if exit_button:
            is_running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if 75 <= mx <= 525 and 155 <= my <= 230:  # Check if mouse click is in the text field area
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:  # Press Enter to save the input
                    SaveLoad.save_game(Dungeon.get_instance().pickle_dungeon(), input_text)
                    active = False  # Deactivate the text field after saving
                    is_running = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  # Handle backspace
                else:
                    input_text += event.unicode  # Add the character to the input text

        pygame.display.update()

if __name__ == '__main__':
    run()
