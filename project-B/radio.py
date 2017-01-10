from microbit import *
import radio
radio.on()
radio.config(channel=2)
ball = [0,0]
def draw_display(ball,paddle):
    display.clear()
    display.set_pixel(paddle,0,9)
    if ball[1] > 4:
        display.set_pixel(4-ball[0],4-((ball[1])-5),9)
  
while 1:
  msg = radio.receive()
  if msg:
    print(msg)
    msg = msg.split(':')
    if msg[0] == 'US':
        ball[0] = int(msg[1])
        ball[1] = int(msg[2])
        paddle = int(msg[3])
        draw_display(ball,paddle)
    else:
        display.clear()
    if button_a.was_pressed():
        radio.send('MP:2:l')
    elif button_b.was_pressed():
        radio.send('MP:2:r')
      