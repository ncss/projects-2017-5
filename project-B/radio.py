from microbit import *

radio.on()
radio.config(channel=2)

def draw_display(paddle,ball):
  display.set_pixel(paddle,4,9)
  display.set_pixel(ball[0],ball[1],9)
  
while 1:
  msg = radio.recieve()
  if msg:
    msg.split(':')
    if msg[0] == 'US':
      