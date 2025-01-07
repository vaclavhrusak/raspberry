import machine
from time import sleep
led1 = machine.Pin(1, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)
led3= machine.Pin(3, machine.Pin.OUT)
tlacitko = machine.Pin(4, machine.Pin.IN)
klik = 0
led1.value(0)
led2.value(0)
led3.value(0)
while True:
    if tlacitko.value() == 1:
        klik= klik + 1
        print(klik)
        sleep(0.5)
    if klik==0:
        led1.value(0)
        led2.value(0)
        led3.value(0)
    if klik==1:
        led1.value(1)
        led2.value(1)
        led3.value(1)
    if klik==2:
        led1.value(0)
        led2.value(0)
        led3.value(0)
        sleep(0.2)
        led1.value(1)
        sleep(0.2)
        led2.value(1)
        sleep(0.2)
        led3.value(1)
        sleep(0.2)
    if klik==3:
        led1.value(1)
        led2.value(0)
        led3.value(0)
        sleep(0.2)
        led1.value(0)
        led2.value(1)
        led3.value(0)
        sleep(0.2)
        led1.value(0)
        led2.value(0)
        led3.value(1)
        sleep(0.2)
        led1.value(0)
        led2.value(1)
        led3.value(0)
        sleep(0.2)
    else:
        led1.value(0)
        led2.value(0)
        led3.value(0)
