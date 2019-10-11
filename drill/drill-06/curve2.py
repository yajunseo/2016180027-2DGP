from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x = x + 10
            elif event.key == SDLK_LEFT:
                x = x - 10
            elif event.key == SDLK_ESCAPE:
                running = False
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y = 0
frame = 0
cx, cy = 0, 0
def draw_curve_3_points(p1, p2, p3, p4):
    global cx, cy
    global x, y
    t = 0
    global frame
    global running
    while t < 9998 / 10000:
        for i in range(0, 10000 + 1, 2):


            t = i / 10000
            cx = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
            cy = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

            if x < cx:
                character.clip_draw(frame * 100, 100 * 1, 100, 100, cx, cy)
            elif x >= cx:
                character.clip_draw(frame * 100, 0 * 1, 100, 100, cx, cy)
            update_canvas()
            x, y = cx, cy
            frame = (frame + 1) % 8


p = [(random.randint(20, 1000), random.randint(20, 1000)) for n in range(10)]

r = 0

while running:
    update_canvas()
    while True:
        draw_curve_3_points(p[r % 10], p[(r+1) % 10], p[(r+2) % 10], p[(r+3) % 10])
        r += 1


    handle_events()

close_canvas()

