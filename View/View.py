import pygame
from Model.Hero import Hero
from Model.Inventory import Inventory
pygame.init()

width = 810
height = 810
room_size = width//3
default_size = width // 18


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dungeon Adventure')

def get_camera_offset():
    x_min = max(0, Hero.get_instance().get_x() - width // 2)
    y_min = max(30, Hero.get_instance().get_y() - height // 2)
    camera_offset_x = min(room_size*3, x_min)
    camera_offset_y = min(room_size*3 + 30, y_min)
    return camera_offset_x, camera_offset_y


def draw_hero():
    camera_offset_x, camera_offset_y = get_camera_offset()

    hero_img = pygame.image.load(Hero.get_instance().get_image())
    scaled_hero = pygame.transform.scale(hero_img, (default_size, default_size))
    img_x = Hero.get_instance().get_x() - camera_offset_x
    img_y = Hero.get_instance().get_y() - camera_offset_y
    screen.blit(scaled_hero, (img_x, img_y))
    current_pillars = Inventory.get_instance().get_pillars()
    if len(current_pillars) > 0:
        locations = [(img_x -8, img_y - 30),
                     (img_x + 27, img_y -30),
                     (img_x - 30, img_y),
                     (img_x + 50, img_y)
                     ]
        i = 0
        for pillar in current_pillars:
            img = pygame.image.load(pillar.get_image())
            scaled_img = pygame.transform.scale(img, (30,30))
            screen.blit(scaled_img, (locations[i]))
            i+=1
    return scaled_hero.get_rect()

def draw_room(room):
    camera_offset_x, camera_offset_y = get_camera_offset()
    rect_list = []
    x = room.get_location()[0] * room_size - camera_offset_x
    y = room.get_location()[1] * room_size + default_size - camera_offset_y

    floor = pygame.image.load('floor.png')
    floor_img = pygame.transform.scale(floor, (room_size, room_size))
    floor_rect = floor_img.get_rect()
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

def draw_exit(room):
    camera_offset_x, camera_offset_y = get_camera_offset()
    if room.has_exit and Inventory.get_instance().has_all_pillars():
        x = room.get_location()[0] * room_size - camera_offset_x
        y = room.get_location()[1] * room_size +default_size -camera_offset_y
        door = pygame.image.load("exit_door.png")
        door_img = pygame.transform.scale(door, (default_size*2, default_size*2))
        door_rect = door_img.get_rect()
        door_rect.topleft = (x + (room_size/2) -45, y + (room_size/2)-45)
        screen.blit(door_img, (x + (room_size / 2) -45, y + (room_size / 2)-45))
        return door_rect
    else:
        return None

def draw_potion(room):
    camera_offset_x, camera_offset_y = get_camera_offset()
    x = room.get_location()[0] * room_size - camera_offset_x
    y = room.get_location()[1] * room_size +default_size -camera_offset_y
    if room.get_potion() is not None:
        potion = room.get_potion().get_image()
        potion_img = pygame.image.load(potion)
        potion_rect = (potion_img.get_rect())
        potion_rect.center = (x + (room_size/2) -30, y + (room_size/2) -30)
        screen.blit(potion_img, (x + (room_size/2) -30, y + (room_size/2) -30))
        return potion_rect
    else:
        return None

def draw_monster(room):
    camera_offset_x, camera_offset_y = get_camera_offset()
    x = room.get_location()[0] * room_size - camera_offset_x
    y = room.get_location()[1] * room_size + default_size - camera_offset_y
    if room.get_monster() is not None:
        monster = room.get_monster()
        monster_img = monster.get_image()
        img = pygame.image.load(monster_img)
        img = pygame.transform.scale(img, (1.5*default_size, 1.5*default_size))
        monster_rect = pygame.Rect(x + room_size/18, y + room_size/18 , room_size - (room_size/9), room_size - (room_size/9))
        monster_rect.center = (x + (room_size/2) -30, y + (room_size/2) -30)
        screen.blit(img, (x + (room_size/2) -30, y + (room_size/2) -30))
        return monster_rect
    else:
        return None

def draw_toolbar():

    font = pygame.font.Font("8-bit-pusab.ttf", 15)

    image = pygame.Surface((width, default_size/1.5))
    image.fill((118,59,54))
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
def draw_inventory():

    row_height = 4*default_size
    font = pygame.font.Font("8-bit-pusab.ttf", 15)

    image = pygame.Surface((width, row_height))
    image.fill((250,197,143))
    rect = image.get_rect()
    rect.topleft = (0, default_size/1.5)
    screen.blit(image, rect)
    potion_label = pygame.Rect(5, default_size/1.5 + default_size, default_size*2, default_size)
    pillar_label = pygame.Rect(5, default_size/1.5 + 3*default_size, default_size * 2, default_size)

    potion_surface = font.render("Potions:", True, (255,255,255))
    pillar_surface = font.render("Pillars:", True, (255, 255, 255))


    screen.blit(potion_surface, potion_label)
    screen.blit(pillar_surface, pillar_label)
    current_pillars = Inventory.get_instance().get_pillars()
    i = 3
    for pillar in current_pillars:
        img = pygame.image.load(pillar.get_image())
        scaled_img = pygame.transform.scale(img, (30, 30))
        screen.blit(scaled_img, (default_size*i, default_size/1.5 + 3*default_size))
        i += 2

    health_rects = []
    current_health_potions = Inventory.get_instance().get_health_potions()
    i = 3
    for potion in current_health_potions:
        img = pygame.image.load(potion.get_image())
        scaled_img = pygame.transform.scale(img, (30, 30))
        rect = scaled_img.get_rect()
        rect.topleft = (default_size * i, default_size / 1.5 + default_size)
        screen.blit(scaled_img, (default_size * i, default_size / 1.5 + default_size))
        i += 2
        health_rects.append(rect)

    vision_rects = []
    current_vision_potions = Inventory.get_instance().get_vision_potions()
    i = 3
    for potion in current_vision_potions:
        img = pygame.image.load(potion.get_image())
        scaled_img = pygame.transform.scale(img, (30, 30))
        rect = scaled_img.get_rect()
        rect.topleft = (default_size * i, default_size / 1.5 + 2*default_size)
        screen.blit(scaled_img, (default_size * i, default_size / 1.5 + 2*default_size))
        i += 2
        vision_rects.append(rect)

    # Return the button rectangle for external use
    return health_rects, vision_rects
def draw_vision():
    img = pygame.image.load("vision.png")
    screen.blit(img, (0,30))