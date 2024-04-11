#Ejemplo N°8: Utilización del potenciómetro como divisor de voltaje - Lectura con factor de conversión

from machine import Pin, ADC
from utime import sleep

potenciometro = ADC(26)

factor_conversion = 3.3 / (65535) 

while True:
    voltaje = potenciometro.read_u16() * factor_conversion
    print(voltaje)
    sleep(5)