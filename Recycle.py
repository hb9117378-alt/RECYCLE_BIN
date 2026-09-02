import pgzrun
import random
WIDTH = 800
HEIGHT = 600

CENTER = (WIDTH//2, HEIGHT//2)
FINAL_LEVEL = 10
START_SPEED = 10
ITEMS =  ["battery", "bottle", "chips", "plasticBag"]

Game_over = False
Game_complete = False
current_level = 1
item = []
animations = []

def draw():
    global item, current_level, Game_over, Game_complete
    screen.clear()
    if Game_over:
        screen.draw.text("Game Over", fontsize= 60, center=CENTER, color="Red")
        screen.draw.text("Try Again", fontsize= 30, center=(400,500), color="Black")
    elif Game_complete:
        screen.draw.text("YOU WIN", fontsize= 70, center=CENTER, color="Blue")
        screen.draw.text("Play again", fontsize= 35, center=(400,500), color="Black")
    else:
        for i in item:
            i.draw()

def update():
    global item
    if len(item)==0:
        item=make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items 

def get_option_to_create(number_of_extra_items):
    items_to_create = ["bag"]
    for i in range(0,number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create 

def create_items(items_to_create):
   new_items = []
   for i in items_to_create:
       item = Actor(i+"Img")
       new_items.append(item)
   return new_items

def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout)+1
    gap_size = WIDTH/number_of_gaps

    for i,item in enumerate(items_to_layout):
        new_x_pos = (i+1)*gap_size
        i.x = new_x_pos

def animate_items(items_to_animate):
    global animations
    for i in items_to_animate:
        dur=START_SPEED-current_level
        i.anchor=("center","bottom")
        animation=animate(i,duration = dur, on_finished = handle_game_over, y= HEIGHT)
        animations.append(animation)

def handle_game_over():
    global Game_over
    Game_over = True 

def handle_game_complete():
    global current_level,items,animations,Game_complete
    stop_animation(animations)
    if current_level==FINAL_LEVEL:
        Game_complete=True
    else:
        current_level+=1
        items=[]
        animations=[]


def on_mouse_down(pos):
    global item,current_level
    for i in item:
        if i.collidepoint(pos):
            if "bag" in i.image:
                handle_game_complete()
            else:
                handle_game_over()
            

def stop_animation(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

pgzrun.go()



