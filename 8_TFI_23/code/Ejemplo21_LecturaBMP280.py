# Ejemplo N°21: Leer los valores de temperatura y presión provenientes del BMP280

from machine import Pin, I2C
from utime import sleep
from bmp280 import *

scl = Pin(1)
sda = Pin(0)
freq = 100000

bus = I2C(0,sda=sda,scl=scl,freq=freq)

bmp = BMP280(bus, addr = 0x76)

while True:
    temperature = bmp.temperature
    pressure = bmp.pressure
    print('Temperatura: ',temperature,' °C')
    print('Presión: ',pressure,' Pa')
    print() # Renglón en blanco
    sleep(2)
    