from pico2d import *


map_width, map_height = 960, 600
open_canvas(map_width, map_height)

stage1 = load_image('stage1.png')
move_left = load_image('move.png')
move_right = load_image('move-r.png')
x = 300
y = 0
jump_x = 0
jump_y = 0
frame = 0
running = True
side = 1
dir = 0

def draw_curve_3_points(p1, p2, p3):
    global cx, cy
    global x, y
    t = 0
    global frame
    global running
    while t < 998 / 1000:
        for i in range(0, 1000 + 1, 2):
            t = i / 1000


            cx = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
            cy = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]

            clear_canvas()
            stage1.draw(map_width // 2, map_height // 2)

            if x < cx:
                move_right.clip_draw(frame * 47, 10, 40, 40, x, y)
            elif x >= cx:
                move_left.clip_draw(frame * 47 , 55, 40, 40, x, y)
            update_canvas()

            y = cy
            if cx > 70 and cx < 900:
                x = cx

            else:
                if x == 70:
                    x == 80
                if x >= 900:
                    x == 890
            frame = (frame + 1) % 7


def handle_events():
    global running
    global x, y
    global jump_x, jump_y
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
            if event.key == SDLK_SPACE:
                jump_y = y + 200
                if side == 1:
                    jump_x = x + 200
                else:
                    jump_x = x - 200
                draw_curve_3_points((x, y), ((jump_x + x)/2, jump_y), (jump_x, y))

        if event.type == SDL_KEYUP:
            run = 0
            if event.key == SDLK_LEFT:
                dir += 1
            if event.key == SDLK_RIGHT:
                dir -= 1





while running:
    clear_canvas()
    stage1.draw(map_width//2, map_height//2)

    if x >= 70 and x <= 900:
        if dir < 0:
            move_left.clip_draw(frame * 47 , 55, 40, 40, x, 30)
        elif dir > 0:
            move_right.clip_draw(frame * 47, 10, 40, 40, x, 30)
        else:
            if side == 1:
                move_right.clip_draw(frame * 47, 10, 40, 40, x, 30)
            elif side == -1:
                move_left.clip_draw(frame * 47, 55, 40, 40, x, 30)
        x += dir * 2
        if x <= 70:
            x += 10
        if x >= 900:
            x -= 10
    else:
        if side == 1:
            move_right.clip_draw(frame * 47, 10, 40, 40, x, 30)
        elif side == -1:
            move_left.clip_draw(frame * 47, 55, 40, 40, x, 30)


    update_canvas()
    frame = (frame + 1) % 7
    handle_events()
