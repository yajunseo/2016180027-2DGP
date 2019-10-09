from pico2d import *








def handle_events():


    global running


    global x


    global dir


    global see


    events = get_events()


    for event in events:


        if event.type == SDL_QUIT:


            running = False


        elif event.type == SDL_KEYDOWN:


            if event.key == SDLK_RIGHT:


                dir += 1


                see = 1


            elif event.key == SDLK_LEFT:


                dir -= 1


                see = -1


            elif event.key == SDLK_ESCAPE:


                running = False


        elif event.type == SDL_KEYUP:


            if event.key == SDLK_RIGHT:


                dir = 0


            elif event.key == SDLK_LEFT:


                dir = 0











    pass








open_canvas()


grass = load_image('grass.png')


character = load_image('animation_sheet.png')





running = True


x = 800 // 2


frame = 0


dir = 0


see = 1





while running:


    clear_canvas()


    grass.draw(400, 30)


    if(x>=25 and x<=775):


        if dir > 0:


            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)


        elif dir < 0:


            character.clip_draw(frame * 100, 0 * 1, 100, 100, x, 90)


        elif dir == 0:


            if see == -1:


             character.clip_draw(frame * 100, 200 * 1, 100, 100, x, 90)


            elif see == 1:


              character.clip_draw(frame * 100, 300 * 1, 100, 100, x, 90)








    else:


        if see == -1:


            dir = 0


            character.clip_draw(frame * 100, 200 * 1, 100, 100, x, 90)


        else:


            dir = 0


            character.clip_draw(frame * 100, 300 * 1, 100, 100, x, 90)





    update_canvas()





    handle_events()


    frame = (frame + 1) % 8


    x += dir








close_canvas()

