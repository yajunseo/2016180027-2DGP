import random
import json
import os

from pico2d import *

import game_framework
import game_world

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
    game_world.add_object(background, 0)
    game_world.add_object(dragon, 1)
    cnt = 2
    for i in monster1:
        game_world.add_object(i, cnt)
        cnt += 1


def exit():
    game_world.clear()


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
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






