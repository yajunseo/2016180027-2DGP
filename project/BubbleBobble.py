from pico2d import *


map_width, map_height = 960, 600
open_canvas(map_width, map_height)

stage1 = load_image('stage1.png')
move_left = load_image('move.png')
move_right = load_image('move-r.png')
x = 300
y = 0
frame = 0
running = True
side = 1
dir = 0

def handle_events():
    global running
    global x, y
    global dir
    global side
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            run = 1
            if event.key == SDLK_LEFT:
                dir -= 1
                side = -1
            if event.key == SDLK_RIGHT:
                dir += 1
                side = 1
        if event.type == SDL_KEYUP:
            run = 0
            if event.key == SDLK_LEFT:
                dir += 1
            if event.key == SDLK_RIGHT:
                dir -= 1





while running:
    clear_canvas()
    stage1.draw(map_width//2, map_height//2)

    if x > 70 and x < 900:
        if dir < 0:
            move_left.clip_draw(frame * 47 , 10, 40, 40, x, 30)
        elif dir > 0:
            move_right.clip_draw(frame * 47, 10, 40, 40, x, 30)
        else:
            if side == 1:
                move_right.clip_draw(frame * 47, 10, 40, 40, x, 30)
            elif side == -1:
                move_left.clip_draw(frame * 47, 10, 40, 40, x, 30)
        x += dir * 2
        if x == 70:
            x += 10
        if x == 900:
            x -= 10
    else:
        if side == 1:
            move_right.clip_draw(frame * 47, 10, 40, 40, x, 30)
        elif side == -1:
            move_left.clip_draw(frame * 47, 10, 40, 40, x, 30)


    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
