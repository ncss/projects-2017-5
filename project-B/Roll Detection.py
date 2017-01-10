from microbit import *
from radio import *
on()
config(channel = 2)
a=accelerometer
def a_left():
    return a.is_gesture("left")
def a_right():
    return a.is_gesture("right")
def a_still():
    return a.is_gesture("face up")
last_state = 's'
display.show(Image.ARROW_N)
while 1:
    #print(last_state)
    if a_left():
        if last_state == 's':
            send("left")
            print("left")
        last_state = 'l'
    if a_right():
        if last_state == 's':
            send("right")
            print("right")
        last_state = 'r'
    if a_still():
        last_state = 's'