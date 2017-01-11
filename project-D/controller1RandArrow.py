from microbit import *
import radio
import random
time = 2000
radio.on()
radio.config(channel=9, address=0x12345678)
directions = {"right": Image.ARROW_E,
                  "for": Image.ARROW_N,
                  "back":Image.ARROW_S,
                  "left":Image.ARROW_W}    
direction  = ["right","left","for","back"]
sent = False
while True:
    if button_a.was_pressed():
        start,end = running_time(),running_time()
        while end - start < 90000:
            radio.config(channel=9, address=0x12345678)
            if sent == False:
                cur = random.choice(direction) 
                display.show(directions[cur])
                sleep(time)
                display.clear()
                radio.send(cur)
                sent = True
            else:
                sleep(time)
                sent = False
            if button_b.was_pressed():
               end = start + 200000
            time = max(int(time* 0.95),650)   
            end = max(running_time(),end)
    time = 2000
