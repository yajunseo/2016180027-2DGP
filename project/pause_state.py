import game_framework
from pico2d import *
import main_state

name = "PauseState"
image = None
flick = 0

def enter():
    global image
    image = load_image('pause1.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p ):
                game_framework.pop_state()


def draw():
    global flick
    flick += 1
    clear_canvas()
    main_state.draw()
    if flick % 2 == 0:
        image.draw(400, 300, 300, 300)
    if flick == 10:
        flick = 0
    update_canvas()






def update():
    pass


def pause():
    pass


def resume():
    pass






