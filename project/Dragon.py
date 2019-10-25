from pico2d import *

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE_DOWN = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN
}

class IdleState:
    @staticmethod
    def enter(Dragon, event):
        if event == RIGHT_DOWN:
            Dragon.velocity += 1
        elif event == LEFT_DOWN:
            Dragon.velocity -= 1
        elif event == RIGHT_UP:
            Dragon.velocity -= 1
        elif event == LEFT_UP:
            Dragon.velocity += 1


    @staticmethod
    def exit(Dragon, event):
        pass

    @staticmethod
    def do(Dragon):
        Dragon.frame_speed += 1
        if Dragon.frame_speed > 30:
            Dragon.frame = (Dragon.frame + 1) % 16
            Dragon.frame_speed = 0

    @staticmethod
    def draw(Dragon):
        if Dragon.dir == 1:
            Dragon.image.clip_draw(Dragon.frame * 16, 160, 16, 16, Dragon.x, Dragon.y, 60, 60)
        else:
            Dragon.image.clip_draw(Dragon.frame * 16, 176, 16, 16, Dragon.x, Dragon.y, 60, 60)


class RunState:
    @staticmethod
    def enter(Dragon, event):
        if event == RIGHT_DOWN:
            Dragon.velocity += 1
        elif event == LEFT_DOWN:
            Dragon.velocity -= 1
        elif event == RIGHT_UP:
            Dragon.velocity -= 1
        elif event == LEFT_UP:
            Dragon.velocity += 1
        Dragon.dir = Dragon.velocity

    @staticmethod
    def exit(Dragon, event):
        pass

    @staticmethod
    def do(Dragon):
        Dragon.frame_speed += 1
        if Dragon.frame_speed > 30:
            Dragon.frame = (Dragon.frame + 1) % 16
            Dragon.frame_speed = 0
        Dragon.x += Dragon.velocity
        Dragon.x = clamp(70, Dragon.x, 960 - 70)

    @staticmethod
    def draw(Dragon):
        if Dragon.velocity == 1:
            Dragon.image.clip_draw(Dragon.frame * 16, 128, 16, 16, Dragon.x, Dragon.y, 60, 60)
        else:
            Dragon.image.clip_draw(Dragon.frame * 16, 144, 16, 16, Dragon.x, Dragon.y, 60, 60)

class JumpState:
    temp_x, temp_y = 0, 0
    t = 0
    p1, p2, p3 = (0, 0), (0, 0), (0, 0)
    @staticmethod
    def enter(Dragon, event):
        if event == SPACE_DOWN:
            Dragon.jump_y = Dragon.y + 200
            if Dragon.velocity > 0:
                Dragon.jump_x = Dragon.x + 200
            elif Dragon.velocity < 0:
                Dragon.jump_x = Dragon.x - 200
            else:
                Dragon.jump_x = Dragon.x
            JumpState.p1, JumpState.p2, JumpState.p3 = (Dragon.x, Dragon.y), ((Dragon.jump_x + Dragon.x) / 2, Dragon.jump_y), (Dragon.jump_x, Dragon.y)
            t = 0
    @staticmethod
    def exit(Dragon, event):
        pass

    @staticmethod
    def do(Dragon):
        Dragon.frame_speed += 1
        if Dragon.frame_speed > 30:
            Dragon.frame = (Dragon.frame + 1) % 16
            Dragon.frame_speed = 0

        while JumpState.t <= 1:
            for i in range(0, 1000 + 1, 2):
                JumpState.t = i / 1000
                JumpState.temp_x = (2 * JumpState.t ** 2 - 3 * JumpState.t + 1) * JumpState.p1[0] + (-4 * JumpState.t ** 2 + 4 * JumpState.t) * JumpState.p2[0] + (2 * JumpState.t ** 2 - JumpState.t) * JumpState.p3[0]
                JumpState.temp_y = (2 * JumpState.t ** 2 - 3 * JumpState.t + 1) * JumpState.p1[1] + (-4 * JumpState.t ** 2 + 4 * JumpState.t) * JumpState.p2[1] + (2 * JumpState.t ** 2 - JumpState.t) * JumpState.p3[1]
                JumpState.temp_x = clamp(70, Dragon.x, 960 - 70)
            Dragon.x = JumpState.temp_x
            Dragon.y = JumpState.temp_y

    @staticmethod
    def draw(Dragon):
        if Dragon.dir == 1:
            Dragon.image.clip_draw(Dragon.frame * 16, 0, 16, 16, JumpState.temp_x, JumpState.temp_y, 60, 60)
        else:
            Dragon.image.clip_draw(Dragon.frame * 16, 16, 16, 16, JumpState.temp_x, JumpState.temp_y, 60, 60)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState,
                LEFT_DOWN: RunState, SPACE_DOWN: JumpState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState,
               RIGHT_DOWN: IdleState, SPACE_DOWN: JumpState},
    JumpState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState,
                LEFT_DOWN: RunState}
}


class Dragon:
    def __init__(self):
        self.x, self.y = 480, 70
        self.jump_x, self.jump_y = 0, 0
        self.image = load_image('sprite\\Character\\character.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.frame_speed = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def update_state(self,  state):
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


