# Ejemplo N°16: Lectura sensor DHT11

from machine import Pin
from utime import sleep
from dht import DHT11

dht11_sensor = DHT11(Pin(28, Pin.IN))

while True:
    sleep(2)
    dht11_sensor.measure()
    temp = dht11_sensor.temperature()
    hum = dht11_sensor.humidity()
    
    print('Temperatura: ',temp,'°C')
    print('Humedad Relativa: ',hum,'%')
    print() # Renglón en blanco 