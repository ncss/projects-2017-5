from microbit import *

import radio

radio.config(channel = 5, address=0xffffffff)

radio.on()

start = False

display.show(Image.TARGET)

while True:
    if pin0.read_digital():
        if start == False:
            start = True
            radio.send("BTN:START")
            display.show(Image.HEART)
    else:
        if start == True:
            display.show(Image.NO)
    
    msg = radio.receive()
    
    if msg:
        if "FINISH" in msg:
            start = False
            display.show(Image.TARGET)