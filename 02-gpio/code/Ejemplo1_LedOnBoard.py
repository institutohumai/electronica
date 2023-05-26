# Ejemplo N°1: Encendido/Apagado del LED onboard 

from machine import Pin
from utime import sleep

LED_onboard = Pin("LED", Pin.OUT)  # LED_onboard = Pin(25, Pin.OUT) si empleamos la RPico

LED_onboard.value(1)

sleep(5)

LED_onboard.value(0)