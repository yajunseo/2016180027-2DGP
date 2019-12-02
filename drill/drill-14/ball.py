import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1600-1), random.randint(0, 1200-1)
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.bg = 0
        self.cx, self.cy = 0, 0

    def set_background(self, bg):
        self.bg = bg

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x - self.bg.window_left, self.y - self.bg.window_bottom)
        # fill here for draw

    def update(self):
        pass



    #fill here for def stop


# fill here
# class BigBall