from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)

cursor = load_image('hand_arrow.png')
background = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


def move(p1, p2):
    global x, y
    global dir
    global frame
    global side
    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]

        clear_canvas()
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if side == 1:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif side == -1:
            character.clip_draw(frame * 100, 000 * 1, 100, 100, x, y)

        update_canvas()
        handle_events()
        frame = (frame + 1) % 8

        if i == 100:
            dir = 0



def handle_events():
    global running
    global x, y
    global cursor_x
    global cursor_y
    global side
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_MOUSEMOTION:
            cursor_x,cursor_y = event.x, KPU_HEIGHT - 1 - event.y
        if event.type == SDL_MOUSEBUTTONUP:
            cursor_x, cursor_y = event.x, KPU_HEIGHT - event.y
            dir = 1
            if cursor_x >= x:
                side = 1
            else:
                side = -1

            move((x, y), (cursor_x, cursor_y))








running = True
frame = 0
x = KPU_WIDTH//2
y = KPU_HEIGHT//2
dir = 0
side = 1
cursor_x = 0
cursor_y = 0
hide_cursor()



while running:
    clear_canvas()
    background.draw(KPU_WIDTH//2, KPU_HEIGHT//2)
    cursor.draw(cursor_x,cursor_y)

    if (x >= 25 and x <= 1255 and y>=25 and y<= 999):
        if dir == 1:
            if side == 1:
                character.clip_draw(frame * 100, 100 * 1, 100, 100, x-25, y+25)
            elif side == -1:
                character.clip_draw(frame * 100, 000 * 1, 100, 100, x-25, y+25)

        elif dir == 0:
            if side == 1:
                character.clip_draw(frame * 100, 300 * 1, 100, 100, x-25, y+25)
            elif side == -1:
                character.clip_draw(frame * 100, 200 * 1, 100, 100, x-25, y+25)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

close_canvas()





