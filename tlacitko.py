import machine
import time

button = machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_DOWN)
led1 = machine.Pin(2,machine.Pin.OUT)
led2 = machine.Pin(3,machine.Pin.OUT)
led3 = machine.Pin(4,machine.Pin.OUT)
led4 = machine.Pin(5,machine.Pin.OUT)

while True:
    if button.value() == 1:
        led1(True)
        led2(True)
        led3(True)
        led4(True)
    else:
        led1(False)
        led2(False)
        led3(False)
        led4(False)