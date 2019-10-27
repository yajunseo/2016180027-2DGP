from pico2d import *
import random


class Monster1:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 12)
        self.frame_speed = 0
        if Monster1.image == None:
            Monster1.image = load_image('sprite\\Enemy\\walker.png')


    def update(self):
        Monster1.frame_speed += 1
        if Monster1.frame_speed > 30:
            Monster1.frame = (Monster1.frame + 1) % 12
            Monster1.frame_speed = 0
        self.x += 5

    def draw(self):
        if Monster1.dir == 1:
            Monster1.image.clip_draw(Monster1.frame * 16, 128, 16, 16, Monster1.x, Monster1.y, 50, 50)
        else:
            Monster1.image.clip_draw(Monster1.frame * 16, 144, 16, 16, Monster1.x, Monster1.y, 50, 50)



