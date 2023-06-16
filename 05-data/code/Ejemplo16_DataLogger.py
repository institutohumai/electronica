# Ejemplo N°16: Almacenar un dato del sensor de temperatura interno de nuestra Raspberry Pi Pico

from machine import Pin, ADC
from utime import sleep

sensor_temp = ADC(4)

factor_conversion = 3.3 / (65535)

lectura = sensor_temp.read_u16() * factor_conversion
temperatura = 27 - (lectura - 0.706)/0.001721
print(temperatura)

file = open("temps.txt", "w")
file.write(str(temperatura))
file.close()