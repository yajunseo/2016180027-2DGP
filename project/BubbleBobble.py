from pico2d import *


map_width, map_height = 960, 600
open_canvas(map_width, map_height)

stage1 = load_image('stage1.png')
move_left = load_image('move.png')
move_right = load_image('move-r.png')
x = 300
y = 0
temp_x = 0
temp_y = 0
frame = 0
running = True
look_side = 1
dir = 0
is_jump = 0
block_size = 70


class Hero:
    def __init__(self):
        self.x, self.y = 300, 30
        self.jump_x, self.jump_y = self.x, self.y
        self.frame = 0

    def update(self):
        global is_jump
        global dir
        if is_jump == 1:
            self.jump_y = self.y + 200
            if dir == 0:
                if look_side == 1:
                    self.jump_x = self.x + 5
                elif look_side == -1:
                    self.jump_x = self.x - 5
            else:
                if look_side == 1:
                    self.jump_x = self.x + 200
                elif look_side == -1:
                    self.jump_x = self.x - 200

        self.frame = (self.frame + 1) % 7

    def draw(self):
        global is_jump
        global block_size
        global map_width
        global dir
        global look_side

        if is_jump == 1:
            p1, p2, p3 = (self.x, self.y), ((self.jump_x + self.x) / 2, self.jump_y), (self.jump_x, self.y)
            t = 0
            p1_x, p1_y = p1[0], p1[1]
            while t < 998 / 1000:
                for i in range(0, 1000 + 1, 2):
                    t = i / 1000
                    temp_x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
                    temp_y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]

                    clear_canvas()
                    stage1.draw(map_width // 2, map_height // 2)

                    if p1_x < temp_x:
                        move_right.clip_draw(self.frame * 47, 10, 40, 40, p1_x, p1_y)
                    elif p1_x >= temp_x:
                        move_left.clip_draw(self.frame * 47, 55, 40, 40, p1_x, p1_y)
                    update_canvas()


                    p1_y = temp_y

                    if (temp_x > block_size) and (temp_x < (map_width - block_size)):
                        p1_x = temp_x

                    else:
                        if p1_x <= block_size:
                            p1_x = (block_size + 10)
                        if p1_x >= (map_width - block_size):
                            p1_x = (map_width - block_size - 10)
                    self.frame = (self.frame + 1) % 7
            is_jump = 0
            self.x = p1_x
            self.y = p1_y

        else:
            if (self.x >= (block_size)) and self.x <= (map_width - block_size):
                if dir < 0:
                    move_left.clip_draw(self.frame * 47, 55, 40, 40, self.x, self.y)
                elif dir > 0:
                    move_right.clip_draw(self.frame * 47, 10, 40, 40,self.x, self.y)
                else:
                    if look_side == 1:
                        move_right.clip_draw(self.frame * 47, 10, 40, 40, self.x, self.y)
                    elif look_side == -1:
                        move_left.clip_draw(self.frame * 47, 55, 40, 40, self.x, self.y)
                self.x += dir * 2
                if self.x <= block_size:
                    self.x += 10
                if self.x >= map_width - block_size:
                    self.x -= 10
            else:
                if look_side == 1:
                    move_right.clip_draw(self.frame * 47, 10, 40, 40, self.x, self.y)
                elif look_side == -1:
                    move_left.clip_draw(self.frame * 47, 55, 40, 40, self.x, self.y)



def handle_events():
    global running
    global x, y
    global dir
    global look_side
    global is_jump
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            run = 1
            if event.key == SDLK_LEFT:
                dir -= 1
                look_side = -1
            if event.key == SDLK_RIGHT:
                dir += 1
                look_side = 1
            if event.key == SDLK_SPACE:
                is_jump = 1

        if event.type == SDL_KEYUP:
            run = 0
            if event.key == SDLK_LEFT:
                dir += 1
            if event.key == SDLK_RIGHT:
                dir -= 1



main_hero = Hero()


while running:

    handle_events()
    update_canvas()
    main_hero.update()
    clear_canvas()
    stage1.draw(map_width//2, map_height//2)
    main_hero.draw()

