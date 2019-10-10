from pico2d import *


map_width, map_height = 960, 600
open_canvas(map_width, map_height)

stage1 = load_image('stage1.png')
character = load_image('character1.png')
x = 0
y = 0.
frame = 0
running = True

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


while running:
    clear_canvas()
    stage1.draw(map_width//2, map_height//2)
    character.clip_draw(frame * 60, 10, 60, 60, 300, 300)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
