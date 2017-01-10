from microbit import *
import radio

radio.on()
radio.config(channel = 2)

ball = [1,2]
velocity = [1,1]
 
walls_x = [-1,5]
walls_y = [-1,10]

paddle_1 = 2 #Paddle 1 is master paddle
paddle_2 = 2

def move_ball():
    if ball[0] + velocity[0] in walls_x: #Needs to take into account paddle
        velocity[0] = -velocity[0]
    ball[0] += velocity[0]
   
    if ball[1] + velocity[1] in walls_y:
        velocity[1] = -velocity[1]
    ball[1] += velocity[1]

def shift_paddle(paddle, direction):
    if paddle + direction not in walls_x:
      paddle += direction

current_screen = 1      
      
def update_screen():
  #radio.send("US:" + ball[0] + ":" + ball[1])#add paddle
  if current_screen == 1:
    display_range = [0,1,2,3,4]
    if ball[1] in display_range:
      display.set_pixel(ball[0],ball[1], 9)
  else:
    display_range = [5,6,7,8,9]
    if ball[1] in display_range:
        display.set_pixel(ball[0],ball[1]-5, 9 )
      



  
while 1: 
    move_ball()
    radio.send("US:" + str(ball[0]) + ":" + str(ball[1]) + ":" + str(paddle_2))#add paddle
    update_screen()
     
    
    display.set_pixel(paddle_1,0,9)
    
    if button_a.was_pressed:
        shift_paddle(paddle_1, -1)
    if button_b.was_pressed:
        shift_paddle(paddle_1, 1)
    
    b = radio.receive()
    if b:
        b = b.split()
        if b[0] == "MP":
            if b[2] == "r":
                shift_paddle(paddle_2, -1)
            if b[2] == "l":
                shift_paddle(paddle_2, 1)
    sleep(300)
    display.clear()
    
    
    
