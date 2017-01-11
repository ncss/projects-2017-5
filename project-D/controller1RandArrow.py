from microbit import *
import radio
import random

radio.on()
radio.config(channel=9)

def arrowChoice():
    directions = {"right": Image.ARROW_E,
                  "for": Image.ARROW_N,
                  "back":Image.ARROW_S,
                  "left":Image.ARROW_W}
    direction  = ["right","left","for","back"]
    cur = random.choice(direction)
    display.show(directions[cur])
    
while True:
    