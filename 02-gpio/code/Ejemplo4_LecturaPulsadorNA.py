# Ejemplo N°4: Lectura de un pulsador NA

from machine import Pin
from utime import sleep

pulsador = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if pulsador.value() == 1:
        print("Presionaste el pulsador!")
        sleep(3)