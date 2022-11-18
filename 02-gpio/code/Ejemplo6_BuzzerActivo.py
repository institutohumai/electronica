# Ejemplo N°6: Alarma intermitente con buzzer activo 

from machine import Pin
from utime import sleep

buzzer = Pin(15, Pin.OUT)

while True:
    buzzer.toggle()
    sleep(5)