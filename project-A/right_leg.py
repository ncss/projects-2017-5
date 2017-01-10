from microbit import *
import radio
import music

radio.on()
radio.config(channel=13)

pos = "down"

def is_leg_up():
    z = accelerometer.get_z()
    return z < -850

def is_leg_down():
    z = accelerometer.get_z()
    return -300 < z  < -50    

STATE_START = 0
STATE_WAIT_FOR_HOLD = 1
STATE_HOLD_LONG_ENOUGH = 2
STATE_SUCCESSFUL_LEG_RAISE = 3
STATE_FINISHED = 4

state = STATE_START

while True:    
    if state == STATE_START:
        if is_leg_up():
            state = STATE_WAIT_FOR_HOLD
            continue
    elif state == STATE_WAIT_FOR_HOLD:
        
        if is_leg_down():
            state = STATE_START
            continue
        elif 
    elif state == STATE_HOLD_LONG_ENOUGH:
        continue
    elif state == STATE_SUCCESSFUL_LEG_RAISE:
        continue
    elif state == STATE_FINISHED:
        continue
    
    x, y, z = accelerometer.get_values()
    sleep(50)
    
    if pos == "up":
        if -300 < z  < -50:
            pos = "down"
            display.show(Image.SAD)
            
    elif pos == "down":
        if z < -850:
            pos = "up"
            #display.show(Image.ASLEEP)
            
                    
            music.play('C7:1')
            radio.send("right")
            display.show(Image.HAPPY)
    
