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
start_time,end_time = running_time(),running_time()
while True:
    if sent == False:
        arrow = radio.receive()
        if arrow in direction:
            display.show(directions[arrow])
            sleep(time)
            display.clear()
            radio.config(channel=9, address=0x87654321)
            radio.send(arrow)
            radio.config(channel=9, address=0x12345678)
          #  sent = True
            time = max(int(time* 0.95),650)
            start_time,end_time = running_time(),running_time()
        else:
           end_time = running_time()
           if end_time - start_time > 4000:
               time = 2000
        

