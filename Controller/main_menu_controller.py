from View import main_menu_view
import pygame

run = True

while run:
    main_menu_view.screen.fill((234, 165, 108))
    main_menu_view.draw_scaled_image("dungeonBackground.png", 0, 0, 810, 810)
    main_menu_view.draw_scaled_image("banner.png", 155, 80, 500, 150)
    main_menu_view.draw_header("Dungeon Adventure", 197, 120)
    main_menu_view.draw_button("button.png", "New Game", 300, 300, 210, 50)
    main_menu_view.draw_button("button.png", "Load Game", 300, 370, 210, 50)
    main_menu_view.draw_button("button.png", "How to play", 300, 440, 210, 50)
    quit_button = main_menu_view.draw_button("button.png", "Quit", 300, 510, 210, 50)

    if(quit_button == True):
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
