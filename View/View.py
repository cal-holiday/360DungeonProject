import pygame
from Model.Hero import Hero
from Model.Inventory import Inventory
pygame.init()

SCREEN_WIDTH = 810
SCREEN_HEIGHT = 820
ROOM_SIZE = SCREEN_WIDTH//6
DEFAULT_SIZE = SCREEN_WIDTH // 36


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dungeon Adventure')




def draw_hero():
    hero_img = pygame.image.load(Hero.get_instance().get_image())
    scaled_hero = pygame.transform.scale(hero_img, (DEFAULT_SIZE, DEFAULT_SIZE))
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

def draw_room(room):

    rect_list = []
    x = room.get_location()[0] * ROOM_SIZE
    y = room.get_location()[1] * ROOM_SIZE + DEFAULT_SIZE

    floor = pygame.image.load('floor.png')
    floor_img = pygame.transform.scale(floor, (ROOM_SIZE - 5, ROOM_SIZE - 5))
    screen.blit(floor_img, (x, y))
    corner = pygame.image.load('corner.png')
    corner = pygame.transform.scale(corner, (DEFAULT_SIZE, DEFAULT_SIZE))
    screen.blit(corner, (x, y))
    screen.blit(corner, (x + ROOM_SIZE - DEFAULT_SIZE, y))
    screen.blit(corner, (x, y + ROOM_SIZE - DEFAULT_SIZE))
    screen.blit(corner, (x + ROOM_SIZE - DEFAULT_SIZE, y + ROOM_SIZE -DEFAULT_SIZE))

    wall = pygame.image.load('wall.png')
    vert_wall = pygame.transform.scale(wall, (DEFAULT_SIZE, DEFAULT_SIZE))
    horz_wall = pygame.transform.rotate(vert_wall, 90)
    default_vert_walls = [(x, y + DEFAULT_SIZE), #top left corner bottom
                     (x, y + ROOM_SIZE - 2*DEFAULT_SIZE), #bottom left corner top
                     (x + ROOM_SIZE - DEFAULT_SIZE, y + DEFAULT_SIZE),#top right corner bottom
                     (x + ROOM_SIZE - DEFAULT_SIZE, y + ROOM_SIZE- 2*DEFAULT_SIZE), #bottom right corner top
                     ]
    default_horz_walls = [(x + DEFAULT_SIZE, y), #top left corner right
                     (x + ROOM_SIZE - 2*DEFAULT_SIZE, y), #top right corner left
                     (x + DEFAULT_SIZE, y + ROOM_SIZE- DEFAULT_SIZE), #bottom left corner right
                     (x + ROOM_SIZE- 2*DEFAULT_SIZE, y + ROOM_SIZE - DEFAULT_SIZE) #bottom right corner left
                     ]
    for location in default_vert_walls:
        rect = pygame.Rect(location[0], location[1], DEFAULT_SIZE, DEFAULT_SIZE)
        screen.blit(vert_wall, location)
        rect_list.append(rect)
    for location in default_horz_walls:
        rect = pygame.Rect(location[0], location[1], DEFAULT_SIZE, DEFAULT_SIZE)
        screen.blit(horz_wall, location)
        rect_list.append(rect)

    if room.get_nwall():
        screen.blit(horz_wall, (x + 2*DEFAULT_SIZE, y))
        screen.blit(horz_wall, (x + ROOM_SIZE - 3*DEFAULT_SIZE, y))
        n_wall = pygame.Rect(x + DEFAULT_SIZE, y, ROOM_SIZE- 2*DEFAULT_SIZE, DEFAULT_SIZE)
        rect_list.append(n_wall)

    if room.get_wwall():
        screen.blit(vert_wall, (x, y + 2*DEFAULT_SIZE))
        screen.blit(vert_wall, (x, y + ROOM_SIZE - 3*DEFAULT_SIZE))
        w_wall = pygame.Rect(x, y + DEFAULT_SIZE, DEFAULT_SIZE, ROOM_SIZE - 2*DEFAULT_SIZE)
        rect_list.append(w_wall)

    if room.get_ewall():
        screen.blit(vert_wall, (x + ROOM_SIZE - DEFAULT_SIZE, y + 2*DEFAULT_SIZE))
        screen.blit(vert_wall, (x + ROOM_SIZE - DEFAULT_SIZE, y + ROOM_SIZE - 3*DEFAULT_SIZE))
        e_wall = pygame.Rect(x + ROOM_SIZE - DEFAULT_SIZE, y + DEFAULT_SIZE, DEFAULT_SIZE, ROOM_SIZE - 2*DEFAULT_SIZE)
        rect_list.append(e_wall)

    if room.get_swall():
        screen.blit(horz_wall, (x + 2*DEFAULT_SIZE, y + ROOM_SIZE - DEFAULT_SIZE))
        screen.blit(horz_wall, (x + ROOM_SIZE - 3*DEFAULT_SIZE, y + ROOM_SIZE - DEFAULT_SIZE))
        s_wall = pygame.Rect(x + DEFAULT_SIZE, y + ROOM_SIZE - DEFAULT_SIZE, ROOM_SIZE - 2*DEFAULT_SIZE, DEFAULT_SIZE)
        rect_list.append(s_wall)
    return rect_list

