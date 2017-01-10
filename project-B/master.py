from microbit import *
import radio

radio.on()
radio.config(channel = 2)

ball = [1,2]
velocity = [1,1]
 
walls_x = [-1,5]
walls_y = [-1,11]

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
      display.set_pixel(ball[0],ball[1])
  else:
    display_range = [5,6,7,8,9]
    if ball[1] in display_range:
        display.set_pixel(ball[0],ball[1]-5)
      



  
while 1:
    display.clear()  
    sleep(300)
    
    
    
    draw_display(paddle1,paddle2,ball)