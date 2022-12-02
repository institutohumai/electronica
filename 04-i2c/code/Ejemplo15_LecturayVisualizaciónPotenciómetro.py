# Ejemplo N°15: Lectura y visualización de los valores de un potenciómetro

from machine import Pin, ADC, I2C
from utime import sleep
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

potenciometro = ADC(26)

factor_conversion = 3.3 / (65535)

scl = Pin(1)
sda = Pin(0)
freq = 400000

i2c = I2C(0,sda=sda,scl=scl,freq=freq)

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

lcd = I2cLcd(i2c,I2C_ADDR,I2C_NUM_ROWS,I2C_NUM_COLS)

while True:
    voltaje = potenciometro.read_u16() * factor_conversion

    lcd.clear() # Borra cualquier caracter previo que exista
    lcd.move_to(0,0) # Posiciona el cursor en el primer renglón y en la primera columna
    lcd.putstr("Voltaje: ") # Escribir en la pantalla
    lcd.move_to(0,1) # Posiciona el cursor en el segundo renglón y en la primera columna
    lcd.putstr(str (voltaje)) # Escribir en la pantalla
    sleep(1)