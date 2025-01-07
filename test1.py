import machine
import time
klik=0
button = machine.Pin(4,machine.Pin.IN,machine.Pin.PULL_DOWN)
led1 = machine.Pin(1,machine.Pin.OUT)
led2 = machine.Pin(2,machine.Pin.OUT)
led3 = machine.Pin(3,machine.Pin.OUT)

while(True):
    if button.value() ==1:
        klik=klik+1
        time.sleep(0.2)
    if klik== 1:
        led1(True)
        led2(True)
        led3(True)
        time.sleep(0.2)
        led1(False)
        led2(False)
        led3(False)
        
    elif klik== 2:
        led1(True)
        time.sleep(0.5)
        led2(True)
        time.sleep(1)
        led3(True)
        time.sleep(1.5)
        led1(False)
        led2(False)
        led3(False)
        