from microbit import *
import radio

radio.on()
radio.config(channel=13)

#leg up sends 'left'/'right'
goal = 30
leg = 'right'
count = 0

while True:
    message = radio.receive()
    if message:
        if message == 'left' and leg == 'left':
            
            
            
            
            
            
            
            