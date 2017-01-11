from microbit import *
import radio
import random
time = 2000
score = 0
multiplier = 0
combo = 0
#https://www.youtube.com/watch?v=fBGSJ3sbivI
radio.on()
radio.config(channel=9, address=0x87654321)
lose = 0

def round(time, combo, multiplier,cur):
    directions = {"right": Image.ARROW_E,
                  "for": Image.ARROW_N,
                  "back":Image.ARROW_S,
                  "left":Image.ARROW_W}
    direction  = ["right","left","for","back"]
    game_won = False
    sleep(2)
    display.show(directions[cur])
    start =  running_time()
    end = running_time()
    
    
    while end-start < time:
        get = radio.receive()
        if type(get) is str:
            if get == cur:
                game_won = True
                combo += 1
                break
            else:
                game_won = False
                combo = 0
                break
        end = running_time()
    
    #if time > 400:
    time = max(int(time* 0.95),650)
    if combo >= 3:
        multiplier += 1
        combo = 0
    if game_won:
        round_won = True
    else:
        multiplier = 1
        combo = 0
        round_won = False
    return time,combo,multiplier,round_won
    


while True:
    radio.config(channel=9, address=0x87654321)
    cur = radio.receive()
    sleep(1)
    score_start,score_end = running_time(),running_time()
    while type(cur) is not str:
        cur = radio.receive()
        sleep(1)
        score_end = running_time()
        if score_end - score_start > 4000:
            score = 0
            time = 2000
    radio.config(channel = 9 , address = 0x75626974)
    time,combo,multiplier,round_won = round(time,combo,multiplier,cur)
    if round_won:
        radio.config(channel=9, address=0x87654321)
        display.show(Image.HAPPY)
        score += multiplier
    else:
        radio.config(channel=9, address=0x87654321)
        display.show(Image.SAD)      
        lose += 1
    radio.config(channel=6,address=0x12341234)
    radio.send(str("%03d" % score))

        
    