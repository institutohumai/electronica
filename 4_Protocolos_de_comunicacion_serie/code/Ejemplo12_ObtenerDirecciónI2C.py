# Ejemplo N°12: Obtener dirección I2C

from machine import Pin, I2C
from utime import sleep

scl = Pin(1)
sda = Pin(0)
freq = 400000

i2c = I2C(0,sda=sda,scl=scl,freq=freq)

direccion = hex(i2c.scan()[0])

print('La dirección I2C es:', direccion)