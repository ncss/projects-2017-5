from microbit import *
import radio

radio.on()
radio.config(channel=5)

while True:
   msg = radio.receive()   
   if msg: 
       if msg.startswith("MEM:"):
           print(msg)      
           INPUTSEQUENCE = ''
           SENTSEQUENCE = msg[4:]
   
       while len(INPUTSEQUENCE) < len(SENTSEQUENCE):
           if button_a.was_pressed():
               INPUTSEQUENCE += 'A'
               display.show("A")
               sleep(100)
           elif button_b.was_pressed():
               INPUTSEQUENCE += 'B'
               display.show("B")
               sleep(100)
               
       print(SENTSEQUENCE)
       print(INPUTSEQUENCE)
       
       if INPUTSEQUENCE == SENTSEQUENCE:
           radio.send('REC:CORRECT')
           #radio.send(ROVER:FORWARD)
           #radio.send(ROVER:REVERSE)
           display.show(Image.HEART)
           sleep(500)
           display.clear()
       else:
           radio.send('REC:INCORRECT')
           display.show('X')
           sleep(2000)
           display.clear()