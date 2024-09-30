from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('zelda.png')

running = True
char_w, char_h = 120, 130
print_w, print_h = 70, 80
pos_x, pos_y = 400, 300
frame = 0
total_frames = 10

ide_frame = 0
ide_total_frames = 3
ide_dir=0

key_state = {
    'UP': False,
    'DOWN': False,
    'LEFT': False,
    'RIGHT': False
}

def handle_events():
    global running, key_state
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_UP:
                key_state['UP'] = True
            elif event.key == SDLK_DOWN:
                key_state['DOWN'] = True
            elif event.key == SDLK_LEFT:
                key_state['LEFT'] = True
            elif event.key == SDLK_RIGHT:
                key_state['RIGHT'] = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                key_state['UP'] = False
            elif event.key == SDLK_DOWN:
                key_state['DOWN'] = False
            elif event.key == SDLK_LEFT:
                key_state['LEFT'] = False
            elif event.key == SDLK_RIGHT:
                key_state['RIGHT'] = False

def move_character():
    global pos_y, pos_x, frame
    frame = (frame + 1) % total_frames

    if key_state['UP']:
        if pos_y < 590:
            pos_y += 5
    if key_state['DOWN']:
        if pos_y > 10:
            pos_y -= 5
    if key_state['LEFT']:
        if pos_x > 10:
            pos_x -= 5
    if key_state['RIGHT']:
        if pos_x < 790:
            pos_x += 5

    if key_state['UP']:
        character.clip_draw(frame * char_w, 130, char_w, char_h, pos_x, pos_y, print_w, print_h)
    elif key_state['DOWN']:
        character.clip_draw(frame * char_w, 390, char_w, char_h, pos_x, pos_y, print_w, print_h)
    elif key_state['LEFT']:
        character.clip_draw(frame * char_w, 260, char_w, char_h, pos_x, pos_y, print_w, print_h)
    elif key_state['RIGHT']:
        character.clip_draw(frame * char_w, 0, char_w, char_h, pos_x, pos_y, print_w, print_h)

def show_ide_animation():
    global ide_frame
    ide_frame = (ide_frame + 1) % ide_total_frames
    character.clip_draw(ide_frame * char_w, 910, char_w, char_h, pos_x, pos_y, print_w, print_h)
    delay(0.1)

while running:
    clear_canvas()
    background.draw(400, 300, 800, 600)
    if not any(key_state.values()):
        show_ide_animation()
    else:
        move_character()
    update_canvas()
    handle_events()
    delay(0.03)

close_canvas()
