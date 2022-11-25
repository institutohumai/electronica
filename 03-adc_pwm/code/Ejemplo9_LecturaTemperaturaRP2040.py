# Ejemplo N°9: Lectura del sensor de temperatura interno de nuestra Raspberry Pi Pico

from machine import Pin, ADC
from utime import sleep

sensor_temp = ADC(4)

factor_conversion = 3.3 / (65535)

while True:
    lectura = sensor_temp.read_u16() * factor_conversion
    temperatura = 27 - (lectura - 0.706)/0.001721
    print(temperatura)
    sleep(3)