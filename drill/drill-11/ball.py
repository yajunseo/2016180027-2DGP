import random
from pico2d import *
import game_world
import game_framework
import main_state


class Ball:
    image = None
    MIN_FALL_SPEED = 50
    # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 200

    # 200 pps = 6 meter per sec

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 800 - 1), 60, 0
        self.distance = 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
        return 0, 0, 0, 0

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time
        self.distance = main_state.brick.x - self.x

    def stop(self):
        self.fall_speed = 0

    def stop_brick(self):
        self.fall_speed = 0
        self.x = main_state.brick.x - self.distance

    def start_update(self):
        self.fall_speed = 100

    # fill here for def stop


# fill here
# class BigBall
class BigBall(Ball):
    MIN_FALL_SPEED = 50
    # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 200
    # 200 pps = 6 meter per sec
    image = None

    def __init__(self):
        if BigBall.image is None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 800 - 1), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED,
                                         BigBall.MAX_FALL_SPEED)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
