import pygame
from Model.Hero import Hero
from Model.Inventory import Inventory
pygame.init()

def draw_hero(screen):
    width, height = pygame.display.get_surface().get_size()
    default_size = width // 18

    hero_img = pygame.image.load(Hero.get_instance().get_image())
    scaled_hero = pygame.transform.scale(hero_img, (default_size, default_size))
    screen.blit(scaled_hero, (Hero.get_instance().get_x(), Hero.get_instance().get_y()))
    current_pillars = Inventory.get_instance().get_pillars()
    if len(current_pillars) > 0:
        locations = [(Hero.get_instance().get_x() -8, Hero.get_instance().get_y() - 30),
                     (Hero.get_instance().get_x() + 27, Hero.get_instance().get_y() -30),
                     (Hero.get_instance().get_x() - 30, Hero.get_instance().get_y()),
                     (Hero.get_instance().get_x() + 50, Hero.get_instance().get_y())
                     ]
        i = 0
        for pillar in current_pillars:
            img = pygame.image.load(pillar.get_image())
            scaled_img = pygame.transform.scale(img, (30,30))
            screen.blit(scaled_img, (locations[i]))
            i+=1
    return scaled_hero.get_rect()

def draw_room(screen, room):
    width, height = pygame.display.get_surface().get_size()
    room_size = width // 3
    default_size = width // 18

    rect_list = []
    x = room.get_location()[0] * room_size
    y = room.get_location()[1] * room_size + default_size

    floor = pygame.image.load('floor.png')
    floor_img = pygame.transform.scale(floor, (room_size - 5, room_size - 5))
    screen.blit(floor_img, (x, y))
    corner = pygame.image.load('corner.png')
    corner = pygame.transform.scale(corner, (default_size, default_size))
    screen.blit(corner, (x, y))
    screen.blit(corner, (x + room_size - default_size, y))
    screen.blit(corner, (x, y + room_size - default_size))
    screen.blit(corner, (x + room_size - default_size, y + room_size -default_size))

    wall = pygame.image.load('wall.png')
    vert_wall = pygame.transform.scale(wall, (default_size, default_size))
    horz_wall = pygame.transform.rotate(vert_wall, 90)
    default_vert_walls = [(x, y + default_size), #top left corner bottom
                     (x, y + room_size - 2*default_size), #bottom left corner top
                     (x + room_size - default_size, y + default_size),#top right corner bottom
                     (x + room_size - default_size, y + room_size- 2*default_size), #bottom right corner top
                     ]
    default_horz_walls = [(x + default_size, y), #top left corner right
                     (x + room_size - 2*default_size, y), #top right corner left
                     (x + default_size, y + room_size- default_size), #bottom left corner right
                     (x + room_size- 2*default_size, y + room_size - default_size) #bottom right corner left
                     ]
    for location in default_vert_walls:
        rect = pygame.Rect(location[0], location[1], default_size, default_size)
        screen.blit(vert_wall, location)
        rect_list.append(rect)
    for location in default_horz_walls:
        rect = pygame.Rect(location[0], location[1], default_size, default_size)
        screen.blit(horz_wall, location)
        rect_list.append(rect)

    if room.get_nwall():
        screen.blit(horz_wall, (x + 2*default_size, y))
        screen.blit(horz_wall, (x + room_size - 3*default_size, y))
        n_wall = pygame.Rect(x + default_size, y, room_size- 2*default_size, default_size)
        rect_list.append(n_wall)

    if room.get_wwall():
        screen.blit(vert_wall, (x, y + 2*default_size))
        screen.blit(vert_wall, (x, y + room_size - 3*default_size))
        w_wall = pygame.Rect(x, y + default_size, default_size, room_size - 2*default_size)
        rect_list.append(w_wall)

    if room.get_ewall():
        screen.blit(vert_wall, (x + room_size - default_size, y + 2*default_size))
        screen.blit(vert_wall, (x + room_size - default_size, y + room_size - 3*default_size))
        e_wall = pygame.Rect(x + room_size - default_size, y + default_size, default_size, room_size - 2*default_size)
        rect_list.append(e_wall)

    if room.get_swall():
        screen.blit(horz_wall, (x + 2*default_size, y + room_size - default_size))
        screen.blit(horz_wall, (x + room_size - 3*default_size, y + room_size - default_size))
        s_wall = pygame.Rect(x + default_size, y + room_size - default_size, room_size - 2*default_size, default_size)
        rect_list.append(s_wall)
    return rect_list

