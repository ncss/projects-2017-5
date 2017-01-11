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
STATE_FINISHED = 3

state = STATE_START

leg_hold_start = 0
current_delay = 1000

display.show(Image.SAD)

while True:    
    if state == STATE_START:
        if is_leg_up():
            state = STATE_WAIT_FOR_HOLD
            leg_hold_start = running_time()
            display.show(Image.ASLEEP)
            continue
            
    elif state == STATE_WAIT_FOR_HOLD:
        if is_leg_down():
            state = STATE_START
            music.play(music.WAWAWAWAA, wait=False)
            display.show(Image.SAD)
            continue
        elif running_time() - leg_hold_start >= current_delay:
            state = STATE_HOLD_LONG_ENOUGH
            display.show(Image.HAPPY)
            music.play('C7:1')
            
    elif state == STATE_HOLD_LONG_ENOUGH:
        if is_leg_down():
            state = STATE_START
            radio.send('left')
            current_delay += 500
            display.show(Image.SAD)
            sleep(100)