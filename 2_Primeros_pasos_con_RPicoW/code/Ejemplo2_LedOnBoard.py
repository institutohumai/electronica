# Ejemplo N°2: Parpadeo de un LED onboard

from machine import Pin
from utime import sleep

LED_onboard = Pin("LED", Pin.OUT)  # LED_onboard = Pin(25, Pin.OUT) si empleamos la RPico

while True:
    LED_onboard.toggle()
    sleep(5)