def draw_exit(room):
    if room.has_exit and Inventory.get_instance().has_all_pillars():
        x = room.get_location()[0] * ROOM_SIZE
        y = room.get_location()[1] * ROOM_SIZE +DEFAULT_SIZE
        door = pygame.image.load("exit_door.png")
        door_img = pygame.transform.scale(door, (DEFAULT_SIZE*2, DEFAULT_SIZE*2))
        door_rect = door_img.get_rect()
        door_rect.topleft = (x + (ROOM_SIZE/2) -45, y + (ROOM_SIZE/2)-45)
        screen.blit(door_img, (x + (ROOM_SIZE / 2) -45, y + (ROOM_SIZE / 2)-45))
        return door_rect
    else:
        return None

def draw_potion(room):
    x = room.get_location()[0] * ROOM_SIZE
    y = room.get_location()[1] * ROOM_SIZE +DEFAULT_SIZE
    if room.get_potion() is not None:
        potion = room.get_potion().get_image()
        potion_img = pygame.image.load(potion)
        potion_rect = (potion_img.get_rect())
        potion_rect.topleft = (x + (ROOM_SIZE/2) -30, y + (ROOM_SIZE/2) -30)
        screen.blit(potion_img, (x + (ROOM_SIZE/2) -30, y + (ROOM_SIZE/2) -30))
        return potion_rect
    else:
        return None

def draw_monster(room):
    x = room.get_location()[0] * ROOM_SIZE
    y = room.get_location()[1] * ROOM_SIZE + DEFAULT_SIZE
    if room.get_monster() is not None:
        monster = room.get_monster()
        monster_img = monster.get_image()
        img = pygame.image.load(monster_img)
        monster_rect = pygame.Rect(x + ROOM_SIZE/18, y + ROOM_SIZE/18 , ROOM_SIZE - (ROOM_SIZE/9), ROOM_SIZE - (ROOM_SIZE/9))
        screen.blit(img, (x + (ROOM_SIZE/2) -30, y + (ROOM_SIZE/2) -30))
        return monster_rect
    else:
        return None

def draw_toolbar():
    font = pygame.font.Font("8-bit-pusab.ttf", 15)

    image = pygame.Surface((SCREEN_WIDTH, DEFAULT_SIZE/1.5))
    image.fill((0,255,255))
    rect = image.get_rect()
    rect.topleft = (0, 0)
    screen.blit(image, rect)
    inventory_button = pygame.Rect(5,0,DEFAULT_SIZE*2, DEFAULT_SIZE)
    map_button = pygame.Rect(DEFAULT_SIZE * 4, 0, DEFAULT_SIZE * 2, DEFAULT_SIZE)
    save_button = pygame.Rect(DEFAULT_SIZE * 6, 0, DEFAULT_SIZE * 2, DEFAULT_SIZE)
    help_button = pygame.Rect(DEFAULT_SIZE * 8, 0, DEFAULT_SIZE * 2, DEFAULT_SIZE)
    quit_button = pygame.Rect(DEFAULT_SIZE * 10, 0, DEFAULT_SIZE * 2, DEFAULT_SIZE)
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

