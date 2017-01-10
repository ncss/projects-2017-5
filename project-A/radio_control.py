from microbit import *
import radio

radio.on()
radio.config(channel=13)

#leg up sends 'left'/'right'
goal = 30
leg = 'right'
count = 0

while count < goal:
    message = radio.receive()
    if message:
        if message == 'left' and leg == 'left':
            count += 1
            leg = 'right'
            radio.send('LIGHT')
        elif message == 'right' and leg == 'right':
            count += 1
            leg = 'left'
            radio.send('LIGHT')
        print(count)
        
            
            
            
            
            
            
            