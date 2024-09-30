from pico2d import *


open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('zelda.png')


def handle_events():
    global running, dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.key == SDLK_ESCAPE:
            running = False




running = True
x = 800 // 2
frame = 0

# fill here
while running:
    clear_canvas()
    background.draw(400,300,800,600)
    update_canvas()
    handle_events()

close_canvas()

