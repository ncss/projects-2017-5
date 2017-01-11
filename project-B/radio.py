from microbit import *
import radio
radio.on()
radio.config(channel=2)
ball = [0,0]
def draw_display(ball,paddle):
    display.clear()
    display.set_pixel(paddle,0,9)
    if ball[1] > 4 and ball[1] < 10:
        display.set_pixel(4-ball[0],4-((ball[1])-5),9)
    if ball[1] == 9:
        display.show(Image('90009:09990:00000:09090:09090'),wait=False)
    elif ball[1] == 0:
        display.show(Image('09990:90009:00000:09090:09090'),wait=False)
  
while 1:
    try:
        msg = radio.receive()
    except ValueError:
        continue
    if msg:
        msg = msg.split(':')
        if msg[0] == 'US':
            ball[0] = int(msg[1])
            ball[1] = int(msg[2])
            paddle = int(msg[3])
            draw_display(ball,paddle)
        if button_a.was_pressed():
            radio.send('MP:2:r')
        elif button_b.was_pressed():
            radio.send('MP:2:l')
      