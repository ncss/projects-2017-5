from microbit import *
from radio import *
on()
config(channel = 2)
NUM = '2'
EXTREME = 1000
STILL = 400
a = accelerometer
state = 's'
display.show(NUM)
zero = a.get_x()
while 1:
    x_tilt = a.get_x() - zero
    if button_a.is_pressed() and button_b.is_pressed():
        zero = a.get_x()
    if abs(x_tilt) <= STILL:
        state = 's'
    if x_tilt >= EXTREME:
        if state == 's':
            send("MP:"+NUM+":l")
        state = 'l'
    if x_tilt <= -EXTREME:
        if state == 's':
            send("MP:"+NUM+":r")
        state = 'r'