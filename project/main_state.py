import random
import json
import os

from pico2d import *

import game_framework


from dragon import Dragon


name = "MainState"

dragon = None


def enter():
    global dragon
    dragon = Dragon()


def exit():
    global dragon
    del dragon


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            dragon.handle_event(event)



def update():
    dragon.update()

def draw():
    clear_canvas()
    dragon.draw()
    update_canvas()






