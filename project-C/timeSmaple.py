
#Sender

from microbit import *

import radio

radio.config(channel = 5)

time = 3 #Change this based off the length of the running space and such

#Sends after sequence has played

def send_time(time):
    radio.send("TIME:" + time)

m = radio.receive()
if m:
    if "TIME:Restart" in m:
        #Resend message
        send_time(5000) #Change this value(Also make value in miliseconds)
        
#------------------------------------------------------

#Reciever

import speech

radio.config(channel = 5)

m = radio.recieve()

if m:
    if "TIME:" in m:
        receive_time(m)

time = 0

def recieve_time(message):
    OriginTime = running_time()
    time = m[5:]
while True:
    if OriginTime - running_time() >= time:
        radio.send("TIME:Restart")
        speech.say("You Suck",speed=40)
        #Then restart the process
    
    