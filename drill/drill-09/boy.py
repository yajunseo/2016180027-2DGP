from pico2d import *

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, LSHIFT_UP,\
    LSHIFT_DOWN, RSHIFT_UP, RSHIFT_DOWN = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_LSHIFT): LSHIFT_UP,
    (SDL_KEYDOWN, SDLK_LSHIFT): LSHIFT_DOWN,
    (SDL_KEYUP, SDLK_RSHIFT): RSHIFT_UP,
    (SDL_KEYDOWN, SDLK_RSHIFT): RSHIFT_DOWN
}


# Boy States
class IdleState:
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else: boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)


class RunState:
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


class DashState:
    @staticmethod
    def enter(boy, event):
        boy.Dash_timer = 150

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.Dash_timer -= 1
        boy.x += boy.velocity * 3
        boy.x = clamp(25, boy.x, 800 - 25)
        if boy.Dash_timer == 0:
            boy.add_event(LSHIFT_UP)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState,
                LEFT_DOWN: RunState,
                LSHIFT_DOWN: IdleState, LSHIFT_UP: IdleState,
                RSHIFT_DOWN: IdleState, RSHIFT_UP: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState,
               RIGHT_DOWN: IdleState,  LSHIFT_DOWN: DashState, LSHIFT_UP: RunState,
               RSHIFT_DOWN: DashState, RSHIFT_UP: RunState},

    DashState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: IdleState,
                LEFT_DOWN: IdleState,
                LSHIFT_DOWN: DashState, LSHIFT_UP: RunState,
                RSHIFT_DOWN: DashState, RSHIFT_UP: RunState}
}


class Boy:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.Dash_timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def update_state(self,  state):
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def change_state(self,  state):
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

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




#########################################################################################

map_width, map_height = 960, 600
open_canvas(map_width, map_height)

stage1 = load_image('stage1.png')

x = 300
y = 0
temp_x = 0
temp_y = 0
frame = 0
running = True
look_side = 1
dir = 0
is_jump = 0
block_size = 70


class Hero:
    def __init__(self):
        self.x, self.y = 300, 50
        self.jump_x, self.jump_y = self.x, self.y
        self.frame = 0
        self.move = load_image('sprite\\Character\\character.png')
        self.stage = Background()

    def update(self):
        global is_jump
        global dir
        if is_jump == 1:
            self.jump_y = self.y + 200
            if dir == 0:
                if look_side == 1:
                    self.jump_x = self.x + 5
                elif look_side == -1:
                    self.jump_x = self.x - 5
            else:
                if look_side == 1:
                    self.jump_x = self.x + 200
                elif look_side == -1:
                    self.jump_x = self.x - 200

        self.frame = (self.frame + 1) % 16

    def draw(self):
        global is_jump
        global block_size
        global map_width, map_height
        global dir
        global look_side

        if is_jump == 1:
            p1, p2, p3 = (self.x, self.y), ((self.jump_x + self.x) / 2, self.jump_y), (self.jump_x, self.y)
            t = 0
            p1_x, p1_y = p1[0], p1[1]
            while t < 998 / 1000:
                for i in range(0, 1000 + 1, 2):
                    t = i / 1000
                    temp_x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
                    temp_y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]

                    clear_canvas()
                    self.stage.draw()

                    if p1_x < temp_x:
                        self.move.clip_draw(self.frame * 16, 0, 16, 16, p1_x, p1_y, 60, 60)
                    elif p1_x >= temp_x:
                        self.move.clip_draw(self.frame * 16, 16, 16, 16, p1_x, p1_y, 60, 60)
                    update_canvas()


                    p1_y = temp_y

                    if (temp_x > block_size) and (temp_x < (map_width - block_size)):
                        p1_x = temp_x

                    else:
                        if p1_x <= block_size:
                            p1_x = (block_size + 10)
                        if p1_x >= (map_width - block_size):
                            p1_x = (map_width - block_size - 10)
                    self.frame = (self.frame + 1) % 7
            is_jump = 0
            self.x = p1_x
            self.y = p1_y

        else:
            if (self.x >= (block_size)) and self.x <= (map_width - block_size):
                if dir < 0:
                    self.move.clip_draw(self.frame * 16, 144, 16, 16, self.x, self.y, 60, 60)
                elif dir > 0:
                    self.move.clip_draw(self.frame * 16, 128, 16, 16, self.x, self.y, 60, 60)
                else:
                    if look_side == 1:
                        self.move.clip_draw(self.frame * 16, 160, 16,16, self.x, self.y, 60, 60)
                    elif look_side == -1:
                        self.move.clip_draw(self.frame * 16, 176, 16, 16, self.x, self.y, 60, 60)
                self.x += dir * 2
                self.x = clamp(block_size, self.x, map_width - block_size)
            else:
                if look_side == 1:
                    self.move.clip_draw(self.frame * 16, 160, 16, 16, self.x, self.y, 60, 60)
                elif look_side == -1:
                    self.move.clip_draw(self.frame * 16, 176, 16, 16, self.x, self.y, 60, 60)

class Background:
    def __init__(self):
        self.stage = load_image('stage1.png')

    def draw(self):
        global map_width, map_height
        self.stage.draw(map_width // 2, map_height // 2)

def handle_events():
    global running
    global x, y
    global dir
    global look_side
    global is_jump
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            run = 1
            if event.key == SDLK_LEFT:
                dir -= 1
                look_side = -1
            if event.key == SDLK_RIGHT:
                dir += 1
                look_side = 1
            if event.key == SDLK_SPACE:
                is_jump = 1

        if event.type == SDL_KEYUP:
            run = 0
            if event.key == SDLK_LEFT:
                dir += 1
            if event.key == SDLK_RIGHT:
                dir -= 1


main_hero = Hero()
stage1 = Background()

while running:

    handle_events()
    update_canvas()
    main_hero.update()

    clear_canvas()

    stage1.draw()
    main_hero.draw()

