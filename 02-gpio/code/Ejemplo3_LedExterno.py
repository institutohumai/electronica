# Ejemplo N°3: Parpadeo de un LED externo (GP15)

from machine import Pin
from utime import sleep

LED_externo = Pin(15, Pin.OUT)

while True:
    LED_externo.toggle()
    sleep(5)
    