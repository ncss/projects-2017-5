from microbit import *
from radio import *
on()
config(channel = 2)
NUM = '2'
EXTREME = 700
STILL = 400
a = accelerometer
state = 's'
display.show(Image())
while 1:
    if abs(a.get_x()) <= STILL:
        state = 's'
    if a.get_x() >= EXTREME:
        if state == 's':
            send("MP:"+NUM+":l")
        state = 'l'
    if a.get_x() <= -EXTREME:
        if state == 's':
            send("MP:"+NUM+":r")
        state = 'r'