def draw_exit(screen,room):
    width, height = pygame.display.get_surface().get_size()
    room_size = width // 3
    default_size = width // 18
    if room.has_exit and Inventory.get_instance().has_all_pillars():
        x = room.get_location()[0] * room_size
        y = room.get_location()[1] * room_size +default_size
        door = pygame.image.load("exit_door.png")
        door_img = pygame.transform.scale(door, (default_size*2, default_size*2))
        door_rect = door_img.get_rect()
        door_rect.topleft = (x + (room_size/2) -45, y + (room_size/2)-45)
        screen.blit(door_img, (x + (room_size / 2) -45, y + (room_size / 2)-45))
        return door_rect
    else:
        return None

def draw_potion(screen, room):
    width, height = pygame.display.get_surface().get_size()
    room_size = width // 3
    default_size = width // 18
    x = room.get_location()[0] * room_size
    y = room.get_location()[1] * room_size +default_size
    if room.get_potion() is not None:
        potion = room.get_potion().get_image()
        potion_img = pygame.image.load(potion)
        potion_rect = (potion_img.get_rect())
        potion_rect.topleft = (x + (room_size/2) -30, y + (room_size/2) -30)
        screen.blit(potion_img, (x + (room_size/2) -30, y + (room_size/2) -30))
        return potion_rect
    else:
        return None

def draw_monster(screen, room):
    width, height = pygame.display.get_surface().get_size()
    room_size = width // 3
    default_size = width // 18
    x = room.get_location()[0] * room_size
    y = room.get_location()[1] * room_size + default_size
    if room.get_monster() is not None:
        monster = room.get_monster()
        monster_img = monster.get_image()
        img = pygame.image.load(monster_img)
        monster_rect = pygame.Rect(x + room_size/18, y + room_size/18 , room_size - (room_size/9), room_size - (room_size/9))
        screen.blit(img, (x + (room_size/2) -30, y + (room_size/2) -30))
        return monster_rect
    else:
        return None

def draw_toolbar(screen):
    width, height = pygame.display.get_surface().get_size()
    room_size = width // 3
    default_size = width // 18
    font = pygame.font.Font("8-bit-pusab.ttf", 15)

    image = pygame.Surface((width, default_size/1.5))
    image.fill((0,255,255))
    rect = image.get_rect()
    rect.topleft = (0, 0)
    screen.blit(image, rect)
    inventory_button = pygame.Rect(5,0,default_size*2, default_size)
    map_button = pygame.Rect(default_size * 4, 0, default_size * 2, default_size)
    save_button = pygame.Rect(default_size * 6, 0, default_size * 2, default_size)
    help_button = pygame.Rect(default_size * 8, 0, default_size * 2, default_size)
    quit_button = pygame.Rect(default_size * 10, 0, default_size * 2, default_size)
    rect_list = [inventory_button, map_button, save_button, help_button, quit_button]

    inventory_surface = font.render("Inventory", True, (255,255,255))
    map_surface = font.render("Map", True, (255, 255, 255))
    save_surface = font.render("Save", True, (255, 255, 255))
    help_surface = font.render("Help", True, (255, 255, 255))
    quit_surface = font.render("Quit", True, (255, 255, 255))

    screen.blit(inventory_surface, inventory_button)
    screen.blit(map_surface, map_button)
    screen.blit(save_surface, save_button)
    screen.blit(help_surface, help_button)
    screen.blit(quit_surface, quit_button)

    # Return the button rectangle for external use
    return rect_list
