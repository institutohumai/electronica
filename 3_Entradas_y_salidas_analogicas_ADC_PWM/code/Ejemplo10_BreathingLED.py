# Ejemplo N°10: Control del brillo de un LED de forma gradual y automática (breathing LED)

from machine import Pin, PWM
from utime import sleep

LED_PWM = PWM(Pin(15))

LED_PWM.freq(1000)

val = 0

while True:
    while val<65535:
        val = val + 50
        sleep(0.05) # 50 milisegundos
        LED_PWM.duty_u16(val)
        print(val)
    while val>0:
        val = val - 50
        sleep(0.05) # 50 milisegundos
        LED_PWM.duty_u16(val)
        print(val)