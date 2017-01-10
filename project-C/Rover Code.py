from microbit import *
import radio

radio.on()
radio.config(channel = 5)

PREFIX = "ROV:"

def forward(time):
    pin16.write_digital(1)
    pin0.write_digital(0)
    
    pin12.write_digital(1)
    pin8.write_digital(0)
    
    current_time = running_time()
    while (running_time() - current_time) / 1000 < time:
        check_finish_line()
        
    stop()
    
def forward_regard(time):
    pin16.write_digital(1)
    pin0.write_digital(0)
    
    pin12.write_digital(1)
    pin8.write_digital(0)
    
    current_time = running_time()
    while (running_time() - current_time) / 1000 < time:
        v = 1
        
    stop()
    
def reverse(time):
    pin16.write_digital(0)
    pin0.write_digital(1)
    
    pin12.write_digital(0)
    pin8.write_digital(1)
    
    current_time = running_time()
    while (running_time() - current_time) / 1000 < time:
        check_start_line()
        
    stop()
    
def stop():
    pin16.write_digital(0)
    pin0.write_digital(0)
    
    pin12.write_digital(0)
    pin8.write_digital(0)
    
def check_finish_line():
    a = pin1.read_analog()
    if a < 300:
        stop()
        
        
def check_start_line():
    a = pin1.read_analog()
    if a < 300:
        stop()
        forward_regard(0.5)

while True:
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