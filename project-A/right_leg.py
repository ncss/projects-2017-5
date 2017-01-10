from microbit import *
import radio
import music

radio.on()
radio.config(channel=13)

pos = "down"



while True:
    x, y, z = accelerometer.get_values()
    sleep(50)
    
    if pos == "up":
        if -300 < z  < -50:
            pos = "down"
            display.show(Image.SAD)
            
    elif pos == "down":
        if z < -850:
            pos = "up"
            #display.show(Image.ASLEEP)
            
                    
            music.play('C7:1')
            radio.send("right")
            display.show(Image.HAPPY)
    
