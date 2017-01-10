from microbit import *
import radio

radio.on()
radio.config(channel=5)

INPUTSEQUENCE = ''
SENTSEQUENCE = ''

while True:
   msg = radio.receive() 