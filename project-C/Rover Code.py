from microbit import *
import radio

radio.on()
radio.config(channel = 5)

PREFIX = "ROVER:"

def forward(time):
    pin16.write_digital(1)
    pin0.write_digital(0)
    
    pin12.write_digital(1)
    pin8.write_digital(0)
    
    sleep(1000 * time)
    
    stop()
    
def reverse(time):
    pin16.write_digital(0)
    pin0.write_digital(1)
    
    pin12.write_digital(0)
    pin8.write_digital(1)
    
    sleep(1000 * time)
    
    stop()
    
def stop():
    pin16.write_digital(0)
    pin0.write_digital(0)
    
    pin12.write_digital(0)
    pin8.write_digital(0)


while True:
    if pin1.read_analog() < 300:
        print("ONLINE")
    elif pin1.read_analog() > 400:
        print("OFFLINE")
    
    msg = radio.receive()
    if msg:
        if msg.startswith(PREFIX):
            msg = msg[len(PREFIX):]
            if msg.startswith("FORWARD:"):
                msg = msg[len("FORWARD:"):]
                forward(int(msg))
                
            if msg.startswith("REVERSE:"):
                msg = msg[len("REVERSE:"):]
                reverse(int(msg))