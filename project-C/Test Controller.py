from microbit import *
import radio

PREFIX = "ROV:"

radio.on()
radio.config(channel=5)

while True:
    if button_a.was_pressed():
        radio.send(PREFIX + "FORWARD:2")
        display.show(Image.ARROW_N)
        sleep(500)
        
    if button_b.was_pressed():
        radio.send(PREFIX + "REVERSE:2")
        display.show(Image.ARROW_N)
        sleep(500)
    
    display.clear()