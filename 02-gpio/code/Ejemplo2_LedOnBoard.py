# Ejemplo N°2: Parpadeo de un LED onboard (GP25)

from machine import Pin
from utime import sleep

LED_onboard = Pin(25, Pin.OUT)

while True:
    LED_onboard.toggle()
    sleep(5)

