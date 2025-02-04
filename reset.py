import time
import network
import socket
from machine import Pin
 
# Set up LED and button
led = Pin(0, Pin.OUT)
led1 = Pin(1, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(3, Pin.OUT)
button = Pin(4, Pin.IN)

def wait():
    while(True):
        led.value(1)
        time.sleep(0.3)
        led.value(0)

 
# Wi-Fi credentials
ssid = 'Samsung S21 Ultra'
password = 'Vojta123'
 
# Initialize Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
 
# Wait for connection
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('Waiting for connection...')
    wait()
    time.sleep(1)
 
if wlan.status() != 3:
    print('Network connection failed')
    if button.value()==1:
        print('starting again')
        max_wait=10
    
else:
    print('Connected')
    status = wlan.ifconfig()
    led.value(0)
    
    print('IP = ' + status[0])

 
# HTML content with buttons
html = """<!DOCTYPE html>
<html>
<head>
    <title>Pico W LED Control</title>
</head>
<body>
    <h1>Pico W LED Control</h1>
    <p>LED is currently: <strong>%s</strong></p>
    <form action="/" method="GET">
        <button name="led" value="on" type="submit">Turn LED ON</button>
        <button name="led" value="off" type="submit">Turn LED OFF</button>
    </form>
</body>
</html>
"""
 
# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('Listening on', addr)
 
# Listen for connections and serve HTML
while True:
    try:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024).decode('utf-8')
        print("Request:", request)
 
        # Check for LED control commands
        led_on = request.find('led=on') != -1
        led_off = request.find('led=off') != -1
 
        if led_on:
            print("Turning LED ON")
            led.value(1)
        if led_off:
            print("Turning LED OFF")
            led.value(0)
 
        # Get the current LED state
        led_state = "ON" if led.value() == 1 else "OFF"
 
        # Send response
        response = html % led_state
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
 
    except OSError as e:
        cl.close()
        print('Connection closed')
