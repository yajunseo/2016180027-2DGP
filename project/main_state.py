import random
import json
import os

from pico2d import *

import game_framework


from dragon import Dragon
from background import Background
from monster1 import Monster1


name = "main_state"

dragon = None
background = None
monster1 = None

def enter():
    global dragon, background, monster1
    dragon = Dragon()
    background = Background()
    monster1 = [Monster1() for i in range(6)]



def exit():
    global dragon, background, monster1
    del dragon
    del background
    del monster1


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
    for mon in monster1:
        mon.update()

def draw():
    clear_canvas()
    background.draw()
    for mon in monster1:
        mon.draw()
    dragon.draw()
    update_canvas()






