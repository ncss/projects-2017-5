from microbit import *
import radio
import random

radio.on()
radio.config(channel = 5, address=0xffffffff, power=7)

letters = ['A','B']
pattern = ''
length = 3

def display_sequence(sequence):
    for char in sequence:      
        display.show(char)
        sleep(1000)
        display.clear()
        sleep(500)

not_recieved = False
while True:
    msg = radio.receive()
    
    if msg and msg == 'BTN:START':
        
        break
button_a.was_pressed()
button_b.was_pressed()
while True:
    if button_a.was_pressed() and button_b.was_pressed():
        for i in range(length):
            pattern += random.choice(letters)
        print(pattern)
        radio.send('MEM:' + pattern)
        display_sequence(pattern)
        not_recieved = True    
            
 
    while not_recieved:    
        msg = radio.receive()
        if msg:
            radio.on()
            
            if msg == 'REC:CORRECT':
                print(msg)
                length += 1
                pattern = ''
                not_recieved = False
            elif msg == 'REC:INCORRECT':
                incorrect = True
                print(msg)
                while incorrect:
                    if button_a.was_pressed() and button_b.was_pressed():
                        print(pattern)
                        radio.send('MEM:' + pattern)   
                        display_sequence(pattern)
                        incorrect = False
                    
            
            