import random
import json
import os

from pico2d import *

import game_framework
import stage1_state

name = "MainState"

dragon = None
stage = None


def enter():
    pass

def exit():
    pass

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

game_framework.change_state(stage1_state)

def update():
    pass

def draw():
    pass






