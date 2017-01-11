from microbit import *
import sys

uart.init(9600, tx=pin1,rx=pin2)

while True:
    if button_a.was_pressed():
        uart.write(b'pressed')
        display.scroll('pressed', wait=False)
        
    if uart.any():
        display.show(Image.HEART)