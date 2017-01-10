from microbit import *
import radio
import random

pattern = ['A', 'B']

radio.on()
radio.config(channel = 5)

length = 3
correct = True
sequence = ''
while True:
    if button_a.was_pressed() and button_b.was_pressed():   
        for i in range(length):
            sequence += random.choice(pattern)
            
        print(sequence)
        
        
        for char in sequence:
            display.show(char)
            sleep(1000)
            display.clear()
            sleep(500)
            
        not_received = True
        radio.send("MEM:" + sequence)
        while not_received:
            msg = radio.receive()     
            if msg:
                if msg == 'REC:INCORRECT':
                    print(msg)
                    while True:
                        if button_a.was_pressed() and button_b.was_pressed():
                            print("2nd AB")
                            
                        
                            for char in sequence:
                                display.show(char)
                                sleep(1000)
                                display.clear()
                                sleep(500)
                            radio.send("MEM:" + sequence)
                            break
                elif msg == 'REC:CORRECT':
                    print(msg)
                    sequence = ''
                    length += 1
                    not_received = False
                

            