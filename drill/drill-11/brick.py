import random
from pico2d import *
import game_world
import game_framework


class Brick:

    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 400, 200
        self.dir = 1

    def get_bb(self):
        return self.x - 80, self.y - 20, self.x + 80, self.y + 20
        return 0, 0, 0, 0

    def draw(self):
        self.image.draw(self.x, self.y, 160, 40)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.dir == 1:
            self.x += 1
            if self.x >= 700:
                self.dir = -1
        else:
            self.x -= 1
            if self.x <= 100:
                self.dir = 1

    # fill here for def stop


