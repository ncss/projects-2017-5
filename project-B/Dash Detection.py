from microbit import *
from radio import *
on()
config(channel = 2)
a=accelerometer
THRESHOLD = 1500
MAX_DELAY = 10000
MIN_DELAY = 1000
def a_left():
    return a.get_x() > THRESHOLD
def a_right():
    return a.get_x() < -THRESHOLD
def a_still():
    return abs(a.get_x()) <= THRESHOLD
last_state = 's'
last_left = -2 * MAX_DELAY
last_right = -2 * MAX_DELAY
display.show(Image.ARROW_N)
while 1:
    #print(last_state)
    if a_left():
        if last_state == 's':
            #send("to left"+str(running_time() - last_right))
            if running_time() - last_right < MAX_DELAY and running_time() - last_left > MIN_DELAY:
                send("left")
        last_state = 'l'
    if a_right():
        if last_state == 's':
            #send("to right"+str(running_time() - last_right))
            if running_time() - last_left < MAX_DELAY and running_time() - last_right > MIN_DELAY:
                send("right")
        last_state = 'r'
    if a_still():
        if last_state == 'l':
            last_left = running_time()
        elif last_state == 'r':
            last_right = running_time()
        last_state = 's'