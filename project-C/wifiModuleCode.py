from machine import UART
import network
import socket

WIFI_UNAME = "Jamal's iphone"
WIFI_PWORD = 'zoewantswifi'
WEBSITE = 'requestb.in'
PAGE = 'xfmsv4xf'

uart = UART(0, 115200)
uart.init(115200, bits=8, parity=None, stop=1)


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect(WIFI_UNAME, WIFI_PWORD)
    while not wlan.isconnected():
        pass

addr = socket.getaddrinfo("""WEBSITE""", 80)[0][-1]
#CHECK website
#ampy -p COM[something] path main.py

s = socket.socket()
s.connect(addr)

while True:
    msg = uart.readline()

    if msg:
        request_string = "POST /%s HTTP/1.0\r\nHost: %s\r\n\r\n" % (PAGE, WEBSITE)
        byte_string = bytes(request_string, 'utf8')
        s.send(byte_string)
        uart.write(b'received')
