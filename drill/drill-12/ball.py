import random
from pico2d import *
import game_world
import game_framework


class Ball:
    image = None

    def __init__(self, x, y):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = x, y

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
        return 0, 0, 0, 0

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

# fill here
# class BigBall
class BigBall(Ball):

    image = None

    def __init__(self, x, y):
        if BigBall.image is None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = x, y

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
