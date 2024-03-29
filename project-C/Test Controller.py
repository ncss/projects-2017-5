from microbit import *
import radio

PREFIX = "ROV:"

radio.on()
radio.config(channel=5, address = 0xffffffff)

while True:
    if button_a.was_pressed():
        radio.send(PREFIX + "CORRECT")
        display.show(Image.ARROW_N)
        sleep(500)
        
    if button_b.was_pressed():
        radio.send(PREFIX + "INCORRECT")
        display.show(Image.ARROW_S)
        sleep(500)
    
    display.clear()