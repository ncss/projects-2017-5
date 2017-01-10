from microbit import *
import radio
import random

pattern = ['A', 'B']

radio.on()
radio.config(channel = 5)

length = 3
correct = True
while True:
    if button_a.was_pressed and button_b.was_pressed():
        sequence = ''
        for i in range(length):
            sequence += random.choice(pattern)
        print(sequence)
        radio.send("MEM:" + sequence)
        for char in sequence:
            display.show(char)
            sleep(1000)
            display.clear()
            sleep(500)
        not_received = True
        while not_received:
            msg = radio.receive()
            if msg and 'MEM:CORRECT' in msg:
                print(msg)
                length += 1
                not_received = False
            elif msg != 'MEM:CORRECT':
                if button_a.was_pressed and button_b.was_pressed():
                    radio.send("MEM:" + sequence)
                    for char in sequence:
                        display.show(char)
                        sleep(1000)
                        display.clear()
                        sleep(500)
                
