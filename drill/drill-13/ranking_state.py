import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import world_build_state
name = "Ranking_State"

top10_ranking_list = []
ranking_data = None
font = None

import main_state

def enter():
    global top10_ranking_list, font, ranking_data
    ranking_data = main_state.get_live_data()
    with open('ranking_data.json', 'r') as f:
        top10_ranking_list = json.load(f)

    top10_ranking_list.append(ranking_data)
    top10_ranking_list.sort(reverse=True)

    font = load_font('ENCR10B.TTF', 20)

    with open('ranking_data.json', 'w') as f:
        json.dump(top10_ranking_list, f)
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
            game_world.save()
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_world.save()
            game_framework.change_state(world_build_state)


def update():
    pass


def draw():
    clear_canvas()

    font.draw(0, 800, "Total Ranking")
    for i in range(min(10, len(top10_ranking_list))):
        font.draw(0, 700 - i * 15, "# " + str(i + 1) + ".")
        font.draw(80 , 700 - i * 15, str(top10_ranking_list[i]))
   #     for j in range(10):
   #         if
  #          font.draw(80 + j*2, 700 - i * 15, str(top10_ranking_list[i][j]))

    update_canvas()
    pass




