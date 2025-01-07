import machine
import time
button = machine.Pin(8,machine.Pin.IN,machine.Pin.PULL_DOWN)
ledky = []
for i in range(7):
    ledky.append(machine.Pin(i).OUT)
    def blikacky():
