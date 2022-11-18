# Ejemplo N°1: Encendido/Apagado de un LED onboard (GP25)

from machine import Pin
from utime import sleep

LED_onboard = Pin(25, Pin.OUT)

LED_onboard.value(1)

sleep(5)

LED_onboard.value(0)