import game_framework
from pico2d import *

import game_world

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (182.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class FlyState:

    @staticmethod
    def enter(bird, event):
        if event == RIGHT_DOWN:
            bird.dir == 1
            bird.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            bird.dir == -1
            bird.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            bird.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            bird.velocity += RUN_SPEED_PPS


    @staticmethod
    def exit(bird, event):
        pass

    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)


    @staticmethod
    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw(int(bird.frame) * 182, 0, 182, 150, bird.x, bird.y+200)
        else :
            bird.image.clip_composite_draw(int(bird.frame) * 182, 0, 182, 150, 0, 'v', bird.x, bird.y + 200)

next_state_table = {
    FlyState: {RIGHT_UP:  FlyState, LEFT_UP:  FlyState, RIGHT_DOWN:  FlyState, LEFT_DOWN:  FlyState,
                 SPACE:  FlyState}
  }

class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.font = load_font('ENCR10B.TTF', 16)
        self.image = load_image('bird_animation.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = FlyState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

