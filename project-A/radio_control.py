from microbit import *
import radio
import music

radio.on()
radio.config(channel=13)

goal = 30

while True:
    leg = 'right'
    count = 0
    display.clear()
    while count < goal:
        display.scroll(str(count))
        message = radio.receive()
        if message:
            print('received {}'.format(message))
            if message == 'left' and leg == 'left':
                count += 1
                leg = 'right'
                radio.send('LIGHT')
            elif message == 'right' and leg == 'right':
                count += 1
                leg = 'left'
                radio.send('LIGHT')
    radio.send('finished')
    music.play(music.NYAN, wait=False)
    display.scroll("Win!!")
    
            
            
            
            
            
            
