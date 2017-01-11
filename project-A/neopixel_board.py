from microbit import *
import neopixel
import radio

radio.on()
radio.config(channel=13)

np = neopixel.NeoPixel(pin0, 30)

pixels = [(min(255,i*12),max(0,255-i*12),0) for i in range(30)]
blank = [(0, 0, 0) for i in range(30)]

print(blank)

while True:
    for i in range(30):
        while True:
            message = radio.receive()
            if message:
                if message == 'LIGHT':
                    print('got message')
                    #if message == 'LIGHT':
                    np[i] = pixels[i]
                    np.show()
                    break
    for i in range(30):
        np[i] = blank[i]
