from microbit import *
import radio

radio.on()
radio.config(address=0xffffffff, channel=5)

while True:
    if button_a.was_pressed():
        radio.send("REC:FORWARD")
        display.show("S")
        sleep(500)
        display.clear()
        sleep(500)