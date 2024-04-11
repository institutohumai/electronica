# Ejemplo N°7: Alarma de movimiento con LED y buzzer

from machine import Pin
from utime import sleep

sensor_pir = Pin(28, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)
buzzer = Pin(14, Pin.OUT)

while True:
    if sensor_pir.value() == 1:
            print("Movimiento detectado")
            led.toggle()
            buzzer.toggle()
            sleep(3)
    else:   
            led.value(0)
            buzzer.value(0)
