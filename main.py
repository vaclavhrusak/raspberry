import dht
import machine
import time

# Inicializace pinu, na který je připojeno DHT čidlo (v tomto případě GP0)
dht_pin = machine.Pin(1)  # GPIO0 (vstupní pin pro DHT čidlo)
sensor = dht.DHT11(dht_pin)  # Používáme DHT11 čidlo
Led1 = machine.Pin(2, machine.Pin.OUT )
Led2 = machine.Pin(3, machine.Pin.OUT)
Led3 = machine.Pin(4, machine.Pin.OUT)
Led4 = machine.Pin(5, machine.Pin.OUT)
while True:
    try:
        # Čtení teploty a vlhkosti
        sensor.measure()  # Vykonání měření
        temperature = sensor.temperature()  # Teplota v °C

        # Výpis na konzoli
        print('Teplota: {}°C'.format(temperature))
        if temperature <22:
            Led1(True)
            Led2(False)
            Led3(False)
            Led4(False)
        elif temperature <23:
            Led1(True)
            Led2(True)
            Led3(False)
            Led4(False)
        elif temperature <27:
            Led1(True)
            Led2(True)
            Led3(True)
            Led4(False)
        elif temperature <30:
            Led1(True)
            Led2(True)
            Led3(True)
            Led4(True)
    
    except OSError as e:
        print('Chyba při čtení z DHT čidla:', e)

    time.sleep(0.2)  # Počkej 2 sekundy před dalším měřením

    
