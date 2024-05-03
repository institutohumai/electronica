# Ejemplo N°5: Encendido/Apagado de un LED con pulsador NA

from machine import Pin
from utime import sleep

led_externo = Pin(15, Pin.OUT)
pulsador = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if pulsador.value() == 1:
            print("Presionaste el pulsador!")
            led_externo.value(1)
            sleep(2)
            
    led_externo.value(0)