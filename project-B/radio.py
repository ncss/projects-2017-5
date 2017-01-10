from microbit import *
import radio
radio.on()
radio.config(channel=2)
ball = [0,0]
def draw_display(ball,paddle):
    display.clear()
    #display.set_pixel(paddle,4,9)
    display.set_pixel(ball[0],ball[1],9)
  
while 1:
  msg = radio.receive()
  if msg:
    print(msg)
    msg = msg.split(':')
    if msg[0] == 'US':
        ball[0] = int(msg[1])
        ball[1] = int(msg[2])
    if ball[1] > 4:
        draw_display([ball[0],-1*(5-ball[1])],1)
    else:
        display.clear()
    print(ball)
      