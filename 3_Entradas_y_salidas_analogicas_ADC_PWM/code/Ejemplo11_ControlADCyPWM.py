# Ejemplo N°11: Control del brillo de un LED de forma gradual mediante potenciómetro

from machine import Pin, ADC, PWM
from utime import sleep

potenciometro = ADC(26)
LED_PWM = PWM(Pin(15))

LED_PWM.freq(1000)

while True:
    val = potenciometro.read_u16()
    LED_PWM.duty_u16(val)