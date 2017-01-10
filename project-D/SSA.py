from microbit import *
import radio
display.off()
radio.on()
radio.config(channel=6)

initial_flex = pin1.read_analog()
flex_scale = 1

pins = {"right": [pin1,pin1.read_analog(),1],
        "left": [pin2,pin2.read_analog(),1],
        "for" : [pin3,pin3.read_analog(),1],
        "back" : [pin4,pin4.read_analog(),1]}


def check(inf):
    p = inf[0]
    initial_flex = inf[1]
    flex_scale = inf[2]
    flex = abs((p.read_analog() - initial_flex) / flex_scale)
    if flex > 30:
        print('PRESSED')
        return True
        
    else:
        print('NOT PRESSED')
        return False
    
    sleep(20)
    
    
while True:
    for i in ["right","left","for","back"]:
        if check(pins[i]):
            radio.send(i)