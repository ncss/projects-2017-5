from microbit import *

import radio

radio.on()

start = False

display.show(Image.TARGET)

while True:
    if pin0.read_digital():
        if start == False:
            start = True
            radio.send("BTN:Start")
            display.show(Image.HEART)
    else:
        if start == True:
            display.show(Image.NO)
    
    msg = radio.receive()
    
    if msg:
        if "Finish" in msg:
            start = False
            display.show(Image.TARGET)