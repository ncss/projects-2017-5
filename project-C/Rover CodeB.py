from microbit import *
import radio

radio.on()
radio.config(channel = 5, address=0xfffffff1, power=7)

REC = "REC:"
MEM = "MEM:"
ROV = "ROV:"

speed = 1

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
    pin12.write_digital(0)
    pin8.write_digital(0)
    
    pin16.write_digital(0)
    pin0.write_digital(0)
    
def check_finish_line():
    a = pin1.read_analog()
    if a < 300:
        stop()
        radio.config(channel = 5, address=0xffffffff, power=7)
        radio.send("ROV:FINISH")
        
def check_start_line():
    a = pin1.read_analog()
    if a < 300:
        stop()
        forward_regard(0.5)

while True:
    msg = radio.receive()
    if msg:
        if msg.startswith(REC):
            msg = msg[len(REC):]
            if msg.startswith("CORRECT"):
                forward(speed)
                
            if msg.startswith("INCORRECT"):
                reverse(speed)