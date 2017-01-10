from microbit import *
import radio
import random
time = 1200
score = 0
multiplier = 0
combo = 0
#https://www.youtube.com/watch?v=fBGSJ3sbivI
radio.on()
radio.config(channel=9)

# d

def round(time, combo, multiplier,score):
    directions = {"right": Image.ARROW_E,
               "for": Image.ARROW_N,
               "back":Image.ARROW_S,
               "left":Image.ARROW_W}
    direction  = ["right","left","for","back"]
    game_won = False
    cur = random.choice(direction)
    display.show(directions[cur])
    start =  running_time()
    end = running_time()
    
    while end-start < time:
        get = radio.receive()
        if get == cur:
            game_won = True
            combo += 1
            break
        end = running_time()
    
    if time > 400:
        time = int(time* 0.9)
    if combo >= 3:
        multiplier += 1
        combo = 0
    if game_won:
        score += multiplier 
    else:
        multiplier = 1
        combo = 0
    return time,combo,multiplier,score


while True:
    if button_a.was_pressed():
        s_start,s_end = running_time(),running_time()
        while s_end - s_start < 170000:
            time,combo,multiplier,score = round(time,combo,multiplier,score)
            display.clear()
            print(score)
        display.scroll(score,wait=False)
        display.show(Image.HEART)
        wait(2000)
        display.show(Image.MUSIC_CROTCHET)
    display.show(Image.MUSIC_QUAVER)
            
    