# Ejemplo N°7: Utilización del potenciómetro como divisor de voltaje - Lectura directa

from machine import Pin, ADC
from utime import sleep

potenciometro = ADC(26)

while True:
    print(potenciometro.read_u16())
    sleep(5)
