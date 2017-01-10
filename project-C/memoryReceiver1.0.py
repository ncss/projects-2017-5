from microbit import *
import radio

radio.on()
radio.config(channel=5, address=0xffffffff)

receivedsequence = ''
inputsequence = ''

while True:
    msg = radio.receive()
    
    button_a.was_pressed()
    button_b.was_pressed()
    
    if msg:
        if msg.startswith("MEM:"):
            radio.on()
            print(msg)
            receivedsequence = msg[4:]
            display.clear()
                
        while len(inputsequence) < len(receivedsequence):
            if button_a.was_pressed():
                inputsequence += "A"
                display.show("A")
                
            elif button_b.was_pressed():
                inputsequence += "B"
                display.show("B")
                
        if inputsequence == receivedsequence:
            radio.send("REC:CORRECT")
            display.show(Image.YES)
            inputsequence = ''
            receivedsequence = ''
            
        else: #inputsequence != receivedsequence:
            radio.send("REC:INCORRECT")
            display.show(Image.NO)
            inputsequence = ''
            receivedsequence = ''