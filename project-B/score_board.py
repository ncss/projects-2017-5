from microbit import *
import radio
score_1 = 0
score_2 = 0

radio.on()
radio.config(channel=2)


def display_score_1():
    for i in range(score_1):
        display.set_pixel(0, 4-i, 9)


def display_score_2():
    for i in range(score_2):
        display.set_pixel(4, 4-i, 9)


display_score_1()
display_score_2()


def win():
    global score_1, score_2
    if score_1 == 5:
        display.show("1")
        sleep(2000)
        while True:
            if button_a.was_pressed() or button_b.was_pressed():
                score_1 = 0
                score_2 = 0
                break
    elif score_2 == 5:
        display.show("2")
        sleep(2000)
        while True:
            if button_a.was_pressed() or button_b.was_pressed():
                score_1 = 0
                score_2 = 0
                break


while True:
    try:
        b = radio.receive()
    catch ValueError:
        continue
    if b:
        b = b.split(":")
        if b[0] == "W" and b[1] == "1":
            score_1 += 1
            display_score_1()
            sleep(500)
            radio.on()
            radio.config(channel=2)

        elif b[0] == "W" and b[1] == "2":
            score_2 += 1
            display_score_2()

            sleep(500)
            radio.on()
            radio.config(channel=2)
    win()
