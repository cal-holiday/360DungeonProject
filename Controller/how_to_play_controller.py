from View import how_to_play_view as help_view
import pygame

pygame.init()
Clock = pygame.time.Clock()

def run():
    is_running = True
    while is_running:


        #images
        help_view.draw_scaled_image("panel.png",0,0,help_view.SCREEN_WIDTH,help_view.SCREEN_HEIGHT)
        help_view.draw_button("buttonSquare_beige.png","w", 500, 420, 75, 75)
        help_view.draw_button("buttonSquare_beige.png","s",500, 500, 75, 75)
        help_view.draw_button("buttonSquare_beige.png", "a", 420, 500, 75, 75)
        help_view.draw_button("buttonSquare_beige.png", "d", 580, 500, 75, 75)

        #texts
        help_view.draw_header("HOW TO PLAY", 50, 50)
        pygame.display.set_caption("How To Play")
        help_view.draw_text("You are a hero trapped in a dungeon.",50,120)
        help_view.draw_text("Navigate through the dungeon maze", 50, 160)
        help_view.draw_text("to find the four pillars of OO.", 50, 200)
        help_view.draw_text("Watch out for monsters! They can drop",50,240)
        help_view.draw_text("pillars or potions to help you get", 50, 280)
        help_view.draw_text("through the maze. Once you find all",50,320)
        help_view.draw_text("four pillars you can find", 50, 360)
        help_view.draw_text("the Exit and escape!", 50, 400)
        help_view.draw_text("use wasd keys to move", 350, 600)



        exit_button = help_view.draw_button("buttonSquare_beige.png","x",710,50,50,50)

        if exit_button:
            is_running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
