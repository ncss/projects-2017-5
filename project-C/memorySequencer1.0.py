from microbit import *
import radio
import random

radio.on()
radio.config(channel = 5, address=0xffffffff)

letters = ['A','B']
pattern = ''
length = 3

def display_sequence(sequence):
    for char in sequence:      
        display.show(char)
        sleep(1000)
        display.clear()
        sleep(500)

while True:
    if button_a.was_pressed() and button_b.was_pressed():
        for i in range(length):
            pattern += random.choice(letters)
        print(pattern)
        radio.send('MEM:' + pattern)
        display_sequence(pattern)
        correct = False
            
            
 
 
    msg = radio.receive()
    if msg:
        radio.on()
        
        if msg == 'REC:CORRECT':
            print(msg)
            length += 1
            pattern = ''
        elif msg == 'REC:INCORRECT':
            incorrect = True
            print(msg)
            while incorrect:
                if button_a.was_pressed() and button_b.was_pressed():
                    print(pattern)
                    radio.send('MEM:' + pattern)   
                    display_sequence(pattern)
                    incorrect = False
                    
            
            