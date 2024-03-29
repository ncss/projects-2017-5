from microbit import *
import radio
import random
import math

radio.on()
radio.config(channel = 2)

walls_x = [-1,5]
walls_y = [0,9]

def reset_game():
    global ticks,last_hit,ball,velocity,paddle_1,paddle_2,hits
    ticks=0
    last_hit = 0

    ball = [random.randrange(5),3]
    velocity = [1,1]
     
    paddle_1 = 2 #Paddle 1 is master paddle
    paddle_2 = 2
    hits = 0

reset_game()

def move_ball(): 
    global hits, last_hit
    if ball[0] + velocity[0] in walls_x:
        velocity[0] = -velocity[0]
    if ball[0] == paddle_1:
        if ball[1] + velocity[1] == 0:
            velocity[1] *= -1
            hits += 1
            last_hit = ticks
    
    if ball[0] == abs(4-paddle_2): 
        if ball[1] + velocity[1] == 9:
            velocity[1] *= -1
            hits += 1
            last_hit = ticks
    ball[0] += velocity[0]
    ball[1] += velocity[1]
   
def shift_paddle(paddle, direction):
    if paddle + direction not in walls_x:
      paddle += direction
    return paddle

current_screen = 1      
      
def update_screen():
  display.clear()
  display.set_pixel(paddle_1,0,9)
  if current_screen == 1:
    display_range = [0,1,2,3,4]
    if ball[1] in display_range:
      display.set_pixel(ball[0],ball[1], 9)
  else:
    display_range = [5,6,7,8,9]
    if ball[1] in display_range:
        display.set_pixel(ball[0],ball[1]-5, 9 )
      
 
def end_game(winner):
    sleep(10)
    if winner == '1':
        display.show(Image('90009:09990:00000:09090:09090'))
        radio.send("W:2")
    elif winner == '0':
        display.show(Image('09990:90009:00000:09090:09090'))
        radio.send("W:1")
            
    sleep(1000)
    while 1:
        if button_a.is_pressed() or button_b.is_pressed():
            reset_game()
            break
  
while 1: 
    if (ticks - last_hit) % max(10, 30 - hits) == 0:
        move_ball()
       
    update_screen()
    radio.send("US:" + str(ball[0]) + ":" + str(ball[1]) + ":" + str(paddle_2))#add paddle
    if ball[1] == 0:
        end_game('1')
    if ball[1] == 9:
        end_game('0')    
    if button_a.was_pressed():
        paddle_1 = shift_paddle(paddle_1, -1)
        
    if button_b.was_pressed():
        paddle_1 = shift_paddle(paddle_1, 1) 
    b = radio.receive()
    if b:
        b = b.split(":")
        if b[0] == "MP":
            if b[1] == '1':
                if b[2] == "r":
                    paddle_1 = shift_paddle(paddle_1, -1)
                if b[2] == "l":
                    paddle_1 = shift_paddle(paddle_1, 1)

            elif b[1] == '2':
                if b[2] == "r":
                    paddle_2 = shift_paddle(paddle_2, -1)
                if b[2] == "l":
                    paddle_2 = shift_paddle(paddle_2, 1)
    sleep(10)
    ticks += 1
    
    
    
