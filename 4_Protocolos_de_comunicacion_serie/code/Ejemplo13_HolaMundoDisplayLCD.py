# Ejemplo N°13: ¡Hola Mundo! en display LCD.

from machine import Pin, I2C
from utime import sleep
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

scl = Pin(1)
sda = Pin(0)
freq = 400000

i2c = I2C(0,sda=sda,scl=scl,freq=freq)

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

lcd = I2cLcd(i2c,I2C_ADDR,I2C_NUM_ROWS,I2C_NUM_COLS)

while True:
    lcd.clear() # Borra cualquier caracter previo que exista
    lcd.move_to(0,0) # Posiciona el cursor en el primer renglón y en la primera columna
    lcd.putstr("Hola Mundo!") # Escribir en la pantalla
    sleep(5)