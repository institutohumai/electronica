# Ejemplo N°17: Almacenar datos de manera continua del sensor de temperatura interno de nuestra Raspberry Pi Pico

from machine import Pin, ADC
from utime import sleep

sensor_temp = ADC(4)

factor_conversion = 3.3 / (65535)

file = open("temps.txt", "w")

while True:
    lectura = sensor_temp.read_u16() * factor_conversion
    temperatura = 27 - (lectura - 0.706)/0.001721

    file.write(str(temperatura) + "\n")
    file.flush()
    sleep(1)