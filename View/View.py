import pygame

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dungeon Adventure')




def draw_hero(hero):
    hero_img = pygame.image.load(hero.get_image())
    screen.blit(hero_img, (hero.get_x(),hero.get_y()))

def draw_room(room, room_size):
    rect_list = []
    default_size = 50
    x = room.get_location()[0] * room_size
    y = room.get_location()[1] * room_size

    screen.blit(pygame.image.load('../Controller/floor.png'), (x, y))
    corner = pygame.image.load('../Controller/corner.png')
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
                     (x + room_size - default_size, y + room_size - 2*default_size), #bottom right corner top
                     ]
    default_horz_walls = [(x + default_size, y), #top left corner right
                     (x + room_size - 2*default_size, y), #top right corner left
                     (x + default_size, y + room_size - default_size), #bottom left corner right
                     (x + room_size - 2*default_size, y + room_size - default_size) #bottom right corner left
                     ]
    for location in default_vert_walls:
        screen.blit(vert_wall, location)
    for location in default_horz_walls:
        screen.blit(horz_wall, location)
    if room.get_nwall():
        screen.blit(horz_wall, (x + 2*default_size, y))
        screen.blit(horz_wall, (x + room_size - 3*default_size, y))
        n_wall = pygame.Rect(x + default_size, y, room_size - 2*default_size, default_size)
        rect_list.append(n_wall)
    else:
        n_wall1 = pygame.Rect(default_horz_walls[0][0], default_horz_walls[0][1], default_size, default_size)
        n_wall2 = pygame.Rect(default_horz_walls[1][0], default_horz_walls[1][1], default_size, default_size)
        rect_list.append(n_wall1)
        rect_list.append(n_wall2)

    if room.get_wwall():
        screen.blit(vert_wall, (x, y + 2*default_size))
        screen.blit(vert_wall, (x, y + room_size - 3*default_size))
        w_wall = pygame.Rect(x, y + default_size, default_size, room_size - 2*default_size)
        rect_list.append(w_wall)
    else:
        w_wall1 = pygame.Rect(default_vert_walls[0][0], default_vert_walls[0][1], default_size, default_size)
        w_wall2 = pygame.Rect(default_vert_walls[1][0], default_vert_walls[1][1], default_size, default_size)
        rect_list.append(w_wall1)
        rect_list.append(w_wall2)

    if room.get_ewall():
        screen.blit(vert_wall, (x + room_size - default_size, y + 2*default_size))
        screen.blit(vert_wall, (x + room_size - default_size, y + room_size - 3*default_size))
        e_wall = pygame.Rect(x + room_size - default_size, y + default_size, default_size, room_size - 2*default_size)
        rect_list.append(e_wall)
    else:
        e_wall1 = pygame.Rect(default_vert_walls[2][0], default_vert_walls[2][1], default_size, default_size)
        e_wall2 = pygame.Rect(default_vert_walls[3][0], default_vert_walls[3][1], default_size, default_size)
        rect_list.append(e_wall1)
        rect_list.append(e_wall2)

    if room.get_swall():
        screen.blit(horz_wall, (x + 2*default_size, y + room_size - default_size))
        screen.blit(horz_wall, (x + room_size - 3*default_size, y + room_size - default_size))
        s_wall = pygame.Rect(x + default_size, y + room_size - default_size, room_size - 2*default_size, default_size)
        rect_list.append(s_wall)
    else:
        s_wall1 = pygame.Rect(default_horz_walls[2][0], default_horz_walls[2][1], default_size, default_size)
        s_wall2 = pygame.Rect(default_horz_walls[3][0], default_horz_walls[3][1], default_size, default_size)
        rect_list.append(s_wall1)
        rect_list.append(s_wall2)
    return rect_list






