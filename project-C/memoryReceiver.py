from microbit import *
import radio

radio.on()
radio.config(channel=5)

INPUTSEQUENCE = ''
SENTSEQUENCE = ''

while True:
   msg = radio.receive() 
   
   if msg: 
       print('1', msg)
       if msg.startswith("MEM:"):
           print('2', msg)
           
           INPUTSEQUENCE = ''
           SENTSEQUENCE = msg[4:]
   
       while len(INPUTSEQUENCE) < len(SENTSEQUENCE):
           if button_a.was_pressed():
               INPUTSEQUENCE += 'A'
               display.show("A")
           elif button_b.was_pressed():
               INPUTSEQUENCE += 'B'
               display.show("B")
       
       if INPUTSEQUENCE == SENTSEQUENCE:
           radio.send('MEM:CORRECT')
           #radio.send(ROVER:FORWARD)
           #radio.send(ROVER:REVERSE)
           display.show(Image.HEART)
           sleep(500)
           display.clear()
       else:
           display.show('X')
           sleep(2000)
           display.clear()