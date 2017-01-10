from microbit import *
import radio
import music

radio.on()
radio.config(channel=13)

pos = "down"

while True:
    x, y, z = accelerometer.get_values()
    #print(z)
    sleep(50) 
    if pos == "up":
        if -300 < z  < -50:
            pos = "down"
            print("knee down")
            display.show(Image.SAD)
    elif pos == "down":
        if -1000 < z < -850:
            pos = "up"
            print("knee up")
            display.show(Image.HAPPY)
            music.play('E7:1')
            radio.send("left")
